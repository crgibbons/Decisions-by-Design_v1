# app.R
# install.packages(c("shiny","sf","dplyr","stringr","tigris","ggplot2","lwgeom","readr","zip","units"))

library(shiny)
library(sf)
library(dplyr)
library(stringr)
library(tigris)
library(ggplot2)
library(lwgeom)
library(readr)
library(zip)

options(tigris_use_cache = TRUE)

# -----------------------------
# Helpers
# -----------------------------

congress_to_year <- function(congress) {
  # tigris convention in practice:
  # 118th -> 2023, 119th -> 2024
  if (congress == 118) return(2023L)
  if (congress == 119) return(2024L)
  stop("Unsupported congress; extend congress_to_year().")
}

pick_crs_meters <- function(state) {
  table <- c(
    "VA" = "EPSG:3968",
    "NC" = "EPSG:32119",
    "SC" = "EPSG:32133",
    "GA" = "EPSG:32134",
    "FL" = "EPSG:3086",
    "TX" = "EPSG:3083",
    "CA" = "EPSG:3310",
    "NY" = "EPSG:32116",
    "PA" = "EPSG:3364",
    "MI" = "EPSG:3078",
    "WA" = "EPSG:2855",
    "OR" = "EPSG:2992"
  )
  if (state %in% names(table)) return(table[[state]])
  "EPSG:5070"  # fallback: NAD83 / Conus Albers (meters)
}

fetch_cd <- function(state, congress, cb = FALSE) {
  year <- congress_to_year(congress)
  cd <- tigris::congressional_districts(state = state, year = year, cb = cb)
  
  cd_field <- names(cd)[grepl("^CD\\d+FP$", names(cd))]
  if (length(cd_field) == 0) stop("No CDxxFP field found in tigris output.")
  cd_field <- cd_field[1]
  
  cd %>%
    mutate(district = paste0(state, "-", str_pad(as.character(.data[[cd_field]]), 2, pad = "0")))
}

compute_bundle <- function(cd_sf, crs_m) {
  cd_m <- st_transform(cd_sf, crs_m)
  
  cd_m <- cd_m %>%
    mutate(
      P  = as.numeric(st_length(st_boundary(geometry))), # meters
      A  = as.numeric(st_area(geometry)),                # m^2
      PP = (4 * pi * A) / (P^2),
      
      r_perim = P / (2 * pi),
      r_area  = sqrt(A / pi),
      S = (2 * pi * r_area) / P,
      
      hull_geom  = st_convex_hull(geometry),
      A_hull     = as.numeric(st_area(hull_geom)),
      hull_ratio = A / A_hull
    )
  
  centers <- st_point_on_surface(cd_m) %>% st_geometry()
  
  circles_P <- st_as_sf(
    cd_m %>% st_drop_geometry() %>% select(district, PP),
    geometry = st_buffer(centers, dist = cd_m$r_perim),
    crs = st_crs(cd_m)
  )
  
  circles_A <- st_as_sf(
    cd_m %>% st_drop_geometry() %>% select(district, S),
    geometry = st_buffer(centers, dist = cd_m$r_area),
    crs = st_crs(cd_m)
  )
  
  hulls <- st_as_sf(
    cd_m %>% st_drop_geometry() %>% select(district, hull_ratio),
    geometry = cd_m$hull_geom,
    crs = st_crs(cd_m)
  )
  
  metrics <- cd_m %>%
    st_drop_geometry() %>%
    transmute(
      district,
      perimeter_km = P / 1000,
      area_km2 = A / 1e6,
      polsby_popper = PP,
      schwartzberg_ratio = S,
      hull_ratio = hull_ratio
    ) %>%
    arrange(district)
  
  list(cd_m = cd_m, circles_P = circles_P, circles_A = circles_A, hulls = hulls, metrics = metrics)
}

plot_overview <- function(cd_m, selected_district) {
  # Whole state, selected district in red; no metric overlay
  ggplot() +
    geom_sf(data = cd_m, fill = "grey92", color = "white", linewidth = 0.3) +
    geom_sf(data = cd_m %>% filter(.data$district == selected_district),
            fill = "red", color = "white", linewidth = 0.4) +
    coord_sf(datum = NA) +
    labs(title = "State overview", subtitle = paste0("Selected: ", selected_district)) +
    theme_minimal(base_size = 13) +
    theme(
      panel.grid = element_blank(),
      axis.text = element_blank(),
      axis.title = element_blank(),
      axis.ticks = element_blank(),
      plot.title = element_text(face = "bold")
    )
}

plot_detail <- function(bundle, selected_district, overlay = c("PP","Schwartzberg","Hull"),
                        show_outline = TRUE) {
  overlay <- match.arg(overlay)
  poly <- bundle$cd_m %>% filter(.data$district == selected_district)
  
  base <- ggplot() +
    coord_sf(datum = NA) +
    theme_minimal(base_size = 13) +
    theme(
      panel.grid = element_blank(),
      axis.text = element_blank(),
      axis.title = element_blank(),
      axis.ticks = element_blank(),
      plot.title = element_text(face = "bold")
    )
  
  if (overlay == "PP") {
    ref <- bundle$circles_P %>% filter(.data$district == selected_district)
    pp  <- poly$PP[[1]]
    base +
      geom_sf(data = ref, fill = NA, linewidth = 1.0, linetype = "dashed") +
      geom_sf(data = poly, alpha = 0.22, linewidth = if (show_outline) 0.7 else 0) +
      labs(
        title = paste0(selected_district, " — Equal-perimeter circle (Polsby–Popper)"),
        subtitle = paste0("PP = ", formatC(pp, format = "f", digits = 3))
      )
  } else if (overlay == "Schwartzberg") {
    ref <- bundle$circles_A %>% filter(.data$district == selected_district)
    s   <- poly$S[[1]]
    base +
      geom_sf(data = ref, fill = NA, linewidth = 1.0, linetype = "dashed") +
      geom_sf(data = poly, alpha = 0.22, linewidth = if (show_outline) 0.7 else 0) +
      labs(
        title = paste0(selected_district, " — Equal-area circle (Schwartzberg)"),
        subtitle = paste0("S = ", formatC(s, format = "f", digits = 3))
      )
  } else {
    ref <- bundle$hulls %>% filter(.data$district == selected_district)
    h   <- poly$hull_ratio[[1]]
    base +
      geom_sf(data = ref, fill = NA, linewidth = 1.0, linetype = "dashed") +
      geom_sf(data = poly, alpha = 0.22, linewidth = if (show_outline) 0.7 else 0) +
      labs(
        title = paste0(selected_district, " — Convex hull overlay"),
        subtitle = paste0("A/A_hull = ", formatC(h, format = "f", digits = 3))
      )
  }
}

# -----------------------------
# UI
# -----------------------------

states <- c(
  "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI",
  "MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT",
  "VT","VA","WA","WV","WI","WY"
)

ui <- fluidPage(
  titlePanel("Compactness Explorer (Congressional Districts)"),
  sidebarLayout(
    sidebarPanel(
      selectInput("state", "State", choices = states, selected = "VA"),
      radioButtons("congress", "Congress", choices = c("118th" = 118, "119th" = 119),
                   selected = 119, inline = TRUE),
      checkboxInput("cb", "Use cartographic boundary (simplified; faster)", value = FALSE),
      hr(),
      uiOutput("district_ui"),
      selectInput("overlay", "Metric overlay (detail plot)",
                  choices = c("Polsby–Popper (equal-perimeter circle)" = "PP",
                              "Schwartzberg (equal-area circle)" = "Schwartzberg",
                              "Convex hull ratio (hull outline)" = "Hull"),
                  selected = "PP"),
      checkboxInput("outline", "Show district outline (detail)", value = TRUE),
      hr(),
      downloadButton("download_csv", "Download metrics CSV")
    ),
    mainPanel(
      fluidRow(
        column(6, plotOutput("overview_plot", height = "420px")),
        column(6, plotOutput("detail_plot", height = "420px"))
      ),
      hr(),
      h4("Metrics (selected district)"),
      tableOutput("metric_table")
    )
  )
)

# -----------------------------
# Server
# -----------------------------
server <- function(input, output, session) {
  
  bundle <- reactive({
    crs_m <- pick_crs_meters(input$state)
    cd <- fetch_cd(input$state, as.integer(input$congress), cb = input$cb)
    compute_bundle(cd, crs_m)
  })
  
  output$district_ui <- renderUI({
    b <- bundle()
    districts <- b$metrics$district
    selectInput("district", "District (CD)", choices = districts, selected = districts[1])
  })
  
  output$overview_plot <- renderPlot({
    req(input$district)
    plot_overview(bundle()$cd_m, input$district)
  })
  
  output$detail_plot <- renderPlot({
    req(input$district)
    plot_detail(bundle(), input$district, overlay = input$overlay, show_outline = input$outline)
  })
  
  output$metric_table <- renderTable({
    req(input$district)
    b <- bundle()
    b$metrics %>%
      filter(.data$district == input$district) %>%
      mutate(
        perimeter_km = round(perimeter_km, 2),
        area_km2 = round(area_km2, 2),
        polsby_popper = round(polsby_popper, 4),
        schwartzberg_ratio = round(schwartzberg_ratio, 4),
        hull_ratio = round(hull_ratio, 4)
      )
  })
  
  output$download_csv <- downloadHandler(
    filename = function() paste0(tolower(input$state), "_cd", input$congress, "_metrics.csv"),
    content = function(file) {
      readr::write_csv(
        bundle()$metrics %>%
          mutate(state = input$state, congress = as.integer(input$congress)) %>%
          relocate(state, congress),
        file
      )
    }
  )
}

shinyApp(ui, server)
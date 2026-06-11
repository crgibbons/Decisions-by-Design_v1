# install.packages(c("sf","dplyr","stringr","tigris","ggplot2","lwgeom"))
library(sf)
library(dplyr)
library(stringr)
library(tigris)
library(ggplot2)
library(lwgeom)

options(tigris_use_cache = TRUE)

OUTDIR <- "va_cd119_metric_panels"
dir.create(OUTDIR, showWarnings = FALSE)

# --- Fetch VA districts (119th Congress) ---
# tigris convention: 119th -> year 2024
va <- tigris::congressional_districts(state = "VA", year = 2024, cb = FALSE)

cd_field <- names(va)[grepl("^CD\\d+FP$", names(va))]
if (length(cd_field) == 0) stop("No CDxxFP field found in data.")
cd_field <- cd_field[1]

va <- va %>%
  mutate(district = paste0("VA-", str_pad(as.character(.data[[cd_field]]), 2, pad = "0")))

# Project to meters so circles are actual circles
va_m <- st_transform(va, 3968)

# Compute planar perimeter/area (consistent for shape comparisons)
va_m <- va_m %>%
  mutate(
    P  = as.numeric(st_length(st_boundary(geometry))), # meters
    A  = as.numeric(st_area(geometry)),                # m^2
    PP = (4 * pi * A) / (P^2),
    
    r_perim = P / (2 * pi),        # equal-perimeter circle radius
    r_area  = sqrt(A / pi),        # equal-area circle radius
    S = (2 * pi * r_area) / P,     # Schwartzberg ratio
    
    hull_geom = st_convex_hull(geometry),
    A_hull = as.numeric(st_area(hull_geom)),
    hull_ratio = A / A_hull
  )

# Centers for circles: interior points
centers <- st_point_on_surface(va_m) %>% st_geometry()

# Build per-district reference geometries
circles_P <- st_as_sf(
  va_m %>% st_drop_geometry() %>% select(district, PP),
  geometry = st_buffer(centers, dist = va_m$r_perim),
  crs = st_crs(va_m)
)

circles_A <- st_as_sf(
  va_m %>% st_drop_geometry() %>% select(district, S),
  geometry = st_buffer(centers, dist = va_m$r_area),
  crs = st_crs(va_m)
)

hulls <- st_as_sf(
  va_m %>% st_drop_geometry() %>% select(district, hull_ratio),
  geometry = va_m$hull_geom,
  crs = st_crs(va_m)
)

# --- Plot helpers (one district at a time) ---
base_theme <- theme_minimal(base_size = 13) +
  theme(
    panel.grid = element_blank(),
    axis.text = element_blank(),
    axis.title = element_blank(),
    axis.ticks = element_blank()
  )

plot_pp <- function(d) {
  poly <- filter(va_m, district == d)
  ref  <- filter(circles_P, district == d)
  ggplot() +
    geom_sf(data = ref, fill = NA, linewidth = 1.0) +
    geom_sf(data = poly, alpha = 0.22, linewidth = 0.6) +
    coord_sf(datum = NA) +
    labs(
      title = paste0(d, " — Equal-perimeter circle (Polsby–Popper)"),
      subtitle = paste0("PP = ", formatC(poly$PP[[1]], format="f", digits=3),
                        "   (circle has same perimeter as district)")
    ) +
    base_theme
}

plot_schwartzberg <- function(d) {
  poly <- filter(va_m, district == d)
  ref  <- filter(circles_A, district == d)
  ggplot() +
    geom_sf(data = ref, fill = NA, linewidth = 1.0, linetype = "dashed") +
    geom_sf(data = poly, alpha = 0.22, linewidth = 0.6) +
    coord_sf(datum = NA) +
    labs(
      title = paste0(d, " — Equal-area circle (Schwartzberg)"),
      subtitle = paste0("S = ", formatC(poly$S[[1]], format="f", digits=3),
                        "   (circle has same area as district)")
    ) +
    base_theme
}

plot_hull <- function(d) {
  poly <- filter(va_m, district == d)
  ref  <- filter(hulls, district == d)
  ggplot() +
    geom_sf(data = ref, fill = NA, linewidth = 1.0, linetype = "dotdash") +
    geom_sf(data = poly, alpha = 0.22, linewidth = 0.6) +
    coord_sf(datum = NA) +
    labs(
      title = paste0(d, " — Convex hull overlay"),
      subtitle = paste0("A/A_hull = ", formatC(poly$hull_ratio[[1]], format="f", digits=3))
    ) +
    base_theme
}

# --- Write 3 × (# districts) PNGs ---
districts <- sort(unique(va_m$district))

for (d in districts) {
  ggsave(file.path(OUTDIR, paste0(d, "_PP.png")),
         plot_pp(d), width = 6.5, height = 6.5, dpi = 300)
  
  ggsave(file.path(OUTDIR, paste0(d, "_Schwartzberg.png")),
         plot_schwartzberg(d), width = 6.5, height = 6.5, dpi = 300)
  
  ggsave(file.path(OUTDIR, paste0(d, "_Hull.png")),
         plot_hull(d), width = 6.5, height = 6.5, dpi = 300)
}

message("Wrote plots to: ", OUTDIR)
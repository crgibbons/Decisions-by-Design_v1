# install.packages(c("sf","dplyr","stringr","tigris","ggplot2","ggrepel"))
library(sf)
library(dplyr)
library(stringr)
library(tigris)
library(ggplot2)
library(ggrepel)

options(tigris_use_cache = TRUE)

get_va_cd <- function(year, congress_label) {
  cd <- tigris::congressional_districts(state = "VA", year = year, cb = FALSE)
  
  cd_field <- names(cd)[grepl("^CD\\d+FP$", names(cd))]
  if (length(cd_field) == 0) stop("No CDxxFP field found in data.")
  cd_field <- cd_field[1]
  
  cd %>%
    mutate(
      cd = .data[[cd_field]],
      district = paste0("VA-", str_pad(as.character(cd), 2, pad = "0")),
      congress = congress_label
    )
}

plot_cd_map <- function(sfobj, title) {
  # project just for nicer label placement
  x <- st_transform(sfobj, 3857)
  
  # label points that stay inside polygons
  pts <- x %>%
    mutate(pt = st_point_on_surface(geometry)) %>%
    st_as_sf() %>%
    select(district, pt) %>%
    st_set_geometry("pt")
  
  # coordinates for ggrepel
  xy <- st_coordinates(pts)
  
  ggplot() +
    geom_sf(data = x, fill = "grey92", color = "grey25", linewidth = 0.6) +
    geom_label_repel(
      data = cbind(pts, xy),
      aes(X, Y, label = district),
      size = 3.2,
      label.size = 0.15,
      point.padding = 0.2,
      box.padding = 0.25,
      min.segment.length = 0
    ) +
    coord_sf(datum = NA) +
    labs(title = title) +
    theme_minimal(base_size = 13) +
    theme(
      panel.grid.major = element_line(linewidth = 0.15),
      plot.title = element_text(face = "bold")
    )
}

# 118th ~ year 2023 ; 119th ~ year 2024 (tigris convention)
va_118 <- get_va_cd(2023, "118th")
va_119 <- get_va_cd(2024, "119th")

p118 <- plot_cd_map(va_118, "Virginia Congressional Districts (118th Congress)")
p119 <- plot_cd_map(va_119, "Virginia Congressional Districts (119th Congress)")

p118
p119

# Optional: save bigger, high-res images
ggsave("va_cd118_map.png", p118, width = 10, height = 7.5, dpi = 300)
ggsave("va_cd119_map.png", p119, width = 10, height = 7.5, dpi = 300)


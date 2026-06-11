import geopandas as gpd
from pyproj import Geod

# --- 1. Load TIGER/Line shapefile ---
# Replace with your downloaded path
gdf = gpd.read_file("tl_2025_us_cd119.shp")

# --- 2. Filter to Virginia ---
va = gdf[gdf["STATEFP"] == "51"]

# Optional: pick one district (e.g., VA-07)
va07 = va[va["CD119FP"] == "07"]

# --- 3. Set up geodesic calculator ---
geod = Geod(ellps="WGS84")

def geodesic_perimeter(geom):
    # Returns meters
    return geod.geometry_length(geom)

# --- 4. Compute perimeters ---
va["perimeter_m"] = va.geometry.apply(geodesic_perimeter)
va["perimeter_km"] = va["perimeter_m"] / 1000
va["perimeter_miles"] = va["perimeter_m"] / 1609.344

print(va[["CD119FP", "perimeter_km", "perimeter_miles"]])
#!/usr/bin/env python3
"""
Compute geodesic perimeters + compactness for Virginia's 119th Congressional Districts
from Census TIGER/Line.

Data source (VA 119th CD shapefile):
  https://www2.census.gov/geo/tiger/TIGER2025/CD/tl_2025_51_cd119.zip

Outputs:
  - Prints a sorted table to stdout
  - Writes CSV: va_cd119_perimeter_compactness.csv
"""

import io
import math
import zipfile
from pathlib import Path

import pandas as pd
import geopandas as gpd
import requests
from pyproj import Geod


URL = "https://www2.census.gov/geo/tiger/TIGER2025/CD/tl_2025_51_cd119.zip"
OUT_CSV = "va_cd119_perimeter_compactness.csv"

# WGS84 ellipsoid for geodesic perimeter/area
GEOD = Geod(ellps="WGS84")


def download_zip(url: str) -> bytes:
    r = requests.get(url, stream=True, timeout=120)
    r.raise_for_status()
    return r.content


def read_shapefile_from_zip(zip_bytes: bytes) -> gpd.GeoDataFrame:
    # Read the shapefile *from inside* the ZIP without writing all components to disk.
    # geopandas can read a "zip://" path if we first write the zip to a temp file.
    # We'll write a single temp zip file for robustness.
    tmp = Path("._tmp_tiger_cd119_va.zip")
    tmp.write_bytes(zip_bytes)
    try:
        gdf = gpd.read_file(f"zip://{tmp.resolve()}")
    finally:
        try:
            tmp.unlink()
        except OSError:
            pass
    return gdf


def geodesic_area_perimeter(geom):
    """
    Returns (area_m2, perimeter_m) for a (Multi)Polygon using pyproj.Geod.
    Area is signed; we take abs(area).
    """
    area_m2, perim_m = GEOD.geometry_area_perimeter(geom)
    return abs(area_m2), perim_m


def main():
    print("Downloading TIGER/Line ZIP…")
    zbytes = download_zip(URL)

    print("Reading shapefile…")
    gdf = read_shapefile_from_zip(zbytes)

    # Filter to Virginia (STATEFP = '51') — should already be VA-only, but keep it explicit.
    if "STATEFP" in gdf.columns:
        gdf = gdf[gdf["STATEFP"] == "51"].copy()

    # District code field per Census record layout: CD119FP
    if "CD119FP" not in gdf.columns:
        raise KeyError("Expected field CD119FP not found. Check TIGER vintage / schema.")

    # Compute metrics
    areas_m2 = []
    perims_m = []
    for geom in gdf.geometry:
        a, p = geodesic_area_perimeter(geom)
        areas_m2.append(a)
        perims_m.append(p)

    gdf["area_m2"] = areas_m2
    gdf["perimeter_m"] = perims_m

    # Unit conversions
    gdf["area_km2"] = gdf["area_m2"] / 1_000_000.0
    gdf["area_mi2"] = gdf["area_m2"] / 2_589_988.110336  # exact m^2 per mi^2

    gdf["perimeter_km"] = gdf["perimeter_m"] / 1000.0
    gdf["perimeter_mi"] = gdf["perimeter_m"] / 1609.344

    # Compactness
    # Polsby–Popper: 4πA / P^2   (A in m^2, P in m)
    gdf["polsby_popper"] = (4.0 * math.pi * gdf["area_m2"]) / (gdf["perimeter_m"] ** 2)

    # Optional: Schwartzberg-style ratio = circumference of equal-area circle / perimeter
    # equal-area circle circumference = 2π sqrt(A/π)
    gdf["schwartzberg_ratio"] = (2.0 * math.pi * (gdf["area_m2"] / math.pi).pow(0.5)) / gdf["perimeter_m"]

    # Build a clean table
    out = (
        gdf.assign(
            district=lambda d: d["CD119FP"].astype(str).str.zfill(2).radd("VA-")
        )[["district", "perimeter_km", "perimeter_mi", "area_km2", "area_mi2", "polsby_popper", "schwartzberg_ratio"]]
        .sort_values("district")
        .reset_index(drop=True)
    )

    # Pretty print
    pd.set_option("display.max_rows", 200)
    pd.set_option("display.width", 140)
    pd.set_option("display.float_format", lambda x: f"{x:0.4f}")
    print("\nVirginia (VA) — 119th Congress districts: perimeter + compactness\n")
    print(out.to_string(index=False))

    # Save CSV
    out.to_csv(OUT_CSV, index=False)
    print(f"\nWrote: {OUT_CSV}")


if __name__ == "__main__":
    main()
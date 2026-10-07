"""Convert an Osmosis .poly file (e.g. Geofabrik texas.poly) to a GeoJSON MultiPolygon.

Usage: python3 scripts/poly2geojson.py texas.poly regions/texas.geojson
"""
import json
import sys


def parse_poly(lines):
    polygons = []  # list of [outer, *holes]
    it = iter(line.strip() for line in lines)
    next(it)  # file name line
    for header in it:
        if header == "END":
            break
        ring = []
        for line in it:
            if line == "END":
                break
            lon, lat = (float(v) for v in line.split())
            ring.append([round(lon, 6), round(lat, 6)])
        if ring and ring[0] != ring[-1]:
            ring.append(ring[0])
        if header.startswith("!"):
            polygons[-1].append(ring)  # hole in the previous outer ring
        else:
            polygons.append([ring])
    return polygons


def main(src, dst):
    with open(src) as f:
        polygons = parse_poly(f)
    feature = {
        "type": "Feature",
        "properties": {"name": "Texas", "source": "Geofabrik texas.poly, (c) OpenStreetMap contributors, ODbL"},
        "geometry": {"type": "MultiPolygon", "coordinates": polygons},
    }
    with open(dst, "w") as f:
        json.dump({"type": "FeatureCollection", "features": [feature]}, f)
        f.write("\n")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

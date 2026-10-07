# back-road-hog-basemap

Monthly offline basemap for [Back Road Hog](https://github.com/johnayers84/back-road-hog) (private), a
personal Texas motorcycle route planner.

A scheduled GitHub Action cuts Texas out of the newest [Protomaps](https://protomaps.com) daily
basemap build and publishes it as a release asset:

- `texas.pmtiles`: Protomaps basemap tiles (schema v4), Texas outline, maxzoom 15, ~1 GB
- `manifest.json`: sha256, size, source build, tiles version, build date

Stable download URLs (always the newest release):

```
https://github.com/johnayers84/back-road-hog-basemap/releases/latest/download/manifest.json
https://github.com/johnayers84/back-road-hog-basemap/releases/latest/download/texas.pmtiles
```

The app downloads from here first. If that fails, it falls back to cutting Texas directly from
`build.protomaps.com` with the same `pmtiles extract` command.

## Contents
This repo contains only OpenStreetMap-derived map data. It contains **no TxDOT data**.

- `regions/texas.geojson`: the Texas outline, converted from Geofabrik's `texas.poly` with
  `scripts/poly2geojson.py`.
- `scripts/select_build.py`: picks the newest build matching the app's style major version.
- `.github/workflows/build-basemap.yml`: runs monthly (3rd, 09:17 UTC) or on demand, keeps the
  newest 3 releases, and skips the run if the newest build was already published.

## Attribution
Map data © [OpenStreetMap contributors](https://www.openstreetmap.org/copyright), available under the
[Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/). Basemap tiles are produced
by [Protomaps](https://protomaps.com). The Texas outline is derived from Geofabrik's `texas.poly`
(© OpenStreetMap contributors, ODbL).

"""Print the newest Protomaps daily build key whose tiles major version matches.

Usage: python3 scripts/select_build.py <major> [builds.json path]
Prints: <key> <version> <uploaded>
"""
import json
import sys


def select(builds, major):
    ok = [b for b in builds if str(b.get("version", "")).split(".")[0] == str(major)]
    if not ok:
        raise SystemExit(f"no build with major version {major}")
    return max(ok, key=lambda b: b["uploaded"])


if __name__ == "__main__":
    major = sys.argv[1]
    with open(sys.argv[2] if len(sys.argv) > 2 else "builds.json") as f:
        b = select(json.load(f), major)
    print(b["key"], b["version"], b["uploaded"])

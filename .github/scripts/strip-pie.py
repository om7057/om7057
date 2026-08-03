#!/usr/bin/env python3
"""Remove the language pie-chart <g> group from github-profile-3d-contrib SVGs.

The pie chart is always appended as `<g transform="translate(40, <y>)">...`
(a sibling of the 3D grid and radar groups, using a comma-separated
transform, unlike the grid cells which use a space-separated one), so it
can be located unambiguously and stripped without touching the rest of
the image.
"""
import glob
import re
import sys

OPEN_RE = re.compile(r'<g transform="translate\(40, [0-9.]+\)">')
TAG_RE = re.compile(r"<g[ >]|</g>")


def strip_pie(svg: str) -> str:
    match = OPEN_RE.search(svg)
    if not match:
        return svg

    depth = 0
    pos = match.start()
    for tag in TAG_RE.finditer(svg, match.start()):
        if tag.group().startswith("<g"):
            depth += 1
        else:
            depth -= 1
        if depth == 0:
            return svg[:pos] + svg[tag.end():]
    return svg


def main(paths: list[str]) -> None:
    files = [f for pattern in paths for f in glob.glob(pattern)]
    for path in files:
        with open(path, "r", encoding="utf-8") as fh:
            content = fh.read()
        stripped = strip_pie(content)
        if stripped != content:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(stripped)
            print(f"stripped pie chart from {path}")


if __name__ == "__main__":
    main(sys.argv[1:])

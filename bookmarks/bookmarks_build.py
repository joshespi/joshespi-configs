#!/usr/bin/env python3
"""Convert bookmarks.toml to a browser-importable Netscape HTML file.

No dependencies — uses tomllib from the Python 3.11+ standard library.

Usage:
    python3 bookmarks_build.py
    python3 bookmarks_build.py --input bookmarks.toml --output bookmarks_import.html
"""

import argparse
import html
import sys
import tomllib
from pathlib import Path


def render_entries(entries: list, indent: int) -> list[str]:
    pad = "    " * indent
    lines = []
    for entry in entries:
        title = html.escape(entry.get("title", ""))
        url = entry.get("url", "")
        lines.append(f'{pad}<DT><A HREF="{url}">{title}</A>')
    return lines


def render_section(name: str, value, indent: int) -> list[str]:
    pad = "    " * indent
    folder_name = name.replace("_", " ").title()

    if isinstance(value, list):
        inner = render_entries(value, indent + 1)
    elif isinstance(value, dict):
        inner = []
        for sub_name, sub_value in value.items():
            inner.extend(render_section(sub_name, sub_value, indent + 1))
    else:
        return []

    return [
        f"{pad}<DT><H3>{html.escape(folder_name)}</H3>",
        f"{pad}<DL><p>",
        *inner,
        f"{pad}</DL>",
    ]


def build(input_path: Path, output_path: Path) -> None:
    with open(input_path, "rb") as f:
        data = tomllib.load(f)

    lines = [
        "<!DOCTYPE NETSCAPE-Bookmark-file-1>",
        '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">',
        "<TITLE>Bookmarks</TITLE>",
        "<H1>Bookmarks</H1>",
        "<DL><p>",
    ]

    for section_name, section_value in data.items():
        lines.extend(render_section(section_name, section_value, indent=1))

    lines.append("</DL>")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Written: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build browser bookmark import file from TOML.")
    parser.add_argument("--input", default="bookmarks.toml", help="Source TOML file")
    parser.add_argument("--output", default="bookmarks_import.html", help="Output HTML file")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    try:
        build(input_path, output_path)
    except FileNotFoundError:
        sys.exit(f"Input file not found: {input_path}")


if __name__ == "__main__":
    main()

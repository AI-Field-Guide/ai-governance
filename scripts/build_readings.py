#!/usr/bin/env python3
"""Generate the reading tables in _generated/ from data/readings.yml.

Each week page includes its tables with {{< include _generated/<section>-<kind>.md >}}.
readings.qmd includes _generated/all.md.
"""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_generated"

SECTION_TITLES = {
    "week-1": "Week 1 · Why AI governance",
    "week-2": "Week 2 · AI geopolitics",
    "week-3": "Week 3 · Tools of the policymaker",
    "week-4": "Week 4 · Europe & the Netherlands",
    "standalone-dna": "Standalone · AI and DNA",
    "standalone-php": "Standalone · The PHP incident",
}
KIND_TITLES = {"required": "Lecture readings", "optional": "Optional", "discussion": "Discussion"}


def archived(r):
    return r.get("archived") or f"https://web.archive.org/web/{r['url']}"


def table(rows):
    lines = [
        "::: {.reading-table}",
        "",
        "| Reading | Time | Links |",
        "|---|---|---|",
    ]
    for r in rows:
        title = r["title"].replace("|", "\\|")
        title = f"⭐ **{title}**" if r.get("core") else title
        if r.get("part"):
            title += f"<br><small>{r['part']}</small>"
        mins = f"~{r['minutes']} min" if r.get("minutes") else ""
        links = f"[Source]({r['url']}) · [Archived]({archived(r)})"
        lines.append(f"| {title} | {mins} | {links} |")
    lines += ["", ":::", ""]
    return "\n".join(lines)


def main():
    readings = yaml.safe_load((ROOT / "data" / "readings.yml").read_text())
    OUT.mkdir(exist_ok=True)
    for section in SECTION_TITLES:
        for kind in KIND_TITLES:
            rows = [r for r in readings if r["section"] == section and r["kind"] == kind]
            (OUT / f"{section}-{kind}.md").write_text(table(rows) if rows else "_None._\n")

    parts = []
    for section, stitle in SECTION_TITLES.items():
        parts.append(f"## {stitle}\n")
        for kind, ktitle in KIND_TITLES.items():
            rows = [r for r in readings if r["section"] == section and r["kind"] == kind]
            if rows:
                parts.append(f"### {ktitle}\n\n{table(rows)}")
    (OUT / "all.md").write_text("\n".join(parts))
    print(f"Wrote {len(readings)} readings to {OUT}")


if __name__ == "__main__":
    main()

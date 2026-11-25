# AI Governance · AI Field Guide

A four-week module on AI governance, focused on Europe and the Netherlands.
**Live site: https://ai-field-guide.github.io/ai-governance/**

| Week | Topic |
|---|---|
| 1 | Why AI governance: risks, safety vs governance |
| 2 | AI geopolitics: US, China & middle powers |
| 3 | Tools of the policymaker: incidents, system cards, scenarios |
| 4 | Europe & the Netherlands: EU AI Act, AI Office, Dutch oversight |

Plus a discussion series, standalone sessions, and a final essay (research proposal).

## Structure

```
data/readings.yml          ← every reading (single source of truth)
scripts/build_readings.py  ← generates reading tables (runs automatically on render)
index.qmd                  ← start page
week-1.qmd … week-4.qmd    ← lecture weeks
discussions.qmd            ← discussion series
standalone.qmd             ← standalone sessions
essay.qmd                  ← final essay guide
readings.qmd               ← all readings in one list
about.qmd                  ← about, sources, contributing
```

## Edit locally

```bash
pip install pyyaml
quarto preview
```

Pushing to `main` publishes the site via GitHub Actions.

Independent study guide based on the SAIN Utrecht AI Governance course (Nov–Dec 2026). Not an official SAIN publication.

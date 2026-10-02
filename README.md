# Jeet Thakwani — personal website

Plain static GitHub Pages site at `jeet.thakwani.com`, from `J999UCL/J999UCL.github.io`. The separate `myCV` repository serves `/myCV/`.

## Content and build

- `index.html`: plain introduction and links.
- `projects/index.html`: 11 project write-ups.
- `projects.json`: titles, descriptions, tags, source CV references and route aliases.
- `content/<slug>.html`: source article fragments. Edit these to update write-ups.
- `assets/projects/`: original or source-backed charts, route previews, and Perpetua render video.
- `scripts/build.py`: generates pages and aliases; run `python3 scripts/build.py` after edits.
- `plain.css`: active styling; no JavaScript or external font dependencies.

The Google CV URLs `/projects/perpetua`, `/projects/lemon`, `/projects/rl`, `/projects/skateboardai`, and `/projects/mv-tracker++` all serve complete articles. Older routes remain available. `/projects/ucl-cli` is also supported.

## Preview

Run `python3 -m http.server 8085 --bind 127.0.0.1` and open http://127.0.0.1:8085/.

## Evidence and media

Articles use the CV workspace, implementation code, original presentation/report figures, experiment logs, and published paper tables. Graph captions specify metrics and evaluation conditions. The Perpetua video is an existing rendered sequence, not a model prediction. The paper's Rerun recordings are linked externally rather than embedding a large recording download in the page.

Detailed source audits in `research/` are local-only, gitignored, and excluded from GitHub Pages. `_config.yml` also excludes generator inputs and old styles/scripts from Pages output. No raw experiment diaries, private repository links, or customer data are published by the articles.

## Deployment

GitHub Pages publishes the root of `main`. Preserve `CNAME` and both original CV PDFs. Older design assets remain on disk but are not loaded.

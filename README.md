# fccw-docs

Documentation repository for the FCCW project. This repository contains the source (Markdown) for the project's documentation site, build/configuration files for MkDocs, and utility scripts used to generate and manage content.

This `README.md` is intentionally written to be used as a context file for automated agents and code-generation tools (Codex-style). It highlights where useful context lives, how to set up a local environment, and best practices for reading and modifying the content.

## Quick start (Windows PowerShell)

Prerequisites:

- Python 3.12+ (project previously used CPython 3.12 based on cache files)
- Git (optional, for fetching updates)

Typical setup and build steps (PowerShell):

```powershell
# create virtual environment (only if you don't already have one in the repo)
python -m venv venv
# activate the venv (this repo commonly uses `venv` at the project root)
& $PWD\venv\Scripts\Activate.ps1
# install dependencies
pip install -r requirements.txt
# build the MkDocs site
mkdocs build
# or serve locally for development
mkdocs serve
```

If your environment already contains a `venv` folder in the repository root, activate it instead of creating a new one.

There are alternative build configs in the repo: `mkdocs.online.yml` and `mkdocs.offline.yml`. Use `mkdocs build -f <file>` to build with a specific config.

## Project layout (notable paths)

- `docs/` — source Markdown used by MkDocs. Primary location for content authors and agents.
- `mkdocs.yml`, `mkdocs.online.yml`, `mkdocs.offline.yml` — MkDocs site configuration files.
- `site/`, `Guides/`, `includes/`, `overrides/` — generated or shipped site artefacts and templates.
- `utils/` — utility scripts used during content generation and conversion (Python scripts like `build-force.py`, `doc_convert.py`, `fix_images.py`).
- `search/` — search index files such as `search_index.json` useful for quick lookups.
- `requirements.txt` / `requirements.in` — Python dependencies for build tools and scripts.

## Using this repository as an agent/Codex context

Guidance for consumers (agents, code generation tools):

- Prefer the `docs/` directory for authoritative, editable text content. It's the canonical source for pages.
- For rendered HTML or quick lookups, `site/` and `Guides/` contain built pages; use them when you need final markup or static assets.
- Read the top-level `mkdocs.yml` (and the alternate configs) to understand navigation and metadata used across the site.
- `utils/` contains scripts which transform or generate content; inspect them when changes to generated content are required.
- Use `search/search_index.json` or `search/search_index.js` for programmatic search across the built site.

Practical tips:

- Avoid loading large binary files (for example `FCCW-FM.pdf`) into memory when providing context; reference them by path instead.
- Focus on Markdown (`*.md`) files in `docs/` for text operations like summarization, rewriting, or extracting facts.
- Respect front-matter and MkDocs conventions. Do not edit generated `site/` files — change the source in `docs/` and rebuild.

## Small contract for automation

- Input: natural-language prompt or task + optional path(s) inside the repo.
- Output: modified files (usually `docs/*.md`), suggested edits, or a built site artifact.
- Success: edits are applied to `docs/` and pass a local `mkdocs build` without configuration errors.
- Error modes: missing/incorrect Python environment, missing dependencies, or parity issues between `mkdocs.yml` and content.

## Edge cases to watch

- Non-UTF-8 files or unexpected encodings in older content.
- Large assets and PDFs that should not be inlined into agent prompts.
- Generated files in `site/` that will be overwritten by builds — edit only sources.

## Troubleshooting

- If `mkdocs build` fails, run it with `--verbose` to get more info, and confirm the Python environment and `requirements.txt` are installed.

## Next steps for contributors and agents

- Edit source Markdown in `docs/` and use `mkdocs serve` to preview changes locally.
- For programmatic tasks, index `docs/`, `mkdocs.yml`, and `utils/` as primary context sources.

---

Status: This `README.md` was added to the repository root to be used as a concise context file for agents and Codex tasks.

Requirements coverage:

- Create `README.md` in repo root: Done
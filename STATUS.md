# STATUS.md — OCR and Handwriting Guide

Last updated: 2026-11-06

## What was built

A complete beginner manual teaching anyone to turn **paper, receipts, and
handwritten notes into clean, searchable text** using free OCR tools and free
AI assistants. Warm plain-English voice throughout ("like a friend would
explain it"); education only — it deliberately contains **no medical-, legal-,
or tax-retention advice**.

Deliverables:

- **`docs/`** — the manual in Markdown (10 chapters):
  - `00-start-here.md` — orientation, privacy rules, what you need
  - `01-scan-like-a-pro.md` — phone-scanning angle/light/steadiness technique
  - `02-free-ocr-tools.md` — the free-tool landscape by situation (phone
    built-ins, Google Lens/Drive/Docs OCR, Windows PowerToys, OneNote,
    Tesseract, free AI chats), with a cloud-vs-local table
  - `03-ai-cleanup.md` — five copy-paste AI prompts for faithful cleanup,
    formatting, receipts, handwriting, and summarizing/indexing
  - `04-receipts.md` — receipt capture habit + OCR/AI extraction workflow and
    folder structure (education only; no retention/tax advice)
  - `05-handwriting.md` — realistic accuracy expectations, tool ranking,
    step-by-step transcription workflow, escalation ladder
  - `06-fixing-ocr-errors.md` — classic OCR confusion table, 8-line proofread
    checklist, "flag, don't fix" AI proofread prompt, accuracy protocol
  - `07-filing.md` — search-first filing system: naming, 4-line headers,
    grep/Spotlight/Explorer search skills, backups, upkeep habits
  - `08-troubleshooting.md` — master symptom table + 5-minute reset
  - `09-cheat-sheet.md` — everything condensed to half a page
- **`site/`** — polished static HTML edition (10 pages, warm cream/terracotta
  design). Inline CSS in each page; **no build step needed** — just open
  `site/index.html` in a browser. Generated from `docs/` by
  `tools/build_site.py` so the two stay in sync.
- **`tools/build_site.py`** — optional one-command regenerator of the HTML
  site from the Markdown (`python3 tools/build_site.py`; requires the
  `markdown` package).
- **`README.md`** — overview, chapter index, quick start, credits.
- **`LICENSE`** — MIT, copyright line exactly
  `Copyright (c) 2026 Asdale Dynamics, LLC`.

Distinct intentionally from the companion projects: `pdf-everyday-handbook`
(PDF manipulation day-to-day) and `photo-digitizing-guide` (archival family
photos). This guide covers *document text extraction*: phone-scan technique,
free OCR tools, AI cleanup, receipts, handwriting, error fixing, and filing.

Credits to **Asdale Dynamics, LLC** appear in README, LICENSE, docs, and the
site footer. No secrets, API keys, or personal data in any file (verified by
scan); no push, no remotes, no publishing.

## How to run it

- **Read the manual:** open any `docs/*.md` file, or open **`site/index.html`**
  in any browser (double-click works — plain static HTML, inline styles,
  zero dependencies, no server).
- **Regenerate the HTML site after editing `docs/`:**
  ```bash
  python3 tools/build_site.py
  ```
  (Python 3.9+ with the `markdown` package installed.)

## Verification results

- Site build runs cleanly: `python3 tools/build_site.py` →
  `Built site/: 10 pages` (index + 9 chapters), rerun is idempotent.
- HTML validated with an in-context tag-balance parser (HTMLParser): all 10
  pages **OK** (stack balanced, no mismatches, no unclosed tags).
- Link check: all internal `href`s resolve to existing files; **0 broken
  links** across the 10 pages (external links are to dylanasdale.github.io
  only).
- Content sanity: tables render as real `<table>` in tools.html and
  fixing-errors.html; contact prompts render verbatim in code blocks; the
  index hero + table of contents render correctly.
- Secrets/personal-data scan (regex over md/html/py): clean — only innocuous
  prose matches ("the secret is…" in chapter 1; a README sentence about *not*
  containing API keys).
- LICENSE copyright line verified character-exact.

## Known gaps

- External links to companion guides (PDF handbook, photo digitizing) are
  textual references, not hyperlink-verified sibling projects.
- The HTML generation requires the Python `markdown` package if you ever
  need to rebuild the site (the committed `site/` itself needs nothing).
- Tool screenshots: UI steps are described in words only (deliberate — app
  menus move), so a few button labels may drift from app updates.
- No automated unit-test suite; verification is the build + HTML/link/data
  checks described above (a static-content project; nothing executable ships
  as part of the site itself).

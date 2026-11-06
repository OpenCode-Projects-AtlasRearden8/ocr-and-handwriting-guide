#!/usr/bin/env python3
"""Regenerate the static HTML site in site/ from the Markdown manual in docs/.

The generated site needs NO build step to view: just open site/index.html.
This script is an optional maintenance tool that keeps site/ in sync with
docs/. Run from the repository root:

    python3 tools/build_site.py

Requires: Python 3.9+, the `markdown` package (e.g. pip install markdown).
"""

from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent

CHAPTERS = [
    ("00-start-here", "Start Here", "start"),
    ("01-scan-like-a-pro", "Scanning Tips", "scanning"),
    ("02-free-ocr-tools", "Free OCR Tools", "tools"),
    ("03-ai-cleanup", "AI Cleanup", "ai-cleanup"),
    ("04-receipts", "Receipts", "receipts"),
    ("05-handwriting", "Handwriting", "handwriting"),
    ("06-fixing-ocr-errors", "Fixing Errors", "fixing-errors"),
    ("07-filing", "Filing", "filing"),
    ("08-troubleshooting", "Troubleshooting", "troubleshooting"),
    ("09-cheat-sheet", "Cheat Sheet", "cheat-sheet"),
]

CSS = """
:root {
  --paper: #fbf7f0;
  --ink: #33302a;
  --soft: #6b6455;
  --accent: #b3562d;
  --accent-dark: #8a3f1e;
  --card: #ffffff;
  --line: #e7dfd2;
  --code-bg: #f3ede2;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: Georgia, "Iowan Old Style", "Times New Roman", serif;
  line-height: 1.7;
  font-size: 18px;
}
code, pre, kbd { font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace; font-size: 0.82em; }
header.site {
  background: #2e2a24;
  color: #f4efe6;
  padding: 0.6rem 1rem;
}
header.site .inner {
  max-width: 900px; margin: 0 auto;
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.4rem 1rem;
}
header.site .brand {
  font-weight: bold; letter-spacing: 0.03em; text-decoration: none;
  color: #f4b267; font-size: 0.95rem;
}
header.site nav { display: flex; flex-wrap: wrap; gap: 0.35rem 0.9rem; }
header.site nav a {
  color: #e8e1d3; text-decoration: none; font-size: 0.85rem;
  font-family: "Helvetica Neue", Arial, sans-serif;
}
header.site nav a:hover { color: #f4b267; }
main.page {
  max-width: 900px; margin: 0 auto; padding: 2rem 1.2rem 3rem;
}
.kicker {
  font-family: "Helvetica Neue", Arial, sans-serif;
  text-transform: uppercase; letter-spacing: 0.14em;
  color: var(--accent); font-size: 0.78rem; margin-bottom: 0.4rem;
}
h1 { font-size: 2.1rem; line-height: 1.25; margin: 0 0 1rem; }
h2 { font-size: 1.5rem; margin-top: 2.4em; color: var(--accent-dark); }
h3 { font-size: 1.15rem; margin-top: 1.8em; }
p { margin: 1em 0; }
a { color: var(--accent); }
a:hover { color: var(--accent-dark); }
hr { border: none; border-top: 1px solid var(--line); margin: 2.5em 0; }
blockquote {
  margin: 1.4em 0; padding: 0.4em 1.2em;
  border-left: 4px solid var(--accent); background: var(--card);
  border-radius: 0 8px 8px 0; color: var(--soft);
}
code {
  background: var(--code-bg); padding: 0.12em 0.35em; border-radius: 4px;
}
pre {
  background: #2e2a24; color: #f1ebdd; padding: 1rem 1.2rem;
  border-radius: 10px; overflow-x: auto; line-height: 1.55;
}
pre code { background: transparent; color: inherit; padding: 0; font-size: 0.85rem; }
table { border-collapse: collapse; width: 100%; margin: 1.4em 0; font-size: 0.92rem; }
th, td { border: 1px solid var(--line); padding: 0.5em 0.7em; text-align: left; }
th { background: var(--code-bg); }
tr:nth-child(even) td { background: rgba(255,255,255,0.5); }
.pager {
  display: flex; justify-content: space-between; gap: 1rem;
  margin-top: 3rem; border-top: 1px solid var(--line); padding-top: 1.2rem;
  font-family: "Helvetica Neue", Arial, sans-serif; font-size: 0.9rem;
}
.pager a { text-decoration: none; }
.pager a:hover { text-decoration: underline; }
footer.site {
  background: #2e2a24; color: #b8afa0; text-align: center;
  padding: 1.6rem 1rem; font-size: 0.85rem;
  font-family: "Helvetica Neue", Arial, sans-serif;
}
footer.site a { color: #f4b267; }
.hero {
  background: linear-gradient(160deg, #fdf3e4, var(--paper));
  border: 1px solid var(--line); border-radius: 14px;
  padding: 2.2rem 2rem; margin-bottom: 2.4rem;
}
.hero h1 { margin-bottom: 0.5rem; }
.hero p.tagline { color: var(--soft); font-size: 1.12rem; }
.toc { list-style: none; padding: 0; margin: 1.6rem 0 0; }
.toc li { margin: 0.45em 0; padding-left: 0; }
.toc a {
  text-decoration: none; font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 1rem; display: inline-block; padding: 0.25em 0;
}
.toc .n {
  display: inline-block; min-width: 2.2em; color: var(--accent);
  font-weight: bold;
}
.toc a:hover .t { text-decoration: underline; }
.note {
  background: var(--card); border: 1px solid var(--line);
  border-radius: 10px; padding: 1rem 1.3rem; margin: 1.4em 0; font-size: 0.95rem;
}
"""


def href_for(slug: str) -> str:
    """Chapter 00 lives at index.html (the home page)."""
    return "index.html" if slug == "start" else f"{slug}.html"


def nav_html(current: str) -> str:
    links = "\n      ".join(
        (f'<a href="{href_for(slug)}" class="active">{label}</a>'
         if slug == current else f'<a href="{href_for(slug)}">{label}</a>')
        for _, label, slug in CHAPTERS
    )
    return f"""
  <header class="site">
    <div class="inner">
      <a class="brand" href="index.html">OCR &amp; Handwriting Guide</a>
      <nav>
        {links}
      </nav>
    </div>
  </header>
"""


def page(title: str, kicker: str, body: str, current: str, prev_slug: str | None,
         next_slug: str | None) -> str:
    pager_parts = []
    if prev_slug:
        pager_parts.append(f'<a href="{href_for(prev_slug)}">&larr; Previous</a>')
    else:
        pager_parts.append("<span></span>")
    if next_slug:
        pager_parts.append(f'<a href="{href_for(next_slug)}">Next &rarr;</a>')
    pager = '<div class="pager">\n      ' + "\n      ".join(pager_parts) + "\n    </div>"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Turn paper, receipts, and handwritten notes into clean, searchable text with free OCR and AI. A beginner guide by Asdale Dynamics, LLC.">
<title>{title} &mdash; OCR &amp; Handwriting Guide</title>
<style>{CSS}</style>
</head>
<body>
{nav_html(current)}
<main class="page">
  <p class="kicker">{kicker}</p>
  {body}
  {pager}
</main>
<footer class="site">
  <p>OCR &amp; Handwriting Guide — free, education only, not tax/legal/medical advice.<br>
  Built with care by <a href="https://dylanasdale.github.io">Asdale Dynamics, LLC</a>.
  Companion guides: <a href="https://dylanasdale.github.io">dylanasdale.github.io</a></p>
</footer>
</body>
</html>
"""


MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists", "smarty"]

md_converter = markdown.Markdown(extensions=MD_EXTENSIONS)


def convert(md_text: str) -> str:
    md_converter.reset()
    return md_converter.convert(md_text)


def build_chapters() -> None:
    for i, (stem, label, slug) in enumerate(CHAPTERS):
        if i == 0:
            continue  # chapter 00 is the home page, built by build_index()
        src = ROOT / "docs" / f"{stem}.md"
        html_body = convert(src.read_text(encoding="utf-8"))
        title = f"Chapter {i}: {label}"
        prev_slug = CHAPTERS[i - 1][2] if i > 1 else None
        next_slug = CHAPTERS[i + 1][2] if i + 1 < len(CHAPTERS) else None
        out = page(
            title=title,
            kicker=f"Chapter {i} of 9" if i else f"Chapter {i} of 9  —  start here",
            body='<div class="doc">' + html_body + "\n  </div>",
            current=slug,
            prev_slug=prev_slug,
            next_slug=next_slug,
        )
        (ROOT / "site" / f"{slug}.html").write_text(out, encoding="utf-8")


def build_index() -> None:
    intro = (ROOT / "docs" / "00-start-here.md").read_text(encoding="utf-8")
    intro_html = convert(intro)
    toc_items = "\n".join(
        f"""    <li><span class="n">{i if i else '&rarr;'}</span>
        <a href="{href_for(slug)}"><span class="t">{label}</span></a></li>"""
        for i, (_, label, slug) in enumerate(CHAPTERS)
    )
    hero = f"""<div class="hero">
  <h1>Your Paper, Made Searchable</h1>
  <p class="tagline">Turn paper, receipts, and handwritten notes into clean,
  searchable text — using free OCR and free AI. No gadgets, no subscriptions,
  explained like a friend would explain it.</p>
  <p><strong>The pipeline:</strong> Paper &rarr; flat, side-lit phone photo &rarr;
  OCR &rarr; AI cleanup &rarr; good filename &rarr; search finds it forever.</p>
  <ul class="toc">
{toc_items}
  </ul>
</div>
    """.strip()
    # Drop the doc's own H1 and first paragraph (the hero replaces them).
    if "<h1>" in intro_html:
        intro_html = intro_html.split("</h1>", 1)[1]
    head, sep, rest = intro_html.partition("<hr")
    body = hero + head
    if sep:
        body += "<hr" + rest
    prev_slug, next_slug = None, "scanning"
    out = page(
        title="OCR & Handwriting Guide",
        kicker="A free beginner manual — Asdale Dynamics, LLC",
        body="<div class=\"doc\">" + body + "\n  </div>",
        current="start",
        prev_slug=prev_slug,
        next_slug=next_slug,
    )
    (ROOT / "site" / "index.html").write_text(out, encoding="utf-8")


def main() -> None:
    (ROOT / "site").mkdir(exist_ok=True)
    build_index()
    build_chapters()
    pages = sorted(p.name for p in (ROOT / "site").glob("*.html"))
    print(f"Built site/: {len(pages)} pages -> {', '.join(pages)}")


if __name__ == "__main__":
    main()

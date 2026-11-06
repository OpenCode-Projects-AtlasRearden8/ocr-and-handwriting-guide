# Chapter 7: File It So You Can Find It (Search-First Filing)

You have clean text now. Congratulations — and also welcome to the moment
where digitizing projects either thrive or quietly dissolve into
`Documents/new folder/new folder (2)/final_final2.txt`. This chapter keeps
yours thriving with a filing system built around one idea: **you will find
things by searching, not by browsing.**

## The one principle: optimize for search, not for sorting

Most filing advice (nested folder trees, rigid category codes) is designed
for humans browsing with their eyes. But your transcripts are *text* — and
text is searchable. The modern filing mindset:

- **Flat-ish structure, few folders.** Think 3 levels deep, max.
- **Rich filenames.** The filename is your first line of metadata.
- **A keyword line inside the file.** The second line of metadata, and the
  reason searching by topic works years later.
- **Everything lives under ONE root.** Not scattered between Desktop,
  Documents, and Downloads.

## The recommended structure (copy this)

One folder per year, one per month only when volume justifies it:

```text
Documents/
  Scans/                       ← THE root; everything digitized lives under here
    2026/
      2026-03-receipts.md
      2026-03-receipts/        ← (optional) the source images for that table
        2026-03-02-cedar-hardware.jpg
      2026-04-12-aunt-june-letter.md
      2026-04-notebook-ideas.md
      2026-04-20-contract-quote.md
    2027/
      ...
```

Rules that keep it alive:

1. **`YYYY-MM-DD` at the front of datable documents.** Sorting by name =
   sorting by time, automatically, forever.
2. **Who/what in the name:** `aunt-june-letter`, `cedar-hardware-receipt`.
   Future you will type `aunt-june` into a search box and be *done*.
3. **Folders for collections, files for items.** A pile of receipts becomes
   one file per month plus an images folder. A notebook becomes one file per
   page or per session — usually one file per session, honestly, because
   twenty page-files share the same theme and Searches work better with
   fewer, chunkier files.

## The five-line file header (small habit, huge payoff)

At the top of every transcript file, add a tiny header — this is what makes
topic-search work three years from now:

```markdown
<!--
Subject: letters from Aunt June
Tags: family, correspondence, farm
Source: photo of original letter, 1987, in family album p. 14
Transcribed: 2026-04-12
-->
```

(Or in plain text, without the comment marks — the point is the four lines,
not the exact syntax.) Notice what's here and what's *not*: topic, tags,
provenance, date of transcription. **No personal data beyond what's needed
to know what the document is.** If the letter contains a bank account or an
ID number, that stays in the document body — and if you ever share or
publish the file, Chapter 1's privacy rules apply first: strip identifiers.

## Naming cheat sheet

| Kind of document | Name pattern | Example |
|---|---|---|
| Dated letter/correspondence | `YYYY-MM-DD-person-topic` | `2026-04-12-aunt-june-letter.md` |
| Receipt batch | `YYYY-MM-receipts` | `2026-03-receipts.md` |
| Notebook session | `YYYY-MM-topic-notes` | `2026-04-project-ideas-notes.md` |
| Single item image | `YYYY-MM-DD-merchant-item` | `2026-03-02-cedar-hardware.jpg` |
| Reference/how-to | `topic-name` | `recipes-preserve-tomatoes.md` |

Readable words, all lowercase, hyphens between — filenames that don't need
decoding, that sort cleanly, and that search *loves*.

## Searching: the skills, in order of usefulness

1. **Filename search** — in Explorer/Finder or your file manager's search
   box, just type part of a name: `aunt-june`, `receipts-2026`.
2. **Full-text search** — all major operating systems search *inside* plain
   text files natively (Windows: search box in Explorer, enable "Always
   search file names and contents" in Folder Options for .txt; macOS:
   Spotlight finds .md/.txt content instantly; Linux: GNOME Files or the
   `grep` command). This is why you saved things as **plain text or
   Markdown** and not PDFs or images — the search index can't read pixels.
3. **`grep` power move (any OS, one line):** searching *every* file for a
   phrase:
   ```bash
   grep -ril "compost" Documents/Scans/
   ```
   (`-ril` = names + contents, case-insensitive; lists every file in your
   Scans mentioning "compost" in under a second, even across years.)
4. **The AI as librarian** — paste several transcripts into a free AI chat
   and ask: *"Across these documents, where is [topic] mentioned?"* —
   cross-notebook questions answered in one request. (This is your local
   preview of what future automation could do; see the *Local AI Starter
   Guide* when you're ready.)

## Backups: the non-negotiable part

A digitized archive has *one* machine as a single point of failure unless
you add at least one more copy. Options, cheapest first:

1. **A second physical copy** — USB drive or SD card, copied monthly
   (calendar reminder). Keep it somewhere else than the computer (different
   room, or literally off-site).
2. **A cloud backup of the Scans folder** — encrypted, set-once
   (many people use paid plans for this; that's your call and your budget;
   free tiers work for modest archives).
3. **Periodic archive snapshot** — once a year, zip the year's folder
   (`scans-2026-archive.zip`) and store it. Freezing an archive makes it
   tamper-evident and simple to copy elsewhere.

**Rule of thumb: two copies, one of them elsewhere.** (For what *not* to
treat like ordinary scans — medical paperwork has special retention rules
we don't cover here — revisit Chapter 1's privacy notes and ask a
professional for retention guidance.)

## Keeping the system alive (the honest part)

Every filing system decays without a reset habit. Two that work:

- **Weekly 10 minutes:** scan the week's paper receipts/notes (capture job),
  drag raw phone photos into `Scans/YYYY/images/`, rename files whose names
  start with `Screenshot_` or `IMG_` (or batch-rename with the OS rename
  tool).
- **Yearly 30 minutes:** create next year's folder, re-verify backup copy,
  zip last year, skim that nothing important is stranded in Downloads.

That's it. No custom software, no subscription — just one root folder, rich
names, tiny headers, and search.

---

Next: Chapter 8 — when something goes wrong (and it will), the
troubleshooting table that fixes it in five minutes.

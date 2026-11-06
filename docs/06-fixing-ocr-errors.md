# Chapter 6: Fixing OCR Errors — The Field Guide

Even after the AI cleanup pass, transcripts have *tells* — recurring error
patterns you can spot and fix at a glance. This chapter trains the
pattern-recognition (yours, not the AI's) so a quick skim catches 95% of
errors, plus a checklist-driven pass for when accuracy really matters.

## The classic OCR confusions (memorize five, fix most)

| OCR reads | Should be | Why | Example |
|---|---|---|---|
| `0` (zero) | `O` (letter) / vice versa | identical shapes | `B0STON` → `BOSTON` |
| `l` / `1` / `I` / `\|` | each other | identical shapes | `1mportant` → `Important` |
| `rn` | `m` (and reverse) | ligature-like merge | `modeIn` → `modern`, `damged`→`damaged`*(check!)* |
| `cl` | `d` | pair-shape merge | `cIoud` → `cloud` |
| `5` / `S`, `8` / `B`, `6` / `b` | each other | project-thin shapes | `55c` → `SSC`? *check context* |
| `é` `e` accents dropped or scrambled | accented originals | engine charset limits | `cafe` → `café` |
| straight quotes `'` `"` | curly `’` `“”` | binary keyboard set | `don`t` → `don’t` |
| hyphen `-` | en/em dash – — | thin-vs-longer stroke | `10-12 years` → `10–12 years` |

The moment of recognition: when reading your transcript, if a word *looks*
almost-write, run that 5-second shape-substitution check. Nine times out of
ten that's an OCR miss, not a typo.

## Confusion-near-hits worth double-checking (words these substitutions can co-conspire to produce)

`modern` ↔ `modeIn` — `cloud` ↔ `cIoud` — `important` ↔ `import ant` (split) —
`together` ↔ `t0gether` — `burn`/`6urn` — `clay`/`dIay` (rare but real).

## The eight-line pre-save checklist

Before saving any cleaned transcript, run your eyes down it once with these in
mind (about a minute for a typical page):

```text
1. First and last lines of every "paragraph" — line-break misplacement lives here.
2. Every number and date — shapes like 0/8/O/B, 1/l, 5/6 — verify against source if it matters.
3. Every proper name (people, places, brands) — the most confident-looking errors.
4. Every dollar sign, percent, and phone number — highest impact if wrong.
5. Capital letters at odd moments (mid-word) — leftover column/heading artifacts.
6. Two-letter "words" in the middle of sentences — fragments from a bad line-break.
7. Repeated phrases (the same sentence twice) — stitching/seam artifacts from two partial scans.
8. Markdown bullets/tables where prose should be — imbalance from the formatting pass.
```

## An AI proofread prompt (with permission to flag, not fix blindly)

When you want a second set of *digital* eyes on the final text:

```text
Below is a cleaned transcript from OCR, followed by key context: it's a
(1980s letter/notebook page/receipt). Scan it as a proofreader and flag —
do not silently fix — anything that looks like a residual OCR error: shape
confusions (0/O, 1/l, rn/m, cl/d), broken words, impossible spellings,
or wrong-looking numbers. List each with line reference and your suggested
correction marked as "suggestion" only. If the text looks clean, say so.

TRANSCRIPT:
(paste here)
```

"Flag, don't fix" is the magic phrase — without it, the AI enthusiastically
rewrites stylistic quirks that were actually correct on the page.

## Accuracy protocol (when it *really* has to be right)

If the transcript's purpose is something where an error carries real cost —
you're quoting a document, recording an amount, publishing an excerpt — run
this two-tier protocol:

```text
PASS 1: AI cleanup (Chapter 3 prompts, faithful mode).
PASS 2: The 8-line checklist above, read against the source image side by side.
PASS 3: AI proofread with "flag, don't fix".
PASS 4 (precious documents only): a fresh second image upload to a
        DIFFERENT chat/tool transcribed independently, then compare the two
        transcripts — differences mark exactly the lines worth your eyeballs.
```

Four passes sounds heavy; in practice passes 2–4 take minutes and they're
only for the rare documents that matter that much. For everyday notes,
passes 1–2 are plenty.

## The 90%-there trick: incremental follow-up questions

Don't restart the whole conversation when a cleanup is 90% right. Follow-up
prompts that work great in the SAME chat (with original context present):

```text
"Keep same rules: original line breaks must be preserved exactly."

"Paragraph 3 has table-like content that got flattened — rebuild it as a
Markdown table using only the values present in the OCR."

"There's a repeated sentence around the middle. It's likely a stitching
artifact from two overlapping scans. Identify repeated sentences and keep
only the first."

"Line 7 of the transcription is 'Sandy sent the cIoud photos' — I believe
'cIoud' is 'cloud'. Apply that understanding to similar errors elsewhere."

"We flagged [unreadable] in three spots. Here's extra context: (tell it the
topic/time/place/people). Retry just those three."
```

Iterating in-place — the AI seeing its previous attempt plus your pinpointed
fixes — is dramatically faster than re-uploading from scratch.

## When *formatted* cleanup goes wrong

Occasionally a Markdown-formatting pass (Prompt 2, Chapter 3) mangles things
it shouldn't have touched. Two recovery moves:

1. "Undo the table — output that section as plain lines, exactly as the OCR
   had them."
2. "Show me the transcript with NO formatting changes at all, only the
   character corrections." (Then format manually; sometimes the table-like
   section just isn't table material.)

## habits that pay off long-term

- **Build your own growing "confusion list"** in a file (e.g.
  `ocr-fix-list.md`): every recurring error your own documents produce,
  with its correction. Within a month yours will contain a personal hotspot
  list (maybe your scanner consistently misreads your a's as o's at low
  contrast). Preempt-fixing from this list before saving new transcripts
  turns a 15-minute proofread into a 5-minute one.
- **Keep the source images next to the transcripts** (Chapter 7 wiring).
  Disputes between "what the transcript says" and "what the page says" are
  always settled by the image — which is only possible if you kept it.

---

Next: filing everything so future-you finds it with one search.

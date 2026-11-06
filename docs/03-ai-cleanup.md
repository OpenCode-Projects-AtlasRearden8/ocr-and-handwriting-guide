# Chapter 3: Clean It Up with Free AI (Copy-Paste Prompts Inside)

OCR gives you a *draft*. It's usually 90–98% right, and the last 2–10% is
exactly where the frustration lives: split words, shuffled columns, `rn`
read as `m`, line breaks landing in terrible places.

This chapter is the "make it clean" step. You'll use a **free AI chat**
(Gemini, Copilot, or ChatGPT's free tier — all fine) as your cleanup editor.
The trick that makes this work is knowing what to *ask for*, so this chapter
is mostly ready-to-steal prompts. Copy them, paste them, keep them.

## The 2-minute cleanup workflow

```text
1. Get your raw OCR text (Chapters 1–2)
2. Paste it into the AI chat with a cleanup prompt (below)
3. Read the result for 30 seconds, fix anything obvious
4. Save it as a .txt or .md file with a good name (Chapter 7 covers naming)
```

That's the entire loop. Now, the prompts.

## Prompt 1: The faithful cleanup (use this 90% of the time)

**Use when:** you want the text cleaned but *not* changed. This is your
default for notes, letters, printed pages you're archiving as text.

```text
Below is raw OCR output from a scanned document. Clean it up so it reads
naturally, fixing obvious OCR errors: wrong characters, broken words,
merged/split lines, and broken punctuation. DO NOT add, remove, reorder, or
reword any content — the meaning must stay exactly as written. Keep original
paragraph breaks. Preserve lists as lists. If anything is unreadable, mark it
[illegible]. Output only the cleaned text.

OCR TEXT:
(paste here)
```

**Why each line matters:**
- *DO NOT add/remove/reorder* — without this, AI tends to "helpfully" expand
  or summarize, which ruins a transcript.
- *Mark unreadable as [illegible]* — an honest gap beats an invented word.
- *Output only the cleaned text* — skips the chatty preamble you'd have to
  delete.

**Verify your guardrails worked:** skim the result against the original. If
it changed more than character-level fixes, re-run with "Be more conservative;
do not restructure anything."

## Prompt 2: Faithful cleanup + formatting (for messy layouts)

**Use when:** the text is okay-ish but the *shape* is mangled — headings
buried mid-paragraph, lists flattened, tables turned to soup.

```text
Here is raw OCR from a document. Clean the text exactly like a proofreader:
fix OCR errors only; do not change, add, or reorder content. Additionally,
format it in Markdown: use ## for obvious section headings (infer from text
like ALL CAPS lines or numbered sections), convert list-like lines to bullet
lists, and if the text clearly contains a table, rebuild it as a Markdown
table using the original values only. Mark anything unreadable [illegible].

OCR TEXT:
(paste here)
```

**Extra line for tables specifically** (when a real table got mangled):

```text
The following OCR is from a table. Reconstruct the table preserving every
value. If a cell is unreadable, use [?]. Do not invent values. Column
headers appear to be: (tell it what you can see).
```

## Prompt 3: Receipts → tidy data

**Use when:** you have OCR'd receipts and want a usable expense list. This
one is a time-saver you'll use weekly. (Full receipts workflow in Chapter 4.)

```text
Below are OCR results from several receipts. For each receipt, extract:
Date | Merchant | Items (brief) | Total | Tax | Payment method (if shown).
Output as a single Markdown table, one row per receipt, plus a TOTAL row at
the bottom summing the totals. Use 0.00 placeholder for unreadable numbers
and note them. Do not guess or round.

RECEIPT OCR:
(paste here)
```

## Prompt 4: Handwriting transcription

**Use when:** working with handwritten text (deep dive in Chapter 5).

```text
Transcribe the handwriting in this image. Keep the person's own spelling,
punctuation, and line breaks as close as possible — do not "correct" them.
If a word is truly unreadable, write [unreadable]. Do not summarize or
reorganize. Output only the transcription.
```

The "don't correct them" line matters more than you'd think: AI loves
fixing spelling, but if this is *your* journal or a *grandparent's* letter,
the spelling *is* the artifact.

## Prompt 5: Summarize or index a long transcript

**Use when:** the transcription is fine but too long to skim (meeting notes,
a long letter, class lecture).

```text
Below is a cleaned transcription. Create: (1) a 5-bullet summary of the main
points; (2) a list of any dates, names, or amounts mentioned; (3) three
good search keywords someone might use to find this document later.

TRANSCRIPT:
(paste here)
```

That little keyword list becomes gold in Chapter 7 — it's your future search
fuel.

## Common cleanup mistakes (so you don't make them)

1. **Asking for cleanup *without* the "do not change content" line**, then
   getting a rewritten version you didn't want. Fix: always include the
   faithful-language.
2. **Uploading sensitive paper** to a free chat. Fix: sensitive → on-device
   OCR only, or AI on the *text* (not image) after stripping identifiers.
3. **Trusting numbers.** AI and OCR both misread digits exuberantly. If a
   receipt says $18.75, glance at the image. Digits get a "trust but
   visually verify" rule; words you can usually catch by ear when reading.
4. **One prompt, no follow-up.** If output is 80% there, just say: "Same
   rules, but keep original line breaks exactly." Iterating in the same chat
   where it can see the previous attempt is the whole magic.

## Which free AI chat should I use?

Any of them, truly. Free tiers of Gemini, Copilot, and ChatGPT all handle
image + text happily. Practical differences for *this* work:

- **Gemini / Google ecosystem** — plays nicest with Drive; if you already OCR
  into Google Docs, staying in-family is smooth.
- **Copilot / Microsoft ecosystem** — same story if you live in OneNote/Word.
- **ChatGPT free tier** — strong handwriting readings in our experience, but
  free-tier image limits change often.

Browse on the day and use whichever isn't nagging you about a rate limit.
None of this guide depends on a specific chat.

## What AI is *bad* at (so you double-check)

- **Exact numbers and dollar amounts** — verify against the image.
- **Dates** — `5/6` is May 6 or June 5 depending on country and context;
  confirm from surrounding text.
- **Names** — an unusual name (`Kaelberer`) can become generic (`Keller`);
  verify names against the original.
- **Blank-filling** — AI will sometimes "read" what plausibly *would* be
  there. If a passage seems suspiciously fluent but the source was rough,
  re-check that passage. The `[illegible]` instruction helps, but stay alert.

---

You now own the full pipeline: photo → OCR → AI cleanup. Next, we put it to
work on the most satisfying target: those shoeboxes of receipts.

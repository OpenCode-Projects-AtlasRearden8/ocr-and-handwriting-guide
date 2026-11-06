# Chapter 4: Receipts Without the Shoebox

Receipts are tiny, curly, fade-prone, and amazingly easy to lose — and they
matter for budgets, returns, warranties, and taxes. (If you run a small
business and your receipts feed bookkeeping, the full tax-and-bookkeeping
workflows live in the *Small-Business Bookkeeping* guide; here we focus on
the **capture and OCR** half.)

> **A note before we start:** this chapter is education about organizing
> your own records. It is not tax or accounting advice, and we won't tell you
> how long to keep receipts or whether they're deductible — retention and
> deduction rules vary by country, situation, and year. Ask a qualified
> professional about those. What we *can* do is make sure that when you *do*
> need a receipt from March, you can find it in ten seconds.

## The two jobs of receipt digitizing

1. **Capture** — get the receipt into your system the day you get it.
2. **Extract** — turn the pile of images into searchable data (that's where
   OCR + AI from Chapters 1–3 do the heavy lifting).

Most people fail at #1 and blame #2. Capture-anytime beats extract-perfectly.

## Job 1: Capture (the 15-second habit)

The whole trick: **photograph the receipt before it leaves your hand.** Not
tonight. Not "the car." Standing at the register.

**The no-setup method (everyone, today):**

1. Open your phone camera.
2. Photo of the receipt flat on the counter (or held flat with both ends
   visible — counter is better).
3. Later, the photos sit in your camera roll with everything else — which
   works, but buries them.

**The slightly-better method (5 minutes to set up once):**

- **iPhone:** make a dedicated note called "Receipts 2026" (or an album in
  Photos called "Receipts"). Use Notes' *Scan Documents* straight into that
  note. One note per month if it gets long.
- **Android:** Google Drive → **+** → *Scan* saves to your Drive (make a
  "Receipts" folder — it asks where). Or use Lens' *Copy text* if you need
  the number *right now*.

The difference between these two methods is enormous three months later: a
single tidy folder in chronological order beats 400 photos interleaved with
pictures of your lunch.

**Fading ink alert:** thermal receipt ink fades in months, faster in heat and
sunlight. A photo taken now preserves text that may be unreadable by summer.
If it's an important receipt (big purchase, warranty item), photograph it
*the same day*. This is honestly the single most valuable habit in this
chapter.

## Job 2: Extract (turn images into a searchable list)

Batch it, don't trickle it. Once a week or month (calendar reminder!), dump a
stack of receipt photos into OCR (Chapter 2, Situation 3: Google Docs for
batches works great) and run **Prompt 3 from Chapter 3**:

```text
Below are OCR results from several receipts. For each receipt, extract:
Date | Merchant | Items (brief) | Total | Tax | Payment method (if shown).
Output as a single Markdown table, one row per receipt, plus a TOTAL row.
Use 0.00 placeholders for unreadable numbers and note them. Do not guess.

RECEIPT OCR:
(paste here)
```

You'll get a tidy table like:

```text
| Date       | Merchant     | Items              | Total | Tax  | Pay     |
|------------|--------------|--------------------|-------|------|---------|
| 2026-03-02 | Cedar Hardware | screws, washers  | 12.48 | 0.98 | Visa-****  |
| 2026-03-04 | Book Nook    | paperback          | 18.99 | 1.32 | cash      |
| TOTAL      |              |                    | 31.47 | …    |           |
```

(Yes — AI misreads numbers sometimes. The "do not guess" instruction helps,
but **verify totals against the images**; a wrong digit in a total is the
classic failure.)

Save that table as a file like `receipts-2026-03.md`. Now your March
expenses are *text*: searchable, sortable, pasteable into any spreadsheet or
budgeting tool. Ten seconds of setup beats an afternoon of squinting at
curling paper.

## Storage folder structure that stays clean

Keep it boring and it'll keep working:

```text
Receipts/
  2026/
    2026-01.md        (the extracted table for January)
    2026-02.md
    images/
      2026-01-scan-01.jpg
      2026-01-scan-02.jpg
```

- One `.md` (or `.txt`/`.csv`) table per month, images alongside in `images/`.
- Files named `YYYY-MM` sort chronologically forever.
- If a receipt is tied to something important (warranty, big purchase), add
  the item name to the *filename* of the image, e.g.
  `2026-03-02-cedar-hardware-blender.jpg`. Filenames are search's best
  friend (more in Chapter 7).

## Special cases

**Long receipts** — see Chapter 1 (unroll first; two overlapping photos if
needed).

**Faded/ghost prints** — try the exposure-down trick from Chapter 1; if the
text is partially gone, have the AI fill gaps *only* when it labels its
guesses (`[guess]`), and verify anything that matters. Sometimes the honest
answer is a partially unreadable receipt (record what's readable).

**eReceipts (email receipts)** — these are already text! Drag into your
month's folder, or copy the key line into the table. No OCR needed — but do
save them; email accounts get locked mid-transition and "it's in my email" is
not a backup.

**Returns and warranties** — the extracted table helps you *find* it; the
photo helps you *prove* it. Keep both together. (There's a separate
*Paperwork Organizer* guide for the full warranty/life-admin system.)

## Time it actually takes

Once the habit clicks: ~15 seconds per receipt at the register, ~10 minutes
per month of batch extraction. That's the entire cost of never digging
through a shoebox again.

---

Next chapter: handwriting, the hardest and most satisfying OCR frontier.

# Chapter 9: The Cheat Sheet (Everything in Half a Page)

The whole system, condensed. Save this to your phone or print it — it's the
part you'll actually reach for.

## THE PHOTO RULES (before OCR exists)

```text
1. PAPER FLAT on a table; phone directly above, parallel.
2. WHOLE PAGE in frame + margin; small paper → get closer.
3. WINDOW LIGHT from the SIDE; no flash; watch hand/phone shadows.
4. TAP TO FOCUS on the text; steady; exhale; shoot.
5. RECEIPTS: uncurl first (reverse-roll). Too long? Two overlapping shots.
```

## THE TOOL PICK (3 seconds)

```text
Everyday text, in my hand......  iPhone Live Text / Android Lens
Keeping batches of documents... Notes "Scan Documents" / Drive Scan
On my computer................. Snipping/PowerToys (Win), Live Text (Mac),
                                Google Docs OCR (cloud), Tesseract (local)
Sensitive paper................ on-device tools ONLY
Handwriting / messy layout..... free AI chat + Prompt 4 (below)
```

## THE PROMPTS (copy, paste, keep)

**Faithful cleanup:**
```text
Below is raw OCR output. Clean it, fixing obvious OCR errors only.
DO NOT add, remove, reorder, or reword content. Keep paragraph breaks.
Mark unreadable text [illegible]. Output only the cleaned text.
```

**Handwriting transcription:**
```text
Transcribe the handwriting. Keep the writer's own spelling and line
breaks — do not correct them. Unreadable = [unreadable]. Do not
summarize. Output only the transcription.
```

**Receipts to table:** *(Chapter 3, Prompt 3 — Date | Merchant | Items |
Total | Tax | Pay.)*

**Second-pass proofread (flag, don't fix):** *(Chapter 6 prompt.)*

## THE 8-LINE PROOFREAD CHECKLIST

```text
1 First & last lines of each paragraph    5 Mid-word CAPITALS
2 Every number and date                   6 Two-letter 'words' mid-sentence
3 Every proper name                       7 Duplicated sentences (stitch seams)
4 Every $, %, phone number                8 Markdown where prose should be
```

## THE FILING RULES

```text
One root:  Documents/Scans/YYYY/
Name:      date-first + who-what → 2026-04-12-aunt-june-letter.md
Header:    4 lines — subject / tags / source / transcribed date
Search:    filenames first; then full-text; grep -ril "term" for the win
Backup:    two copies, one of them somewhere else
Upkeep:    weekly 10 min (capture + rename); yearly 30 min (zip + backup)
```

## THE TROUBLESHOOTING MANTRA

```text
Gibberish?     → language setting, contrast, or not-text-at-all / swap tools
Wrong order?   → columns. Crop per column; or AI-vision table prompt
Missing lines? → reshoot: flatter, better light, whole block
Numbers wrong? → verify against image; retype the ones that matter
AI showed off? → "Output ONLY the transcription": re-send faithful prompt
Stuck?         → fresh chat + reshot photo + smaller crop: the 5-min reset
```

## THE PIPELINE (one line, commit to memory)

```text
Paper → flat/side-lit photo → OCR (right tool for the input) →
AI cleanup (faithful prompt) → 8-line check → good filename + 4-line header
→ one Scans root → search finds it forever → two copies, one elsewhere
```

---

That's the whole handbook in one page. If this guide helped, the natural
next steps are the companion guides: the *PDF Everyday Handbook* (working
with PDFs day-to-day), the *Photo Digitizing Guide* (archival photos), and
the *Paperwork Organizer* (the life-admin filing system that these scanned
files can plug into).

*Asdale Dynamics, LLC — plain-English AI education, like a friend would
explain it. Education only; not tax, legal, or medical advice.*

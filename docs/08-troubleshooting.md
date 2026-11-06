# Chapter 8: Troubleshooting — When OCR Betrays You

Everything breaks eventually, and OCR breaks in the same handful of ways
every time. This is the ER intake table: find your symptom in the left
column, apply the first fix that sounds doable, work down the list. Five
minutes of targeted fixes solves more than five hours of re-uploading the
same broken image and hoping.

## The master symptom table

| Symptom | Most likely cause | Fixes, in order |
|---|---|---|
| Output is gibberish / random symbols | Wrong language setting, or image isn't really text (art/photo), or terrible contrast | 1. Check the tool's language setting. 2. Better light, flatter paper, fill the frame (Ch. 1). 3. Try a different tool (classic OCR ↔ AI vision swap). |
| Everything readable but words scrambled in the wrong order | Multi-column layout or a table confuse the reader | Crop to *one column at a time* and OCR separately; or skip classic OCR — use AI vision with the table prompt (Ch. 3, Prompt 2). |
| Missing chunks of text (lines vanish) | Shadow band across page, page curve, or text outside the frame, or very low resolution | 1. Reshoot with even side-light, whole block in frame. 2. Crop tighter + higher contrast. 3. Two overlapping shots, stitch manually. |
| Some characters fine, some systematically wrong | Consistent confusions (0/O, 1/l, rn/m, cl/d) | Consult the Ch. 6 table; run the 8-line checklist; use the AI proofread prompt with "flag, don't fix". |
| Numbers are consistently wrong | Digits are the hardest prey | Verify each number against the image; where it matters, retype digits manually. AI "do not guess" prompt helps but eyeballs win. |
| Handwriting output is nonsense | Classic OCR on cursive | Use a free AI vision model instead (Ch. 5 ranking), with Prompt 4; crop to paragraphs; add context ("this is a 1990s family journal"). |
| Long receipt bottom half missing | Receipt curled out of frame or shadow | Unroll (reverse-curl), shoot two overlapping halves, OCR separately (Ch. 1 & 4). |
| Faded thermal receipt text won't read | Ink fade + low contrast | 1. Exposure-down/contrast-up in an editor. 2. Try scanning on both white and dark backgrounds. 3. Ask AI to reconstruct with `[guess]` marks only. 4. Accept partial: record what's readable. |
| AI chat outputs a summary instead of a transcript | Missing faithful-language in prompt | Re-send with "Output ONLY the transcription, no summary; keep exact wording" (Ch. 3 Prompt 4). |
| Text output has weird boxes/garbage chars (�, mojibake) | Character-encoding mismatch on save/open | Save/open as UTF-8 (most editors: File → Save with encoding → UTF-8). |
| Two identical overlapping paragraphs | Stitching artifact from overlapped shots | Ask AI: "Keep only the first occurrence of repeated sentences" (Ch. 6). |
| Whole file won't open in your editor | Wrong extension or binary | Check extension; if it's .docx or .pdf when you wanted text, re-extract (Ch. 2 tools). |

## The generic five-minute reset (works more often than it should)

When nothing above obviously fits, this sequence resets almost any OCR
session to working order:

```text
1. Close the tool/chat; reopen fresh (clears stuck context).
2. Reshot the image: flat, side-lit, whole frame, tap-to-focus (Ch. 1).
3. Different tool (if classic OCR failed → try AI vision; if AI failed →
   try phone on-device Live Text/Lens).
4. Smaller crop: feed one paragraph, not the page.
5. Re-add the faithful prompt, word for word.
```

Between steps 2 and 5, you've changed every variable that *can* matter. One
of them will be the culprit.

## 'It works for everything except this one page'

That one page is probably: glossy (menu), thermal (receipt), handwritten in
a system only the author knows, or the ink/paper has aged oddly. That's not
a bug — it's the hard end of the difficulty curve. Options:

- **Manual rescue** — retype the important parts by hand. For one precious
  page, ten minutes of typing beats an hour of failed automation.
- **Crowd the frame** — physically closer camera + tighter crops per line;
  resolution-per-letter is usually the missing ingredient.
- **Time-travel test** — take the photo at a different hour: daylight angle
  changes contrast dramatically; morning window light has saved many
  'unreadable' pages.

## When the AI chat hits its image-upload limit (free tiers do this)

Rotate tools: Gemini → Copilot → ChatGPT (all free tiers accept images).
Or wait for the limit to reset (usually hourly/daily). Or use the phone
on-device tools for that session. Batch limits are the main reason
not to *depend* on one specific chat tool.

## Prevention > cure (what the pros actually do)

The chapters you've read front-load the prevention; here's the compressed
version of *why*:

```text
- Shoot flat, side-lit, tap-to-focus   → prevents 70% of all failures
- Uncurl receipts before shooting      → receipt failures mostly vanish
- Use AI vision for handwriting/columns → right tool for the input type
- Faithful-prompt with [illegible]     → honest gaps, no invented text
- Keep source images with transcripts  → every future dispute gets settled
```

Your `ocr-fix-list.md` from Chapter 6 grows more valuable every month:
as it learns *your* paper's quirks, proofreading stops being hunting and
starts being checking.

## When to stop troubleshooting and start over

The counter-intuitive truth: ~80% of OCR failures are fixed faster by
re-shooting the photo than by any amount of cleverness afterward. If two fix
attempts fail and the source image was taken in a hurry — just take a better
photo. The photo is the root of the pipeline; fixing downstream of a bad
root is wasted effort.

---

One chapter left: the pocket cheat sheet. Print it or save it to your phone
— it's everything above in half a page.

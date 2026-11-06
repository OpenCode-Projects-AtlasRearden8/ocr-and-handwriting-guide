# Chapter 1: Scan Like a Pro (It's All About Angle and Light)

Here's the secret nobody tells beginners: **the quality of your OCR is 80%
decided before any software ever gets involved.** The five seconds you spend
setting up the shot save you five minutes of cleanup later. This chapter
teaches you to take photos that computers can read perfectly on the first
try.

## The three enemies of OCR

OCR fails for exactly three reasons, and every tip below exists to defeat one
of them:

1. **Perspective skew** — you shot the page from an angle, so rectangular
   text looks like a trapezoid. Letters get stretched and the OCR engine
   guesses wrong.
2. **Uneven light** — a shadow from your hand, a glare hotspot from a lamp,
   or one bright edge and one dim edge. The engine confuses dark shadows with
   dark ink.
3. **Blur** — camera moved, page moved, or focus locked onto the wrong thing.

Fix those three and even mediocre OCR software performs well. Ignore them and
even the best AI will output gibberish.

## The 10-second setup that never fails

**Angle: shoot straight down, dead-on.**

- Hold the phone **parallel to the paper**, like you're photographing the
  paper's face, not its horizon. Aim for the camera lens being directly above
  the center of the page.
- When in doubt, get the paper **flat** — lay it on a table, not held up in
  your hand. Curved pages (book spines, crumpled receipts) are where OCR goes
  to die.
- If you must photograph a page in a binder or book, press it flat and accept
  that the curve near the spine will be the weakest part. Photograph the page
  closest to flat.

**Light: window daylight from the side.**

- Daylight from a window is the best free light source on Earth. Position the
  paper so the window is *to the side* of it, not behind you and not behind
  the paper (that causes glare straight into the lens or shadows from the
  phone itself).
- **No flash.** Your phone's flash will bounce off glossy paper, thermal
  receipt paper, and plastic sleeves, creating a white hotspot that erases
  text. If the room is dim, take the paper to the window instead.
- Watch for your own shadow. Phone held up = phone shadow on the page. If you
  see it, shift the paper, not your grip.

**Steadiness: two tricks.**

- Rest your elbows or the edge of your hands on the table while shooting.
- Tap the screen on a piece of *text* to lock focus and exposure — most phone
  cameras will then sharpen on that text and stop hunting around.

## The pre-shot checklist

Make this muscle memory (it takes three seconds once you've done it a few
times):

```text
[ ] Paper is flat on a surface
[ ] Phone is directly above, parallel to the paper
[ ] Whole page is in the frame, with a sliver of margin around it
[ ] Window or room light is beside the setup, light falling evenly
[ ] No shadows of hands or phone on the page
[ ] Tapped to focus on the text, then exhaled and tapped the shutter
```

## Special cases (paper that doesn't cooperate)

### Long, curled thermal receipts

Receipts are the classic villain: printed on curly paper with fading ink. The
fix:

1. **Uncurl before shooting.** Roll the receipt the *opposite* direction of
   its curl for a few seconds, or lay it under a heavy book for a minute.
2. Tape or hold the ends with fingers *outside the frame*.
3. Shoot straight down. If the receipt is too long for one frame, cut the
   photo into two overlapping halves (overlap by a full line of text so
   nothing lands in the gap) and OCR each half separately.

If a receipt's ink has faded to ghost-gray, try photographing it with
**contrast boosted** in your camera app (drag the exposure slider *down* — it
sounds backwards, but darkening faintly printed thermal paper often makes the
text pops). If that fails, see Chapter 8's "faded ink" section.

### Book pages and bound documents

The curve near the spine kills OCR accuracy. Press the book as flat as it
will gladly go — *never crank a bound book flat enough to damage the spine* —
and accept lower accuracy there. OCR the flatter 80% and retype the few words
near the spine by hand if you need them.

### Wrinkled, folded, or sticky-note paper

Flatten what you can. A very slightly wrinkled page photographs fine if light
is even (shadows in wrinkles are the actual problem, not the wrinkles). For
sticky notes, peel carefully and flatten on the table. Tiny notes benefit
from getting *closer* — fill the frame with the note.

### Whiteboards and chalkboards

These photograph great if you do two things: turn off any lights that cause
glare streaks on the glossy surface, and use your camera's HDR mode if it has
one. Marker text on a flat whiteboard is some of the easiest OCR out there.

## Should I use the phone's built-in scanner instead of a plain photo?

Modern phones have genuinely excellent built-in document modes — they
automatically find the page edges, correct the perspective, boost contrast,
and de-shadow. Use them whenever available:

- **iPhone:** the Notes app → new note → camera icon → *Scan Documents*. It
  produces a cleaned, flattened, black-and-white-ready scan, and the text in
  it is already searchable (you can copy it). Long-press the scan to copy its
  text.
- **Android:** the Google Drive app → **+** → *Scan*, or the Google Lens
  camera mode (point at text, tap *Copy text*). Pixel phones also have this
  right inside the Camera app's *Document* mode.

These built-in modes handle flattening and contrast *for* you, which is the
same advice as above, automated. A plain photo works too — the built-in
scanner just skips half your cleanup.

**One caution:** the *Scan Documents* tools sometimes ship pages off to cloud
services (that's how they do their magic). For anything sensitive —IDs,
medical paperwork, bank statements — prefer plain, in-app photos you keep
local, or use OCR that runs on-device (Chapter 2's table marks which tools
process where). You're in charge of where your paper's data travels.

## A word about resolution

You don't need to obsess, but two quick rules:

- **Small text = more pixels.** Fill the frame with the document. If the
  paper is a full page, shoot it full-frame; don't stand back and photograph
  the whole desk.
- **Jpg/heic from your phone is plenty.** Don't bother with special
  "document" apps promising 1200 dpi scans; your phone's normal camera at
  normal settings beats most flatbed scanners for OCR purposes.

## Quick recap

1. Flat paper, phone directly above, parallel.
2. Window light from the side, no flash, no shadows.
3. Tap to focus on the text, steady hands, shoot.
4. Prefer built-in scanner modes for everyday paper; go plain and local for
   sensitive stuff.
5. Uncurl receipts, press books *gently*, fill the frame.

You're now producing scans a computer can read on the first try. Next
chapter: which free OCR tool to actually feed them to.

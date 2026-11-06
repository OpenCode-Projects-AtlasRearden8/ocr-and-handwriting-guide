# Chapter 2: The Best Free OCR Tools (and When to Use Each)

You don't need to buy anything. Between your phone, a browser tab, and one
small free program you can install in five minutes, you have access to OCR
that's better than what businesses paid real money for fifteen years ago.

This chapter is a field guide: what each tool is good at, where it runs, and
how to use it in under a minute.

## The big picture: two kinds of OCR

**On-device OCR** — the recognition happens inside your phone or computer.
Nothing is uploaded. Fast, private, great for sensitive paper.

**Cloud OCR** — your image is sent to a server (often a big AI model) that
reads it and returns text. Often more accurate on hard text, but your document
leaves your device. Fine for restaurant menus and magazine pages; think twice
for anything with account numbers or personal identifiers.

You'll use both. The skill is knowing which situation calls for which.

## The tools, ranked by situation

### Situation 1: "I need text out of this, right now, in my hand"

**Google Lens** (Android: built into the camera or the Google app; iPhone:
inside the Google app) — point at any visible text, tap *Search* or the text
frame, then *Copy text* or *Copy to computer* (that last one sends the text to
any nearby Chrome browser — genuinely wonderful). Fast, usually on-device,
free.

**iPhone Live Text** — built into iOS. Open any photo with text, press and
hold the text, it lifts right off. Works on signs, pages, receipts. On-device,
free, zero setup. This solves *most* people's *most* OCR needs all by itself.

**When to use:** restaurant menus, posters, a paragraph from a book, wifi
passwords on a router label, quick line-of-text grabs.

### Situation 2: "I have a photo/screenshot on my computer"

- **Windows:** press `Win + Shift + T` (Snipping Tool text extraction) —
  after snipping, the toolbar offers *Text actions* to copy all text. Also,
  **PowerToys Text Extractor** (`Win + Shift + T` when PowerToys is installed)
  grabs text from anywhere on screen. Both are free and on-device.
- **Mac:** macOS has Live Text system-wide — just select/copy text inside any
  image in Preview or Quick Look.
- **Any platform:** open the image in **Google Docs** (Drive → upload → right
  click → *Open with Google Docs*) and the OCR text appears above the image.
  Cloud-based, needs a Google account, handles whole multi-page documents
  beautifully.

**When to use:** screenshots, downloaded images, PDFs-that-are-actually-pictures.

### Situation 3: "I have a whole stack of photos/documents"

**Google Drive's Scan + Google Docs OCR** is the stack king: upload a batch to
Drive, select all, *Open with → Google Docs*, and you get one doc per image
with the text extracted. Cloud-based, but Google's OCR is free and very good.

**OneNote's "Copy text from picture"** (free with a Microsoft account):
insert the image into a note, right-click the picture, *Copy Text from
Picture*, paste anywhere. Cloud-assisted, handles messy real-world paper
well.

**When to use:** digitizing a folder of notes, class handouts, clippings.

### Situation 4: "I want OCR that never touches the internet"

**Tesseract** — the classic open-source OCR engine. It's a command-line tool
(AIcomplete: you type a command, it outputs a text file), and it's the engine
inside a lot of commercial tools. Free forever, runs on Windows/Mac/Linux,
100% on-device. Community tools like **OCR4Linux-style wrappers**, **gImageReader** (GUI front-end for Tesseract), or Linux's **GNOME Sushi/doc properties** integrations put friendly faces on it.

One-line example once installed (Linux/macOS after `brew install tesseract` or
`apt install tesseract-ocr`):

```text
tesseract receipt-01.jpg receipt-01-text
```

That drops `receipt-01-text.txt` next to the image. Done.

**When to use:** anything sensitive, big batch jobs you want to automate,
older/no-internet computers, or if you just like owning your tools.

### Situation 5: "Just let the AI read it"

Free AI chats — **Gemini**, **Copilot**, and **ChatGPT** all accept image
uploads on their free tiers — will happily transcribe an image of text. This
is technically AI vision, not classic OCR, and for modern printed text it's
extremely good. It also *understands* the text, so it can format, summarize,
or fix garble in the same breath (Chapter 3 is all about this).

**When to use:** messy layouts, forms with boxes and columns (where classic
OCR shuffles order), pages in more than one language, and anything you'll
clean up anyway.

**Privacy note:** this is cloud OCR (and then some) — treat free chat tiers'
uploads as "leaving the building." Use it for ordinary paper, not for IDs or
sensitive personal data.

## The cheat table

| Tool | Where it runs | Best for | Cloud or local | Skill level |
|---|---|---|---|---|
| iPhone Live Text | iOS Photos/anywhere | Instant text from any image | Local | Zero |
| Google Lens | Android/iPhone (Google app) | Instant text, send-to-computer | Mostly local | Zero |
| Notes/Drive *Scan Documents* | Phone camera apps | Multi-page tidy scans | Cloud-assisted | Zero |
| Snipping Tool / PowerToys Text Extractor (Win) | Windows on screen | Text in screenshots | Local | Easy |
| macOS Live Text | Mac system-wide | Text in images on Mac | Local | Zero |
| Google Docs OCR | Google Drive | Whole documents, stacks | Cloud | Easy |
| OneNote picture-to-text | Windows/Mac/web | Odd real-world paper | Cloud-assisted | Easy |
| Free AI chat (Gemini/Copilot/ChatGPT) | Browser/app | Messy layouts, + cleanup/formatting | Cloud | Easy |
| Tesseract (+ GUI front-ends) | Your computer | Offline, batches, automation, privacy | Local | Moderate |

*Tool menus move around; if a button has wandered since we wrote this, the
principle stands: find the tool's "read text from image" feature and feed it a
good photo (Chapter 1).*

## Choosing without agonizing

If you're overwhelmed, here's the honest recommendation for most beginners:

1. **Phone, everyday stuff:** Live Text (iPhone) or Google Lens (Android).
   Done. That's it.
2. **Documents in batches or that you want to keep:** *Scan Documents* into
   Notes (iPhone) or Drive Scan (Android), then optionally Docs OCR for
   extracted text.
3. **Sensitive paper:** on-device tools only (numbers 1–3, or Tesseract).
4. **Hard layouts or handwriting:** free AI chat, followed by the cleanup
   workflow in Chapter 3.

That's the whole decision tree.

## Coming up

A raw OCR dump is usually readable but ragged — wrong line breaks, `0` for
`O`, columns shuffled. Chapter 3 shows how a free AI assistant polishes that
into genuinely clean text in about two minutes, using copy-paste prompts you
can steal.

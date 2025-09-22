# merge-jpgs-to-pdf

Simple, reliable script to merge `.jpg`/`.jpeg` images into a single PDF. 
Designed to be copy‑paste friendly and easy to run from the command line.

> GitHub home: https://github.com/AygunVarol/merge-jpgs-to-pdf

---

## Features
- Natural file ordering: `img1.jpg, img2.jpg, ..., img10.jpg` (no more `1, 10, 2` surprises)
- Converts images to RGB for PDF compatibility (transparency removed automatically)
- Zero config: point at a folder, get a PDF
- Pure-Python, tiny dependency footprint

## Requirements
- Python 3.8+
- Pillow (`pip install pillow`)

## Installation

Clone the repository:

```bash
git clone https://github.com/AygunVarol/merge-jpgs-to-pdf.git
cd merge-jpgs-to-pdf
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Or just copy the single script from `src/merge_jpgs_to_pdf.py` into your project and install Pillow.

## Usage

```bash
# Merge all JPG/JPEG files in ./scans into merged.pdf
python src/merge_jpgs_to_pdf.py ./scans merged.pdf
```

**CLI syntax**

```text
python src/merge_jpgs_to_pdf.py <folder_with_jpgs> <output.pdf>
```

- `<folder_with_jpgs>`: directory containing `.jpg`/`.jpeg` images
- `<output.pdf>`: path to write the merged PDF

**Natural ordering**  
Files are ordered by name using human‑friendly rules (e.g., `page2.jpg` comes before `page10.jpg`).  
If you need a different order, rename files (e.g., prefix with `001_`, `002_`, …).

## Troubleshooting

- **No JPG files found**: make sure your files end with `.jpg` or `.jpeg` (case‑insensitive).
- **Very large image sets**: Pillow loads all images to save them into a single PDF. If you're merging thousands of pages on a low‑memory system, consider the alternative below.

```bash
pip install img2pdf
```

A companion CLI using `img2pdf` is trivial; see the commented note in the script and this repo’s Issues for tips.

## License

MIT © 2025 Aygun Varol

---

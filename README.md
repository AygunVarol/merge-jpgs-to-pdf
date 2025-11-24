# Image & PDF Merge Tools
Simple, reliable scripts to merge `.jpg/.jpeg` images and PDF files. 
Designed to be copy‑paste friendly and easy to run from the command line.

> GitHub home: https://github.com/AygunVarol/merge-jpgs-to-pdf

---

## Features

### JPG to PDF Merger
- Natural file ordering: `img1.jpg, img2.jpg, ..., img10.jpg` (no more `1, 10, 2` surprises)
- Converts images to RGB for PDF compatibility (transparency removed automatically)
- Zero config: point at a folder, get a PDF
- Pure-Python, tiny dependency footprint

### PDF Merger
- Merges multiple PDF files into a single document
- Alphabetical ordering by filename
- Progress feedback during merge
- Simple and reliable

## Requirements
- Python 3.8+
- Pillow (`pip install pillow`)
- PyPDF2 (`pip install PyPDF2`)

## Installation
Clone the repository:
```bash
git clone https://github.com/AygunVarol/merge-jpgs-to-pdf.git
cd merge-jpgs-to-pdf
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Or just copy the scripts from the `src/` folder into your project and install the dependencies.

## Usage

### Merge JPGs to PDF
```bash
# Merge all JPG/JPEG files in ./scans into merged.pdf
python src/merge_jpgs_to_pdf.py ./scans merged.pdf
```

**CLI syntax**
```text
python src/merge_jpgs_to_pdf.py <folder_with_jpgs> <output.pdf>
```
- `<folder_with_jpgs>`: directory containing `.jpg/.jpeg` images
- `<output.pdf>`: path to write the merged PDF

### Merge PDFs
```bash
# Merge all PDF files in ./src folder into merged_output.pdf
python src/merge_pdfs.py
```

**CLI syntax**
```text
python src/merge_pdfs.py [source_folder] [output.pdf]
```
- `[source_folder]`: directory containing PDF files (default: `src`)
- `[output.pdf]`: path to write the merged PDF (default: `merged_output.pdf`)

**Natural ordering**  
Files are ordered by name using human‑friendly rules (e.g., `page2.jpg` comes before `page10.jpg`, `doc2.pdf` comes before `doc10.pdf`).  
If you need a different order, rename files (e.g., prefix with `001_`, `002_`, …).

## Troubleshooting
- **No JPG files found**: make sure your files end with `.jpg` or `.jpeg` (case‑insensitive).
- **No PDF files found**: ensure your files have the `.pdf` extension and are in the correct folder.
- **Folder does not exist**: verify the folder path is correct.

## License
MIT © 2025 Aygün Varol

---

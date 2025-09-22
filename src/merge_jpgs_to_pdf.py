# merge_jpgs_to_pdf.py
# Usage:
#   python src/merge_jpgs_to_pdf.py <folder_with_jpgs> <output.pdf>
#
# Requires:
#   pip install pillow
#
# Notes:
# - Images are sorted in "natural" order, e.g., img2.jpg comes before img10.jpg.
# - All images are converted to RGB to ensure PDF compatibility.
# - For very large batches or low-memory environments, consider using "img2pdf".

from pathlib import Path
from PIL import Image
import re
import sys


def natural_key(p: Path):
    """
    Key function for natural sort: splits name into text and integer chunks.
    Example: "page12" -> ["page", 12]
    """
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', p.stem)]


def find_jpgs(folder: Path):
    """Return a naturally sorted list of JPG/JPEG files in the given folder."""
    return sorted(
        [p for p in folder.iterdir() if p.suffix.lower() in (".jpg", ".jpeg")],
        key=natural_key
    )


def jpgs_to_pdf(img_dir: Path, out_pdf: Path):
    """Merge all JPG/JPEG files in img_dir into a single PDF at out_pdf."""
    imgs = find_jpgs(img_dir)
    if not imgs:
        raise SystemExit(f"No JPG files found in: {img_dir}")

    # Open & convert each image to RGB (PDF does not support alpha)
    pil_imgs = []
    try:
        for p in imgs:
            im = Image.open(p).convert("RGB")
            pil_imgs.append(im)

        first, rest = pil_imgs[0], pil_imgs[1:]
        first.save(out_pdf, save_all=True, append_images=rest)
    finally:
        # Make sure everything gets closed even if save() raises
        for im in pil_imgs:
            try:
                im.close()
            except Exception:
                pass


def main(argv=None):
    argv = argv or sys.argv[1:]
    if len(argv) < 2:
        print("Usage: python src/merge_jpgs_to_pdf.py <folder_with_jpgs> <output.pdf>")
        sys.exit(1)

    img_dir = Path(argv[0]).expanduser().resolve()
    out_pdf = Path(argv[1]).expanduser().resolve()

    if not img_dir.exists() or not img_dir.is_dir():
        raise SystemExit(f"Not a directory: {img_dir}")

    # Ensure parent directory for output exists
    out_pdf.parent.mkdir(parents=True, exist_ok=True)

    jpgs_to_pdf(img_dir, out_pdf)
    print(f"Wrote {out_pdf}")


if __name__ == "__main__":
    main()

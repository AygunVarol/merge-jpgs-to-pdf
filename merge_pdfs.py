import os
from pathlib import Path
from PyPDF2 import PdfMerger

def merge_pdfs_in_folder(src_folder='src', output_file='merged_output.pdf'):
    """
    Merges all PDF files in the source folder in alphabetical order.
    
    Args:
        src_folder (str): Path to the folder containing PDF files
        output_file (str): Name of the output merged PDF file
    """
    # Create Path object for the source folder
    src_path = Path(src_folder)
    
    # Check if source folder exists
    if not src_path.exists():
        print(f"Error: The folder '{src_folder}' does not exist.")
        return
    
    # Get all PDF files and sort them alphabetically
    pdf_files = sorted(src_path.glob('*.pdf'))
    
    # Check if there are any PDF files
    if not pdf_files:
        print(f"No PDF files found in '{src_folder}' folder.")
        return
    
    print(f"Found {len(pdf_files)} PDF file(s) to merge:")
    for pdf in pdf_files:
        print(f"  - {pdf.name}")
    
    # Create PdfMerger object
    merger = PdfMerger()
    
    try:
        # Add each PDF file to the merger
        for pdf_file in pdf_files:
            print(f"Adding: {pdf_file.name}")
            merger.append(str(pdf_file))
        
        # Write the merged PDF to output file
        merger.write(output_file)
        merger.close()
        
        print(f"\nSuccess! Merged PDF saved as '{output_file}'")
        
    except Exception as e:
        print(f"Error occurred while merging PDFs: {e}")
        merger.close()

if __name__ == "__main__":
    # Merge PDFs from 'src' folder
    merge_pdfs_in_folder('src', 'merged_output.pdf')
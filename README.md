# Thinsil Technologies Private Limited Assingnments
* This repository is created exclusively for the purpose of submitting assignments related to the Python Developer job offered by Thinsil Technologies Private Limited.
## PDF Processor

* PDF Processor is a Python application that allows you to perform various operations on PDF files, including merging PDFs, splitting PDFs, unlocking password-protected PDFs, extracting text from PDFs, and converting images to PDFs. This tool uses the ILovePDF API for these operations.

### 1. Prerequisites

- Python 3.x
- Required Python packages (install them using `pip`):
  - `tkinter`
  - `pylovepdf`

### 2. Getting Started

1. Clone or download this repository to your local machine.
2. Get you ilovepdf Api key in (https://developer.ilovepdf.com/)
3. Create a file named `creds.py` in the same directory and add your ILovePDF public key as follows:

   ```python
   api_key = 'your_public_key_here'
4. Run the application using Python:

> python main.py

### 3. Use the GUI to select PDF files and perform various PDF operations.

**Features:**
* Set Output Folder: Choose the destination folder for output files.
* Merge PDFs: Combine multiple PDF files into a single PDF.
* Split PDFs: Split a PDF file into multiple individual pages.
* Unlock PDF: Remove password protection from a PDF file.
* Extract Text from PDF: Extract text content from a PDF.
* Convert Images to PDF: Convert image files (JPG, PNG, TIFF) into a PDF document.


### 4. Acknowledgments
* [ILovePDF](https://developer.ilovepdf.com/)
* tkinter

Feel free to contribute, report issues, or suggest enhancements to this project.

Enjoy working with PDFs!

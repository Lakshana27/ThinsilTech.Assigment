# Import necessary libraries
from tkinter import *
from tkinter import filedialog, messagebox
from pylovepdf.ilovepdf import ILovePdf
from creds import api_key

# Initialize ILovePdf
public_key = api_key
ilovepdf = ILovePdf(public_key, verify_ssl=True)


# Define the PdfProcessorApp class
class PdfProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Processor")
        self.root.geometry("480x440")


        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=True)

        self.set_output_folder_button = Button(self.frame, text="Set Output Folder", command=set_output_folder,
                                               font=("Calibri", 15, "bold"), fg="white", bg="#FF8E13", bd=3,
                                               width=25,height=1)
        self.set_output_folder_button.pack(pady=30)


        self.combine_button = Button(self.frame, text="Merge PDFs", command=merge_pdfs,
                                    font=("Calibri", 12, "bold"), fg="white", bg="#FF8E33", bd=3,width=20)
        self.combine_button.pack(pady=10)

        self.separate_button = Button(self.frame, text="Split PDFs", command=split_pdf,
                                    font=("Calibri", 12, "bold"), fg="white", bg="#FF8E33", bd=3,width=20)
        self.separate_button.pack(pady=10)

        self.remove_password_button = Button(self.frame, text="Unlock PDF", command=unlock_pdf,
                                    font=("Calibri", 12, "bold"), fg="white", bg="#FF8E33", bd=3,width=20)
        self.remove_password_button.pack(pady=10)

        self.extract_text_button = Button(self.frame, text="Extract Text from PDF", command=extract_text_from_pdf,
                                    font=("Calibri", 12, "bold"), fg="white", bg="#FF8E33", bd=3,width=20)
        self.extract_text_button.pack(pady=10)

        self.image_to_pdf_button = Button(self.frame, text="Convert Images to PDF", command=image_to_pdf,
                                    font=("Calibri", 12, "bold"), fg="white", bg="#FF8E33", bd=3,width=20)
        self.image_to_pdf_button.pack( pady=10)

# Function to set the output folder for ILovePDF tasks
output_folder = ""

def set_output_folder():
    global output_folder
    output_folder = filedialog.askdirectory()
    if output_folder:
        messagebox.showinfo("Output Folder", f"Output folder set to {output_folder}")


# Function to merge PDFs
def merge_pdfs():
    global output_folder
    if not output_folder:
        messagebox.showerror("Error", "Please set the output folder first.")
        return

    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if len(files) > 0:
        merge_task = ilovepdf.new_task('merge')
        for file in files:
            merge_task.add_file(file)
        merge_task.set_output_folder(output_folder)
        merge_task.execute()
        merge_task.download()
        messagebox.showinfo("Merge PDFs", "PDFs merged successfully!")

# Function to split PDF
def split_pdf():
    global output_folder
    if not output_folder:
        messagebox.showerror("Error", "Please set the output folder first.")
        return

    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file:
        split_task = ilovepdf.new_task('split')
        split_task.add_file(file)
        split_task.set_output_folder(output_folder)
        split_task.execute()
        split_task.download()
        messagebox.showinfo("Split PDF", "PDF split successfully!")

# Function to unlock a PDF
def unlock_pdf():
    global output_folder
    if not output_folder:
        messagebox.showerror("Error", "Please set the output folder first.")
        return

    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file:
        unlock_task = ilovepdf.new_task('unlock')
        unlock_task.add_file(file)
        unlock_task.set_output_folder(output_folder)
        unlock_task.execute()
        unlock_task.download()
        messagebox.showinfo("Unlock PDF", "PDF unlocked successfully!")


# Function to extract text from a PDF
def extract_text_from_pdf():
    global output_folder
    if not output_folder:
        messagebox.showerror("Error", "Please set the output folder first.")
        return

    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file:
        # Initialize an ILovePdf task for text extraction
        text_extraction_task = ilovepdf.new_task('extract_text')
        text_extraction_task.add_file(file)
        text_extraction_task.set_output_folder(output_folder)
        text_extraction_task.execute()
        text_extraction_task.download()
        messagebox.showinfo("Text Extraction", "Text extracted from PDF successfully!")


# Function to convert image to PDF
def image_to_pdf():
    global output_folder
    if not output_folder:
        messagebox.showerror("Error", "Please set the output folder first.")
        return

    files = filedialog.askopenfilenames(filetypes=[("Images", "*.jpg *.png *.tiff")])
    if len(files) > 0:
        imagetopdf_task = ImageToPdf(public_key, verify_ssl=True, proxies=None)
        for file in files:
            imagetopdf_task.add_file(file)
        imagetopdf_task.margin = 0
        imagetopdf_task.pagesize = 'fit'
        imagetopdf_task.set_output_folder(output_folder)
        imagetopdf_task.execute()
        imagetopdf_task.download()
        messagebox.showinfo("Image to PDF", "Images converted to PDF successfully!")


def main():
    # Create a Tkinter window
    root = Tk()
    # Create an instance of PdfProcessorApp
    app = PdfProcessorApp(root)
    # Start the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()

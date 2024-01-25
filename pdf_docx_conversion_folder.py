import os
from pdf2docx import Converter

def convert_folder_pdfs_to_docx(folder_path):
    # Iterate through all files in the folder
    for pdf_file in os.listdir(folder_path):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, pdf_file)
            
            # Generate the corresponding DOCX file name
            docx_output = os.path.splitext(pdf_file)[0] + ".docx"
            docx_output_path = os.path.join(folder_path, docx_output)

            # Convert PDF to DOCX
            cv = Converter(pdf_path)
            cv.convert(docx_output_path, start=0, end=None)
            cv.close()

if __name__ == "__main__":
    # Input folder containing PDFs
    pdf_folder = r"C:\Users\Documents\PDFs"

    # Convert all PDFs in the folder to DOCX
    convert_folder_pdfs_to_docx(pdf_folder)

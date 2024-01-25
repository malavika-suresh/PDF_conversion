from pdf2docx import Converter

def pdf_to_docx(pdf_path, docx_output):
    cv = Converter(pdf_path)
    cv.convert(docx_output, start=0, end=None)
    cv.close()

if __name__ == "__main__":
    pdf_file = r"C:\Users\Documents\file.pdf"
    docx_output = "file.docx"
    pdf_to_docx(pdf_file, docx_output)

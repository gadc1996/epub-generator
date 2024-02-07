import os
import subprocess
from pdf2docx import Converter


class PDFConverter:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def convert_pdf_to_docx(self, pdf_file, docx_file):
        cv = Converter(pdf_file)
        cv.convert(docx_file, start=0, end=None)
        cv.close()

    def convert_docx_to_epub(self, docx_file, epub_file, title):
        subprocess.run(["pandoc", docx_file, "-o", epub_file, "-M", f"title={title}"])

    def cleanup(self, file):
        if os.path.exists(file):
            os.remove(file)

    def convert_all_pdfs(self):
        files = os.listdir(self.input_dir)
        for f in files:
            if f.endswith(".pdf"):
                pdf_file = os.path.join(self.input_dir, f)
                docx_file = os.path.join(self.output_dir, f.replace(".pdf", ".docx"))
                self.convert_pdf_to_docx(pdf_file, docx_file)
                epub_file = os.path.join(self.output_dir, f.replace(".pdf", ".epub"))
                title = os.path.splitext(f)[
                    0
                ]  # Use the filename without extension as the title
                self.convert_docx_to_epub(docx_file, epub_file, title)
                self.cleanup(docx_file)

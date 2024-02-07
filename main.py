import os
from src.pdf_converter import PDFConverter


def main():
    input_dir = os.path.join(os.path.dirname(__file__), "src", "files")
    output_dir = os.path.join(os.path.dirname(__file__), "dist")
    converter = PDFConverter(input_dir, output_dir)
    converter.convert_all_pdfs()


if __name__ == "__main__":
    main()

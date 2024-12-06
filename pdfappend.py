###############################################################################
# Released under the MIT License
# See LICENSE file in the repository root for details.
###############################################################################
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 3 12:04:40 2024

__author__ = "Johnathan SJ"
__license__ = "MIT"
__email__ = "diversity@johnangie.org"
__status__ = "Production"
__version__ = "1.0"
"""
from PyPDF2 import PdfReader, PdfWriter

def append_pdfs(pdf1_path, pdf2_path, output_path):
    pdf_writer = PdfWriter()

    # Read the first PDF and add its pages to the writer
    pdf1_reader = PdfReader(pdf1_path)
    for page in pdf1_reader.pages:
        pdf_writer.add_page(page)

    # Read the second PDF and add its pages to the writer
    pdf2_reader = PdfReader(pdf2_path)
    for page in pdf2_reader.pages:
        pdf_writer.add_page(page)

    # Write the combined PDF to the output file
    with open(output_path, 'wb') as out_file:
        pdf_writer.write(out_file)

# Your specific file paths
pdf1_path = r'Path/to/first/pdf'
pdf2_path = r'path/to/second/pdf'
output_path = r'path/to/save/path'

append_pdfs(pdf1_path, pdf2_path, output_path)

print("PDFs have been successfully merged into Combined_Document.pdf")



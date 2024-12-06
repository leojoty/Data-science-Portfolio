# PDF Append Utility

**Python Script for Combining Multiple PDFs**

This repository contains a simple yet efficient Python script for appending multiple PDF files into a single, consolidated document. The utility leverages the powerful `PyPDF2` library to read and write PDF files.

---

## **Features**

- **Combine Multiple PDFs**: Merges two PDF documents into a single file seamlessly.
- **Preserve Content Quality**: Ensures that the original quality and formatting of the PDF files remain intact.
- **Ease of Use**: Designed with straightforward file path inputs for quick execution.
- **Customizable**: Can be extended to handle multiple PDFs or additional functionalities, such as adding metadata.

---

## **How It Works**

The script reads pages from two PDF files, combines them, and writes the output to a specified file location.

### **Script Overview**
```python
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
```

---

## **Setup and Installation**

### **Prerequisites**
- Python 3.7 or later
- `PyPDF2` library

### **Install Dependencies**
Run the following command to install `PyPDF2`:
```bash
pip install PyPDF2
```

---

## **Usage**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/leojoty/PDF-Append.git
   cd PDF-Append
   ```

2. **Set File Paths**:
   Update the following variables in the script with your file paths:
   - `pdf1_path`: Path to the first PDF file.
   - `pdf2_path`: Path to the second PDF file.
   - `output_path`: Path where the combined PDF will be saved.

3. **Run the Script**:
   Execute the script:
   ```bash
   python append_pdfs.py
   ```

4. **Output**:
   The script will generate a new PDF file at the specified `output_path`.

---

## **Future Enhancements**

This utility is designed to be modular and extensible. Future iterations may include:
- **Support for Multiple PDFs**: Allow appending more than two PDF files.
- **Metadata and Encryption**: Add support for editing metadata and applying password protection.
- **Command-Line Interface (CLI)**: Provide a CLI for easier use without editing the script.

---

## **Contributing**

Contributions are welcome! If you have ideas for improvement or additional features, please:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

---

## **Contact**

For questions, suggestions, or collaboration opportunities:
- **Email**: [john.sj@johnangie.org](mailto:john.sj@johnangie.org)
- **GitHub**: [leojoty](https://github.com/leojoty)

---

## **Acknowledgments**

Thanks to the creators of `PyPDF2` for providing an excellent library for PDF manipulation.
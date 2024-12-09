# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:29:45 2024

@author: gospe
"""

# test_redact.py

import sys
sys.path.append(r"C:\Users\gospe\anaconda3\envs\myenv\Lib\site-packages")
from redact import redact_pdf, redact_pptx


def test_redact_pdf():
    input_pdf = "C:/Users/gospe/Portfolio/Projects/Redact/Deloitte Cover Letter.pdf"  # Replace with your test PDF path
    output_pdf = "redacted_output.pdf"

    print("Testing PDF Redaction...")
    try:
        redact_pdf(input_pdf, output_pdf)
        if open(output_pdf, 'r'):  # Check if the file can be opened
            print("✅ PDF redaction successful!")
    except FileNotFoundError:
        print("❌ PDF redaction failed: Output file not created.")
    except Exception as e:
        print(f"❌ PDF redaction failed: {e}")

def test_redact_pptx():
    input_pptx = "C:/Users/gospe/Portfolio/Projects/Redact/Qualitative Prospectus v.2 (3).pptx"  # Replace with your test PPTX path
    output_pptx = "redacted_output.pptx"

    print("Testing PowerPoint Redaction...")
    try:
        redact_pptx(input_pptx, output_pptx)
        if open(output_pptx, 'r'):  # Check if the file can be opened
            print("✅ PowerPoint redaction successful!")
    except FileNotFoundError:
        print("❌ PowerPoint redaction failed: Output file not created.")
    except Exception as e:
        print(f"❌ PowerPoint redaction failed: {e}")

if __name__ == "__main__":
    # Test PDF Redaction
    test_redact_pdf()

    # Test PowerPoint Redaction
    test_redact_pptx()

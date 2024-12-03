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
import re
import fitz  # PyMuPDF
import spacy

# Load NLP model for Named Entity Recognition
nlp = spacy.load("en_core_web_sm")

# File paths
input_pdf = "path/to/file"
output_pdf = "path/to/save/file"

# Sensitive entity types to redact
entity_types_to_redact = {"PERSON", "ORG", "DATE", "URL"}

# Helper function to find sensitive terms using NLP
def find_sensitive_terms(text):
    doc = nlp(text)
    sensitive_terms = set()
    for ent in doc.ents:
        if ent.label_ in entity_types_to_redact:
            sensitive_terms.add(ent.text)
    return sensitive_terms

# Open the PDF
doc = fitz.open(input_pdf)

# Iterate through the pages
for page_number in range(len(doc)):
    page = doc[page_number]
    text = page.get_text()

    # Find sensitive terms dynamically
    sensitive_terms = find_sensitive_terms(text)

    # Add URL pattern manually
    url_pattern = re.compile(r"https?:\/\/[^\s]+")
    sensitive_terms.update(url_pattern.findall(text))

    # Apply redactions
    for term in sensitive_terms:
        areas = page.search_for(term)
        for area in areas:
            # Use fixed black color and standard font size for replacement
            page.add_redact_annot(
                area,
                "REDACTED",
                fill=(1, 1, 1),  # White background
                text_color=(0, 0, 0),  # Black text color
                fontsize=12,  # Adjust font size as needed
            )

    # Apply the redactions for the page
    page.apply_redactions()

# Save the updated PDF
doc.save(output_pdf, garbage=4, deflate=True)
doc.close()

print(f"Redacted PDF saved as {output_pdf}")

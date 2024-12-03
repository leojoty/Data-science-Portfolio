###############################################################################
# Released under the MIT License
# See LICENSE file in the repository root for details.
###############################################################################
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 3 12:04:40 2024

__author__ = "Johnathan S.J."
__license__ = "MIT"
__email__ = "diversity@johnangie.org"
__status__ = "Production"
__version__ = "1.0"
"""


from setuptools import setup, find_packages

setup(
    name="redact",
    version="1.0.0",
    author="Johnathan Svoboda-James",
    description="A tool for redacting sensitive information from PDFs and PowerPoint files.",
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),  # Automatically finds the `__init__.py` structure
    install_requires=[
        "spacy",  # Example dependencies
        "python-pptx",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

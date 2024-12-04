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
    author="Johnathan S.J.",
    author_email="https://www.johnangie.org",  # Add your email here
    description="A tool for redacting sensitive information from PDFs and PowerPoint files.",
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/leojoty/Data-science-Portfolio/tree/redact-branch",  # Replace with the correct URL
    license="MIT",
    packages=find_packages(),  # Automatically finds Python modules
    install_requires=[
        "spacy",
        "python-pptx",
    ],
    python_requires=">=3.8",  # Ensures compatibility with Python 3.8 and above
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


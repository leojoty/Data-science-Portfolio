###############################################################################
# J-A Legacy PROPRIETARY and Not A Contract Deliverable
# Use and Disclosure Limited to U.S. Employees and only in support of AI programs
# Copyright © J-A Legacy 2019-present. Unpublished work - all rights reserved.
# Third party disclosure requires written approval.
###############################################################################
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:06:05 2024

__author__ = "Johnathan Svoboda-James"
__copyright__ = "Copyright 2024, J-A Legacy"
__license__ = "J-A Legacy Proprietary"
__maintainer__ = "Johnathan Svoboda-James"
__email__ = "Diversity@johnangie.org
__status__ = "Development"
__version__ = "1.0"
"""

import os

def print_tree(startpath, indent="  "):
    """
    Recursively prints a directory structure in a tree format.

    :param startpath: Path of the directory to print.
    :param indent: Indentation style for the tree structure.
    """
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, "").count(os.sep)
        indent_space = indent * level
        print(f"{indent_space}[{os.path.basename(root)}]")
        subindent = indent * (level + 1)
        for file in files:
            print(f"{subindent}{file}")

# Replace 'path_to_your_project' with the actual path to your project directory
project_path = 'C:/Users/gospe/Portfolio' # Example: 'C:/Users/YourName/Documents/MyProject'
print_tree(project_path)
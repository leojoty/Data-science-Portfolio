###############################################################################
# Released under the MIT License
# See LICENSE file in the repository root for details.
###############################################################################
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:57:01 2025

__author__ = "Johnathan SJ"
__license__ = "MIT"
__email__ = "diversity@johnangie.org"
__status__ = "Production"
__version__ = "1.0"
"""

import pandas as pd
import h5py
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define paths
extract_path = 'C:/Users/gospe/Portfolio/Projects/Physics_models/streamer-surface-interaction-in-an-atmospheric-pressure-dielectric-barrier-discharge-in-argon-dataset-All-2025-01-15_2045'
extracted_files = os.listdir(extract_path)

# Helper functions

def plot_histograms(df, title):
    """Plot histograms for all numeric columns in a DataFrame."""
    df.hist(bins=50, figsize=(15, 10))
    plt.suptitle(title, fontsize=16)
    plt.show()

def plot_heatmap(df, title):
    """Plot a heatmap for correlations in a DataFrame."""
    correlation = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(title)
    plt.show()

def inspect_csv(file_path):
    """Load and analyze a CSV file."""
    df = pd.read_csv(file_path)
    print(f"\nSummary for {os.path.basename(file_path)}")
    print(df.info())
    print(df.describe())

    # Plot histograms
    print(f"Histograms for {os.path.basename(file_path)}")
    plot_histograms(df, f"Histograms for {os.path.basename(file_path)}")

    # Plot heatmap
    print(f"Heatmap for {os.path.basename(file_path)}")
    plot_heatmap(df, f"Correlation Heatmap for {os.path.basename(file_path)}")

    return df

def inspect_hdf5(file_path):
    """Inspect the structure and content of an HDF5 file."""
    with h5py.File(file_path, 'r') as h5file:
        print(f"\nContents of {os.path.basename(file_path)}:")
        for key in h5file.keys():
            print(f"Dataset: {key}, Shape: {h5file[key].shape}")

# EDA Workflow
for file in extracted_files:
    file_path = os.path.join(extract_path, file)
    
    if file.endswith('.csv'):
        # Analyze CSV files
        df = inspect_csv(file_path)
    elif file.endswith('.h5'):
        # Analyze HDF5 files
        inspect_hdf5(file_path)

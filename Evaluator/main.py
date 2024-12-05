###############################################################################
# J-A Legacy PROPRIETARY and Not A Contract Deliverable
# Use and Disclosure Limited to U.S. Employees and only in support of AI programs
# Copyright © J-A Legacy 2019-present. Unpublished work - all rights reserved.
# Third party disclosure requires written approval.
###############################################################################
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:04:40 2024

__author__ = "Johnathan Svoboda-James"
__copyright__ = "Copyright 2024, J-A Legacy"
__license__ = "J-A Legacy Proprietary"
__maintainer__ = "Johnathan Svoboda-James"
__email__ = "Diversity@johnangie.org
__status__ = "Development"
__version__ = "1.0"
"""

# main.py: Load, preprocess, and save The Stack v2 dataset to Hugging Face repository

import os
from datasets import load_dataset
from transformers import GPT2Tokenizer
from huggingface_hub import create_repo
from dotenv import load_dotenv
import subprocess
import json

# Load environment variables
load_dotenv()

# Retrieve sensitive information from environment variables
HUGGINGFACE_USERNAME = os.getenv("HUGGINGFACE_USERNAME")
HUGGINGFACE_REPO_NAME = os.getenv("HUGGINGFACE_REPO_NAME")

# Project-specific paths
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(PROJECT_DIR, ".cache")
REPO_DIR = os.path.join(PROJECT_DIR, HUGGINGFACE_REPO_NAME)

# Initialize Hugging Face Repository
def setup_huggingface_repo(repo_dir, repo_name, username):
    print(f"Ensuring Hugging Face repository '{repo_name}' exists...")
    create_repo(repo_name, exist_ok=True)

    if not os.path.exists(repo_dir):
        print(f"Cloning Hugging Face repository: {repo_name}")
        subprocess.run(["git", "clone", f"https://huggingface.co/{username}/{repo_name}", repo_dir], check=True)
    else:
        print(f"Hugging Face repository already exists at: {repo_dir}")

# Load The Stack v2 dataset using streaming
def load_stack_v2_data():
    print("Loading The Stack v2 dataset (streaming)...")
    try:
        dataset = load_dataset("bigcode/the-stack-v2", split="train", streaming=True)
        print("Dataset loaded successfully!")
        return dataset
    except Exception as e:
        print("Failed to load The Stack v2 dataset:", e)

# Tokenize dataset
def preprocess_data(dataset, tokenizer_name="gpt2"):
    print(f"Initializing tokenizer: {tokenizer_name}")
    tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_name, cache_dir=CACHE_DIR)

    # Assign a padding token if it's not set
    if tokenizer.pad_token is None:
        print("Setting pad_token to eos_token.")
        tokenizer.pad_token = tokenizer.eos_token

    print("Tokenizing dataset...")
    tokenized_data = []
    for idx, sample in enumerate(dataset):
        text = sample.get("content", sample.get("path", None))
        if text:
            try:
                tokenized = tokenizer(
                    text, truncation=True, padding="max_length", max_length=512
                )
                tokenized_data.append(tokenized.data)
                print(f"Sample {idx} tokenized successfully.")
            except Exception as e:
                print(f"Failed to tokenize Sample {idx}: {e}")
        else:
            print(f"Sample {idx} missing valid text field for tokenization.")
        if idx >= 9:  # Limit to 10 samples for testing
            break

    if not tokenized_data:
        print("Warning: No tokenized data generated. Please check dataset content and tokenizer.")
    return tokenized_data

# Save tokenized data to Hugging Face repository
def save_to_huggingface_repo(tokenized_data, repo_dir):
    print("Saving tokenized data to Hugging Face repository...")
    save_path = os.path.join(repo_dir, "tokenized_data.json")

    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(tokenized_data, f, ensure_ascii=False, indent=4)
    print(f"Tokenized data saved to {save_path}")

# Commit and push changes to Hugging Face repository
def push_to_huggingface_repo(repo_dir, commit_message="Add tokenized data"):
    print("Pushing changes to Hugging Face repository...")
    try:
        os.chdir(repo_dir)
        # Check if there are staged changes
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not result.stdout.strip():
            print("No changes to commit.")
            return

        # Pull latest changes
        print("Pulling latest changes...")
        subprocess.run(["git", "pull"], check=True)

        # Add all changes
        print("Adding changes...")
        subprocess.run(["git", "add", "."], check=True)

        # Commit changes
        print("Committing changes...")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push changes
        print("Pushing changes...")
        subprocess.run(["git", "push"], check=True)

        print("Changes pushed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    setup_huggingface_repo(REPO_DIR, HUGGINGFACE_REPO_NAME, HUGGINGFACE_USERNAME)
    dataset = load_stack_v2_data()
    if dataset:
        tokenized_data = preprocess_data(dataset)
        if tokenized_data:
            save_to_huggingface_repo(tokenized_data, REPO_DIR)
            push_to_huggingface_repo(REPO_DIR)





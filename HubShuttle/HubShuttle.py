#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HubShuttle: Effortlessly Upload Diffusers Models to Hugging Face Hub.

This script streamlines the process of publishing your local Hugging Face
Diffusers models to the Hugging Face Model Hub. It handles repository
creation (if needed) and uploads all model files.

To use this script, you must first log in to your Hugging Face account
via the command line:
    huggingface-cli login

Then, you can run the script providing the necessary arguments.
"""

import os
import argparse
from huggingface_hub import create_repo, HfApi, upload_folder # Added HfApi for more robust repo creation check
from huggingface_hub.utils import HfHubHTTPError

def main():
    parser = argparse.ArgumentParser(
        description="HubShuttle: Upload Diffusers models to Hugging Face Hub.",
        formatter_class=argparse.RawTextHelpFormatter, # Allows for better formatting of help text
        epilog="""
Example usage:
  python HubShuttle.py ^
    --model_dir "C:\\path\\to\\your\\model_diffusers" ^
    --hf_username "YourHFUsername" ^
    --repo_name "MyAwesomeModel" ^
    --commit_message "Initial upload of MyAwesomeModel" ^
    --private

(Use 'python HubShuttle.py --model_dir "/path/to/your/model_diffusers" ...' on Linux/macOS)

Ensure you have run 'huggingface-cli login' before using this script.
"""
    )

    parser.add_argument(
        "--model_dir",
        type=str,
        required=True,
        help="Path to the local directory containing your Diffusers model files."
    )
    parser.add_argument(
        "--hf_username",
        type=str,
        required=True,
        help="Your Hugging Face Hub username."
    )
    parser.add_argument(
        "--repo_name",
        type=str,
        required=True,
        help="The desired name for your model repository on the Hugging Face Hub (e.g., 'MyCoolModel-v1')."
    )
    parser.add_argument(
        "--commit_message",
        type=str,
        default="Upload model using HubShuttle",
        help="The commit message for the upload (default: 'Upload model using HubShuttle')."
    )
    parser.add_argument(
        "--private",
        action="store_true", # Makes this a flag; if present, private=True
        help="Make the repository private on Hugging Face Hub (default: public)."
    )
    parser.add_argument(
        "--ignore_patterns",
        type=str,
        nargs='*', # Allows for multiple ignore patterns
        default=["*.py", "__pycache__/*"], # Sensible defaults
        help="Glob patterns for files/folders to ignore during upload (e.g., '*.txt' '*.log'). Default: '*.py' '__pycache__/*'."
    )
    parser.add_argument(
        "--repo_type",
        type=str,
        default="model",
        choices=["model", "dataset", "space"],
        help="Type of the repository on Hugging Face Hub (default: 'model')."
    )
    parser.add_argument(
        "--use_fast_transfer",
        action="store_true",
        help="Use experimental fast transfer with huggingface_hub<0.22 and git-lfs>=2.5.0 (default: False)."
    )

    args = parser.parse_args()

    # Construct repository ID
    repo_id = f"{args.hf_username}/{args.repo_name}"

    print("--- HubShuttle: Diffusers Model Uploader ---")
    print(f"ℹ️  Local model directory: {args.model_dir}")
    print(f"ℹ️  Target Hugging Face repo ID: {repo_id}")
    print(f"ℹ️  Repo visibility: {'Private' if args.private else 'Public'}")
    print(f"ℹ️  Commit message: '{args.commit_message}'")
    print(f"ℹ️  Ignoring patterns: {args.ignore_patterns}")
    if args.use_fast_transfer:
        print("ℹ️  Fast transfer enabled.")
    print("-" * 40)

    # Validate model directory
    if not os.path.isdir(args.model_dir):
        print(f"❌ Error: Model directory not found at '{args.model_dir}'. Please check the path.")
        return # Exit if directory doesn't exist

    # --- Repository Creation ---
    api = HfApi()
    try:
        print(f"⏳ Attempting to create or access repository: {repo_id}...")
        # create_repo will not error if repo exists and exist_ok=True
        create_repo(
            repo_id,
            repo_type=args.repo_type,
            private=args.private,
            exist_ok=True
        )
        print(f"✅ Repository '{repo_id}' is ready.")
    except HfHubHTTPError as e:
        # Catch specific HTTP errors, e.g., 401 Unauthorized
        print(f"❌ HTTP Error creating/accessing repository '{repo_id}': {e}")
        print("   Please ensure:")
        print("     1. You are logged in ('huggingface-cli login').")
        print("     2. Your token has the necessary write permissions.")
        print(f"     3. The username '{args.hf_username}' is correct.")
        return
    except Exception as e:
        print(f"❌ An unexpected error occurred while preparing the repository '{repo_id}': {e}")
        return

    # --- Folder Upload ---
    print(f"⏳ Uploading folder '{args.model_dir}' to '{repo_id}'...")
    try:
        upload_folder(
            folder_path=args.model_dir,
            repo_id=repo_id,
            repo_type=args.repo_type,
            commit_message=args.commit_message,
            ignore_patterns=args.ignore_patterns,
            # use_fast_transfer=args.use_fast_transfer, # As of huggingface_hub 0.22, this is handled internally
        )
        print("✅ Upload complete!")
        print(f"🎉 Your model is now available at: https://huggingface.co/{repo_id}")
    except FileNotFoundError:
        print(f"❌ Error: The folder_path '{args.model_dir}' was not found during the upload attempt.")
        print("   This can happen if the path was valid initially but became invalid, or an internal issue.")
    except Exception as e:
        print(f"❌ An error occurred during upload: {e}")
        print("   Please check:")
        print("     - Your internet connection.")
        print("     - Permissions for the repository on Hugging Face Hub.")
        print("     - If files are very large, ensure Git LFS is working correctly on your system.")
        # if not args.use_fast_transfer:
        # print("     - You might want to try the --use_fast_transfer flag if you haven't.")

if __name__ == "__main__":
    main()

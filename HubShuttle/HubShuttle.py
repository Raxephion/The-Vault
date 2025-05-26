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
from huggingface_hub import create_repo, HfApi, upload_folder
from huggingface_hub.utils import HfHubHTTPError

def main():
    parser = argparse.ArgumentParser(
        description="HubShuttle: Upload Diffusers models to Hugging Face Hub.",
        formatter_class=argparse.RawTextHelpFormatter,
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

    parser.add_argument("--model_dir", type=str, required=True, help="Path to the local directory containing your Diffusers model files.")
    parser.add_argument("--hf_username", type=str, required=True, help="Your Hugging Face Hub username.")
    parser.add_argument("--repo_name", type=str, required=True, help="The name for your model repository on the Hugging Face Hub.")
    parser.add_argument("--commit_message", type=str, default="Upload model using HubShuttle", help="The commit message for the upload.")
    parser.add_argument("--private", action="store_true", help="Make the repository private (default is public).")
    parser.add_argument("--ignore_patterns", type=str, nargs='*', default=["*.py", "__pycache__/*"], help="Patterns to ignore during upload.")
    parser.add_argument("--repo_type", type=str, default="model", choices=["model", "dataset", "space"], help="Type of Hugging Face repo.")
    parser.add_argument("--use_fast_transfer", action="store_true", help="Enable experimental fast transfer (optional).")

    args = parser.parse_args()

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

    if not os.path.isdir(args.model_dir):
        print(f"❌ Error: Model directory not found at '{args.model_dir}'.")
        return

    api = HfApi()
    try:
        print(f"⏳ Creating or accessing repository: {repo_id}...")
        create_repo(repo_id, repo_type=args.repo_type, private=args.private, exist_ok=True)
        print(f"✅ Repository '{repo_id}' is ready.")
    except HfHubHTTPError as e:
        print(f"❌ HTTP Error: {e}")
        print("   Ensure you're logged in and your token has write access.")
        return
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return

    print(f"⏳ Uploading '{args.model_dir}' to Hugging Face Hub...")
    try:
        upload_folder(
            folder_path=args.model_dir,
            repo_id=repo_id,
            repo_type=args.repo_type,
            commit_message=args.commit_message,
            ignore_patterns=args.ignore_patterns,
        )
        print("✅ Upload complete!")
        print(f"🎉 Your model is now live at: https://huggingface.co/{repo_id}")
    except FileNotFoundError:
        print(f"❌ Error: The folder '{args.model_dir}' was not found.")
    except Exception as e:
        print(f"❌ Upload failed: {e}")
        print("   Check your internet, repo permissions, or Git LFS setup.")

if __name__ == "__main__":
    main()

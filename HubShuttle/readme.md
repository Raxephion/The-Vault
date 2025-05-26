# 🚀 HubShuttle: Push Diffusers Models to Hugging Face Hub

`HubShuttle.py` is a Python script designed to simplify the process of uploading your locally stored machine learning models, specifically those in the Hugging Face Diffusers format, to the Hugging Face Model Hub. It takes all necessary information via command-line arguments, making it easy to use and integrate into your workflows.

## 📜 Description

Sharing your trained models is a crucial part of the MLOps lifecycle and open-source collaboration. This script automates the creation of a repository on the Hugging Face Hub (if it doesn't already exist) and uploads the entire contents of your local Diffusers model directory to it.


## ✨ Features

*   **Command-Line Interface:** All parameters are passed via command-line arguments for ease of use and automation.
*   **Automated Repository Creation:** Creates a new model repository on Hugging Face Hub if one with the specified name doesn't exist under your username.
*   **Full Folder Upload:** Uploads all files and subdirectories from your local Diffusers model folder.
*   **Git LFS Handling:** Automatically utilizes Git LFS for large model files, which is essential for most model checkpoints.
*   **Public or Private Repositories:** Easily specify repository visibility using the `--private` flag.
*   **Custom Commit Messages:** Allows for custom commit messages for the upload.
*   **Flexible Ignore Patterns:** Specify files or folders to ignore during the upload.
*   **Supports Different Repo Types:** Can be used for models, datasets, or spaces.

## ⚙️ How it Works

1.  **Authentication:** The script relies on you being authenticated with Hugging Face via the `huggingface-cli`. You **must** run `huggingface-cli login` and enter your token before using this script for the first time or if your token has expired.
2.  **Command Execution:** You run `HubShuttle.py` from your terminal, providing the required arguments like your model directory, Hugging Face username, and desired repository name.
3.  **Repository Creation/Access:** It attempts to create the specified repository on Hugging Face Hub using your credentials and the provided arguments. If the repository already exists, it will use the existing one.
4.  **Folder Upload:** The script then uploads the entire contents of your specified local model directory to the target repository on the Hub, using the provided commit message.

## 📋 Prerequisites

*   **Python 3.x**
*   **Required Python Libraries:**
    ```bash
    pip install huggingface_hub
    ```
    *(Note: `argparse` is part of the Python standard library for Python 3.2+ and usually doesn't need separate installation if you have a modern Python. `huggingface_hub` is the key external dependency.)*
*   **Hugging Face CLI Authentication:** You must be logged into your Hugging Face account. If you haven't already, run the following command in your terminal and follow the prompts:
    ```bash
    huggingface-cli login
    ```


    ## 🚀 Usage

Navigate to the directory containing `HubShuttle.py` and run it from your terminal using Python.

**Basic Usage:**

```bash
python HubShuttle.py --model_dir "/path/to/your/model_diffusers" --hf_username "YourHFUsername" --repo_name "MyAwesomeModel"


python HubShuttle.py ^
  --model_dir "C:\path\to\your\model_diffusers" ^
  --hf_username "YourHFUsername" ^
  --repo_name "MyAwesomeModel" ^
  --commit_message "Initial upload of MyAwesomeModel" ^
  --private


python3 HubShuttle.py \
  --model_dir "/path/to/your/model_diffusers" \
  --hf_username "YourHFUsername" \
  --repo_name "MyAwesomeModel" \
  --commit_message "Initial upload of MyAwesomeModel" \
  --private


Command-Line Arguments:
--model_dir (Required): Path to the local directory containing your Diffusers model files.
--hf_username (Required): Your Hugging Face Hub username.
--repo_name (Required): The desired name for your model repository on the Hugging Face Hub (e.g., 'MyCoolModel-v1').
--commit_message (Optional): The commit message for the upload.
Default: "Upload model using HubShuttle"
--private (Optional Flag): If present, makes the repository private on Hugging Face Hub.
Default: Public.
--ignore_patterns (Optional): Glob patterns for files/folders to ignore during upload (e.g., '*.txt' '*.log'). Can specify multiple.
Default: ['*.py', '__pycache__/*']
--repo_type (Optional): Type of the repository on Hugging Face Hub.
Choices: model, dataset, space
Default: model
--use_fast_transfer (Optional Flag): Use experimental fast transfer. May require specific git-lfs versions.
Default: Disabled.


To see all available options and their descriptions, run:
python HubShuttle.py --help

or

python3 HubShuttle.py --help



**Part 6: Notes and final separator**
```markdown
## 💡 Notes

*   Ensure your internet connection is stable during the upload, especially for large models.
*   The `upload_folder` function from `huggingface_hub` is robust and handles Git LFS for large files, which is critical for model checkpoints.
*   Always double-check your paths and usernames before running the script.

---


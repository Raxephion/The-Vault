# 🚀 HubShuttle: Push Diffusers Models to Hugging Face Hub

`HubShuttle.py` is a Python script designed to simplify the process of uploading your locally stored machine learning models, specifically those in the Hugging Face Diffusers format, to the Hugging Face Model Hub. It takes all necessary information via command-line arguments, making it easy to use and integrate into your workflows.

## 📜 Description

Sharing your trained models is a crucial part of the MLOps lifecycle and open-source collaboration. This script automates the creation of a repository on the Hugging Face Hub (if it doesn't already exist) and uploads the entire contents of your local Diffusers model directory to it.

> **Use code with caution.**

---

## ✨ Features

- **Command-Line Interface:** All parameters are passed via command-line arguments for ease of use and automation.  
- **Automated Repository Creation:** Creates a new model repository on Hugging Face Hub if one with the specified name doesn't exist under your username.  
- **Full Folder Upload:** Uploads all files and subdirectories from your local Diffusers model folder.  
- **Git LFS Handling:** Automatically utilizes Git LFS for large model files, which is essential for most model checkpoints.  
- **Public or Private Repositories:** Easily specify repository visibility using the `--private` flag.  
- **Custom Commit Messages:** Allows for custom commit messages for the upload.  
- **Flexible Ignore Patterns:** Specify files or folders to ignore during the upload.  
- **Supports Different Repo Types:** Can be used for models, datasets, or spaces.  

> **Use code with caution.**

---

## ⚙️ How it Works

1. **Authentication:** The script relies on you being authenticated with Hugging Face via the `huggingface-cli`. You **must** run `huggingface-cli login` and enter your token before using this script for the first time or if your token has expired.
2. **Command Execution:** You run `HubShuttle.py` from your terminal, providing the required arguments like your model directory, Hugging Face username, and desired repository name.
3. **Repository Creation/Access:** It attempts to create the specified repository on Hugging Face Hub using your credentials and the provided arguments. If the repository already exists, it will use the existing one.
4. **Folder Upload:** The script then uploads the entire contents of your specified local model directory to the target repository on the Hub, using the provided commit message.

> **Use code with caution.**

---

## 📋 Prerequisites

- **Python 3.x**
- **Required Python Libraries:**

    ```bash
    pip install huggingface_hub
    ```

    > *(Note: `argparse` is part of the Python standard library for Python 3.2+ and usually doesn't need separate installation if you have a modern Python. `huggingface_hub` is the key external dependency.)*

- **Hugging Face CLI Authentication:**  
  You must be logged into your Hugging Face account. If you haven't already, run the following command in your terminal and follow the prompts:

    ```bash
    huggingface-cli login
    ```

> **Use code with caution.**

---

## 🚀 Usage

Navigate to the directory containing `HubShuttle.py` and run it from your terminal using Python.

### Basic Usage

```bash
python HubShuttle.py --model_dir "/path/to/your/model_diffusers" --hf_username "YourHFUsername" --repo_name "MyAwesomeModel"

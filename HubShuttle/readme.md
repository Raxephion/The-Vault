# 🚀 HubShuttle: Push Diffusers Models to Hugging Face Hub

`HubShuttle.py` is a Python script designed to simplify the process of uploading your locally stored machine learning models, specifically those in the Hugging Face Diffusers format, to the Hugging Face Model Hub.

## 📜 Description

Sharing your trained models is a crucial part of the MLOps lifecycle and open-source collaboration. This script automates the creation of a repository on the Hugging Face Hub (if it doesn't already exist) and uploads the entire contents of your local Diffusers model directory to it.

## ✨ Features

*   **Automated Repository Creation:** Creates a new model repository on Hugging Face Hub if one with the specified name doesn't exist under your username.
*   **Full Folder Upload:** Uploads all files and subdirectories from your local Diffusers model folder.
*   **Git LFS Handling:** Automatically utilizes Git LFS for large model files, which is essential for most model checkpoints.
*   **Public or Private:** Can be configured to create public or private repositories.
*   **Custom Commit Messages:** Allows for custom commit messages for the upload.

## ⚙️ How it Works

1.  **Configuration:** The script requires you to provide details such as:
    *   The local path to your Diffusers model directory.
    *   Your Hugging Face Hub username.
    *   The desired name for the repository on the Hub.
    *   (Optionally) Whether the repository should be private.
2.  **Authentication:** It relies on you being authenticated with Hugging Face via the `huggingface-cli`. You **must** run `huggingface-cli login` and enter your token before using this script for the first time or if your token has expired.
3.  **Repository Creation/Access:** It attempts to create the specified repository on Hugging Face Hub using your credentials. If the repository already exists, it will use the existing one.
4.  **Folder Upload:** The script then uploads the entire contents of your specified local model directory to the target repository on the Hub.

## 📋 Prerequisites

*   **Python 3.x**
*   **Hugging Face Hub Library:**
    ```bash
    pip install huggingface_hub
    ```
*   **Hugging Face CLI Authentication:** You must be logged into your Hugging Face account. If you haven't already, run the following command in your terminal and follow the prompts:
    ```bash
    huggingface-cli login
    ```

## 🚀 Usage

*(This section will be updated once the script is modified to accept command-line arguments.)*

Currently, you need to configure the script parameters directly within the `HubShuttle.py` file. Once configured, you can run it from your terminal:

```bash
python HubShuttle.py

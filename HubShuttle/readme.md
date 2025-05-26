# 🚀 HubShuttle: Upload Your Diffusers Models to Hugging Face Hub

**HubShuttle** is a simple command-line script to help you upload your Stable Diffusion models (in 🤗 Diffusers format) to the Hugging Face Model Hub — no need to mess with Git or advanced tools.

## ✅ Features
- Automatically creates the Hugging Face repo (if it doesn't exist)
- Uploads your entire Diffusers model folder
- Supports public and private uploads
- Lets you ignore unnecessary files like `.py` or `__pycache__`
- Lightweight and beginner-friendly

## 📦 Requirements

Install the required package:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install huggingface_hub>=0.21.0
```

## 🔐 Prerequisites

Login to your Hugging Face account from the terminal:

```bash
huggingface-cli login
```

## 💡 Usage

Basic command (Windows):

```bash
python HubShuttle.py ^
  --model_dir "C:\\path\\to\\your\\diffusers_model" ^
  --hf_username "your-username" ^
  --repo_name "MyAwesomeModel"
```

Linux/macOS:

```bash
python HubShuttle.py \
  --model_dir "/path/to/your/diffusers_model" \
  --hf_username "your-username" \
  --repo_name "MyAwesomeModel"
```

### Optional flags:
- `--private` → Makes the repo private
- `--commit_message "your message"` → Custom commit message
- `--ignore_patterns "*.txt" "*.log"` → Skip files during upload
- `--repo_type "model"` → Or use `dataset` or `space` if applicable

## 🌍 After Upload

Your model will be viewable at:

```
https://huggingface.co/your-username/MyAwesomeModel
```

## 🛠️ Notes
- You can re-run the script to upload changes.
- Git LFS is handled automatically.
- Fast transfer flag (`--use_fast_transfer`) is experimental and usually not needed.

---

Happy uploading!  
— **The Vault**

# 🏦 The-Vault: Generative AI Workflow Tools

Welcome to **The-Vault**! This repository is a growing collection of Python scripts and tools designed to aid and assist with generative (Creative AI) workflows, particularly focusing on image generation, model/LoRA inspection, and model management.

These tools are developed to be simple, effective, and are available **free for personal use**. My aim is to provide practical utilities that can help enthusiasts, artists, and developers streamline their creative AI processes.

This is an **ongoing project**, and I will be adding more tools and refining existing ones as I develop them. Your feedback and suggestions are welcome!

🌟 What's Inside?

The-Vault currently contains:

- **HubShuttle**: A simple script to upload your Hugging Face Diffusers models to the Hugging Face Hub in one command. Handles repo creation, file upload, ignore patterns, and optional privacy — no coding required.


Below is a breakdown of the tools available:

---

### 🛠️ Current Tools

#### 1. HubShuttle (`hubshuttle.py`)
   * **What it does:** Uploads a local Hugging Face Diffusers model to the Hugging Face Hub in one go.
   * **How it works:**
     1. Accepts arguments like your model directory, repo name, username, and commit message via command line.
     2. Creates a new repo on Hugging Face Hub (or reuses one if it already exists).
     3. Uploads your model files with optional ignore patterns and privacy settings.
   * **Use Case:** Great for creators who want to share or back up their models without messing around with git or the web UI — just run the script and you're done.

---


### 🚀 Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/The-Vault.git
    cd The-Vault
    ```
2.  **Install Dependencies:**
    Most scripts rely on common libraries in the generative AI space. Ensure you have them installed, typically:
    ```bash
    pip install torch torchvision torchaudio safetensors diffusers transformers accelerate huggingface_hub
    ```
    *Note: A `requirements.txt` file may be added in the future for easier dependency management.*

3.  **Using the Tools:**
    *   Navigate to the directory containing the script you want to use.
    *   **Important:** Most scripts currently have hardcoded file paths (e.g., `lora_path`, `checkpoint_path`, `output_directory`, `model_directory`) and configuration (e.g., `your_username`, `repo_name`). You will need to **open the Python script and modify these parameters** to point to your local files and set your configurations.
    *   **For Hugging Face Uploads:** Ensure you are logged in to Hugging Face. If you haven't already, run `huggingface-cli login` in your terminal and follow the prompts.
    *   Run the script from your terminal:
        ```bash
        python script_name.py
        ```
    *   Follow any on-screen prompts or observe the output.

---

### 🔮 Future Plans

This vault is far from full! I plan to add more tools, including but not limited to:

*   More advanced model and LoRA analysis tools.
*   Batch processing utilities for common tasks.
*   Helpers for dataset preparation or augmentation.
*   Scripts for comparing model outputs or embeddings.
*   User-friendly interfaces or wrappers for existing CLI tools (e.g., using `argparse` for command-line arguments instead of hardcoded paths).

Your suggestions for new tools are highly encouraged! Feel free to open an issue to suggest a new feature or tool.

---

### 🤝 Contributing (Suggestions & Feedback)

While this is primarily a personal project, I'm open to suggestions, feedback, and identifying bugs. Please feel free to:

*   **Open an Issue:** If you find a bug, have a feature request, or a suggestion for a new tool.
*   **Provide Feedback:** Let me know if these tools are helpful for your workflows!

---

### 📜 License

The tools in this repository are provided **free for personal use**.

Please note: While the scripts are provided for personal use, the underlying libraries (`torch`, `diffusers`, `safetensors`, `huggingface_hub`, etc.) are subject to their own licenses.

---

Happy generating!
raxep (Your GitHub Username/Name)

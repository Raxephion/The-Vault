# 🏦 The-Vault: Generative AI Workflow Tools

Welcome to **The-Vault**! This repository is a growing collection of Python scripts and tools designed to aid and assist with generative (Creative AI) workflows, particularly focusing on image generation, model/LoRA inspection, and model management.

These tools are developed to be simple, effective, and are available **free for personal use**. My aim is to provide practical utilities that can help enthusiasts, artists, and developers streamline their creative AI processes.

This is an **ongoing project**, and I will be adding more tools and refining existing ones as I develop them. Your feedback and suggestions are welcome!

## 🌟 What's Inside?

The-Vault currently contains tools for:

1.  **LoRA Inspection & Analysis:** Understand the LoRAs you're using.
2.  **Model Conversion:** Bridge formats between different frameworks.
3.  **Checkpoint/Model Analysis:** Peek inside your model files.
4.  **Model Sharing:** Upload your models to the Hugging Face Hub.

Below is a breakdown of the tools available:

---

### 🛠️ Current Tools

#### 1. LoRA Base Model Guesser (`lora_base_model_guesser.py` - *derived from your `lora inspector`*)
   *   **What it does:** Helps you quickly determine the likely base model (e.g., SD1.5, SDXL) a LoRA was trained on.
   *   **How it works:** It opens a `.safetensors` LoRA file and prints the first few tensor keys. The naming convention of these keys (e.g., `lora_unet_...`, `lora_te_...` for SD1.5 vs `lora_te1_...`, `lora_te2_...` for SDXL) often reveals the target architecture.
   *   **Use Case:** Useful when you've downloaded a LoRA and are unsure which base model it's compatible with.

#### 2. LoRA Layer Rank & Alpha Inspector (`lora_rank_alpha_inspector.py` - *derived from your `lora layer ranks inspector`*)
   *   **What it does:** Provides a detailed look into the structure of a LoRA, showing the rank and alpha values for each trained module.
   *   **How it works:** Loads a `.safetensors` LoRA and:
        1.  Categorizes tensor keys into UNet, Text Encoder 1 (TE1), and Text Encoder 2 (TE2) components.
        2.  For each identified LoRA module (e.g., an attention block), it extracts and displays the shape of `lora_down.weight` and `lora_up.weight` (which indicates the rank) and the `alpha` value.
   *   **Use Case:** Helps advanced users understand the "strength" and complexity of a LoRA, which layers were trained, and at what capacity. This can be insightful for debugging, merging, or fine-tuning LoRAs.

#### 3. Merged Model Inspector (`merged_model_inspector.py`)
   *   **What it does:** Checks if a model file (typically a `.safetensors` or `.ckpt` checkpoint) contains LoRA layers. This is particularly useful for verifying if a LoRA has been successfully merged into a base model.
   *   **How it works:** Loads the model file and scans its state dictionary for keys containing "lora_". If such keys are found, it confirms their presence and lists a preview. If not, it indicates that no LoRA layers were detected and shows some top-level keys for context.
   *   **Use Case:** Verifying LoRA merges, understanding the composition of a downloaded model, or checking if a model has residual LoRA layers.

#### 4. Safetensors to Diffusers Converter (`safetensors_to_diffusers_converter.py`)
   *   **What it does:** Converts a standalone `.safetensors` checkpoint file (e.g., a fine-tuned Stable Diffusion model) into the Hugging Face Diffusers library format.
   *   **How it works:** Utilizes the `StableDiffusionPipeline.from_single_file()` method from the `diffusers` library to load the `.safetensors` model and then saves it using `pipe.save_pretrained()` into a directory structure compatible with Diffusers. It also includes an optional verification step to load the converted model.
   *   **Use Case:** Essential for users who want to use `.safetensors` models with pipelines or frameworks that expect the Diffusers format, or for easier integration with `diffusers`-based applications.

#### 5. Push Diffusers Model to Hugging Face Hub (`diffusers_to_hf_uploader.py` - *derived from your `push diffusers to HF`*)
   *   **What it does:** Uploads a locally stored model (in Diffusers format) to a new or existing repository on the Hugging Face Hub.
   *   **How it works:**
        1.  You configure your Hugging Face username and the desired repository name within the script.
        2.  It uses the `huggingface_hub` library to create a model repository on your Hugging Face account (if it doesn't already exist).
        3.  It then uploads all files from the specified local model directory (which should contain your Diffusers model) to this Hugging Face repository. Git LFS is automatically handled for large files.
        4.  **Important:** You must be logged into your Hugging Face account via the CLI (`huggingface-cli login`) before running this script.
   *   **Use Case:** Easily share your fine-tuned models or converted checkpoints with the community, for collaboration, or for personal backup/access across different environments by hosting them on the Hugging Face Hub.

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

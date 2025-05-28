# 🧪 TensorLayerCheck

**TensorLayerCheck** scans `.safetensors` and `.pt` model files to detect embedded **LoRA layers** and previews their keys.

Perfect for debugging merged models, verifying LoRA integrations, or just satisfying your curiosity.

---

## 🔧 What It Does

- ✅ Detects and lists any `lora_` keys in a model file.
- ✅ Supports both `.safetensors` and `.pt` formats.
- ✅ Previews the first 10 LoRA keys (if found).
- ✅ Falls back to previewing top-level keys if no LoRA keys are present.

---

## 🚀 Usage

Edit the `check_merge_file()` call at the bottom of the script:

```python
check_merge_file(r"C:\Path\To\YourModel.safetensors")
```

Then run it:

```bash
python tensorlayercheck.py
```

---

## 📦 Requirements

Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧩 Example Output

```
🔍 Scanning file for LoRA layers:
  📄 Path: Typhoon-Anime.fp16.safetensors
  📛 Name: Typhoon-Anime.fp16.safetensors
✅ Detected 82 LoRA-related layers.
📚 LoRA Layer Keys Preview:
  - lora_unet_down_blocks_0_attentions_0_proj_in.weight
  - lora_unet_down_blocks_0_attentions_0_proj_out.weight
  ...
```

---

## 🔗 Related Tools

- Want metadata and base model inference? Check out [`TensorPeek`](../TensorPeek).

---

## 🛠️ Part of The Vault

A suite of powerful tools for Generative AI tinkerers, builders, and chaos agents.

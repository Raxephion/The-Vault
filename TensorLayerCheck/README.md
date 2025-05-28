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

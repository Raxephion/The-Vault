# 🧬 TensorMorph-SD

Morph your `.safetensors` checkpoint into a fully usable 🤗 Diffusers model—because raw tensors aren’t fun to play with.

---

## 🚀 What it does

**TensorMorph-SD** takes a Stable Diffusion `.safetensors` file—whether it's SD 1.5, SDXL, pony models, anime, or obscure forks—and converts it into a clean, well-formed Diffusers directory.

You get a pretty folder full of `unet`, `vae`, `tokenizer`, and other stuff that makes 🤗 Diffusers work the way it should.

---

## 📦 How to use

1. Drop your `.safetensors` checkpoint wherever.  
2. Update the config section in `TensorMorph-SD.py`:

    ```python
    checkpoint_path = r"Path\To\Your\model.safetensors"
    output_directory = r"Path\Where\You\Want\The\Model"
    ```

3. Run it:

    ```bash
    python TensorMorph-SD.py
    ```

Done.

---

## 🧪 What it checks

- ✅ Can it load the safetensors model?  
- ✅ Can it save the model into Diffusers format?  
- ✅ Can it reload that folder to confirm conversion worked?

It’ll yell at you if any step fails. Otherwise, smooth sailing.

---

## 📋 Requirements

- PyTorch  
- Diffusers  
- Transformers (via Diffusers)  
- Safetensors (comes along for the ride)

See [`requirements.txt`](./requirements.txt) for install specifics.

---

## 🐍 Output looks like this

```
YourModel/
├── model_index.json
├── scheduler/
├── tokenizer/
├── unet/
├── vae/
└── ...
```

Ready to use with `StableDiffusionPipeline.from_pretrained()`.

---

## 🤖 Notes

- Uses `torch.float16`. If that gives you grief, change it to `float32`.  
- No training or fine-tuning here—just pure format conversion.  
- Works with SD 1.5, SDXL, Illustrious, Pony Diffusion, anime models, and more.

---



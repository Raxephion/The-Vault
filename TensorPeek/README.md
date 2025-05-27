# 🧠 TensorPeek

**"What's in the box?"** – you, after downloading a `.safetensors` model from somewhere shady on the internet.

**TensorPeek** is a small script that does two things:  
1. Peeks inside `.safetensors` files and prints out the metadata (if any).  
2. Scans the tensor keys and makes a semi-educated guess about what base model it belongs to (e.g., SD 1.5, SDXL, Pony, Anime, etc.).

That's it. No torch models are loaded. No GPU is harmed. Just cold, hard metadata and some good old-fashioned string matching.

---

## 🔍 What It Does

- ✅ Loads a `.safetensors` file safely and extracts its metadata (from the file header).  
- ✅ Lists the first few tensor keys inside the file.  
- ✅ Tries to guess the base model type based on known key patterns.

You get readable, structured output printed right to your terminal.

---

## 🤔 Why Would I Use This?

A few use cases for the curious (or cautious) AI tinkerer:

- **Downloaded a model but not sure what it is?** This gives you a fast sanity check.  
- **Writing docs, organizing models, or managing LoRAs?** Peek the internals and label them accordingly.  
- **Training or merging models?** Know your base model architecture before you mess things up.  
- **You're just nosy.** Respect.

---

## 🚀 How to Use

Edit the `model_path` inside the script to point to your `.safetensors` file:

```python
model_path = r"C:\path\to\your\model.safetensors"
```

Then run it:

```bash
python tensorpeek.py
```

You'll get:

- Any metadata stored in the header  
- A quick preview of the tensor keys  
- A base model guess (based on what’s typical for SD 1.5 / 2.x / SDXL / Pony / etc.)

---

## 📦 Dependencies

Just the `safetensors` library:

```bash
pip install safetensors
```

---

## ⚠️ Notes

- This doesn't tell you everything, but it's often enough to know what you're dealing with.  
- It's a read-only operation — nothing is written or modified.  
- Assumes the model was saved in the standard `safetensors` format (surprise: some people do weird stuff).

---

## 🧬 Output Example

```
📄 Metadata:
  title: Typhoon Anime Plus
  fp16: true

🔍 Found 4382 tensor keys.
First few keys:
  model.diffusion_model.input_blocks.0.0.weight
  model.diffusion_model.input_blocks.0.1.bias
  ...

🧠 Base Model Guess: Probably SD 1.5 or 2.x
```

---

## 🐾 Coming Soon?

If you want this script to spit out even more (e.g., layer size stats, LoRA detection, tensor shape dumps, etc.), feel free to yell at me. Or fork it and bolt on what you need.

---

**Happy peeking.**

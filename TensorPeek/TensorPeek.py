# tensorpeek.py

"""
TensorPeek – Inspect metadata and tensor structure in .safetensors files.

Created: 2025-05-25
Author: raxephion

A quick and safe way to peek inside your .safetensors model files.
"""

import os
from safetensors import safe_open

# 🔧 Edit this path to point to your model file
model_path = r"C:\Users\raxep\Desktop\SDForge\webui\models\Stable-diffusion\Typhoon Anime Plus.fp16.safetensors"


def infer_base_model(keys):
    """
    Attempt to guess the base model architecture based on tensor keys.
    """
    if any("model.diffusion_model.input_blocks.0.0.weight" in k for k in keys):
        if any("model.diffusion_model.middle_block.0.attn1.to_q.weight" in k for k in keys):
            return "Probably SDXL"
        return "Probably SD 1.5 or 2.x"
    if any("lora_unet" in k for k in keys) or any("transformer.block" in k for k in keys):
        return "Could be Pony/Anime model"
    return "Unknown"


def main():
    if not os.path.exists(model_path):
        print("❌ Model file not found.")
        return

    try:
        with safe_open(model_path, framework="pt", device="cpu") as f:
            # Print metadata if present
            metadata = f.metadata()
            print("📄 Metadata:")
            if metadata:
                for key, value in metadata.items():
                    print(f"  {key}: {value}")
            else:
                print("  No metadata in header.")

            # Print key summary
            keys = list(f.keys())
            print(f"\n🔍 Found {len(keys)} tensor keys.")
            print("First few keys:")
            for k in keys[:10]:
                print(f"  {k}")

            # Inference guess
            guess = infer_base_model(keys)
            print(f"\n🧠 Base Model Guess: {guess}")

    except Exception as e:
        print(f"❌ Error reading file: {e}")


if __name__ == "__main__":
    main()

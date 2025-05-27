# tensorpeek.py
# -*- coding: utf-8 -*-
"""
Inspect a .safetensors file for metadata, tensor keys, and architecture inference.

Author: raxephion
Date: May 25, 2025
"""

import os
import json
from safetensors import safe_open

# 🔧 SET YOUR MODEL PATH HERE
model_path = r"C:\Users\...\ComfyUI\models\checkpoints\File.safetensors"     # Please set your full model path here


def infer_base_model(keys, metadata):
    # 1. Check if SDXL is mentioned in the merge metadata
    if "sd_merge_models" in metadata:
        for model_info in metadata["sd_merge_models"].values():
            name = model_info.get("name", "").lower()
            if "sdxl" in name:
                return "SDXL (from sd_merge_models)"

    # 2. Check bake-in VAE field
    if "sd_merge_recipe" in metadata:
        bake_vae = metadata["sd_merge_recipe"].get("bake_in_vae", "").lower()
        if "sdxl" in bake_vae:
            return "SDXL (from bake_in_vae)"

    # 3. Look for SDXL-specific architecture keys
    if any("model.diffusion_model.middle_block.0.attn1.to_q.weight" in k for k in keys):
        return "SDXL (from architecture)"

    # 4. Check for LoRA-style keys
    if any("lora_unet" in k for k in keys) or any("transformer.block" in k for k in keys):
        return "Possibly LoRA (Pony/Anime model)"

    # 5. Fallback
    return "SD 1.5 / SD 2.x or Unknown"


# 🧪 Run inspection
if not os.path.exists(model_path):
    print("❌ Model file not found.")
else:
    try:
        with safe_open(model_path, framework="pt", device="cpu") as f:
            metadata = f.metadata()
            print("📄 Metadata:")
            if metadata:
                # Try to parse embedded JSON strings if present
                for key in ["sd_merge_models", "sd_merge_recipe"]:
                    if key in metadata:
                        try:
                            metadata[key] = json.loads(metadata[key])
                        except Exception as e:
                            print(f"⚠️  Could not parse {key}: {e}")

                for k, v in metadata.items():
                    print(f"  {k}: {v}")
            else:
                print("  No metadata in header.")

            keys = list(f.keys())
            print(f"\n🔍 Found {len(keys)} tensor keys.")
            print("First few keys:")
            for k in keys[:10]:
                print(f"  {k}")

            guess = infer_base_model(keys, metadata)
            print(f"\n🧠 Base Model Guess: {guess}")

    except Exception as e:
        print(f"❌ Error: {e}")

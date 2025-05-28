# -*- coding: utf-8 -*-
"""
TensorMorph-SD - Morph your Stable Diffusion safetensors into usable models

Created on Sun May 25 09:21:31 2025
@author: raxephion
"""

import torch
import sys
from diffusers import StableDiffusionPipeline
from pathlib import Path

# --- Configuration ---
checkpoint_path = r"C:\Users\...\Stable-diffusion\Typhoon.fp16.safetensors"
output_directory = r"C:\Users\...\Typhoon V1 Transformers"

# --- Conversion ---
print(f"🔄 Loading checkpoint: {checkpoint_path}")
try:
    pipe = StableDiffusionPipeline.from_single_file(
        checkpoint_path,
        torch_dtype=torch.float16,
        load_safety_checker=False
    )
    print("✅ Checkpoint loaded successfully.")
except FileNotFoundError:
    print(f"❌ Error: Checkpoint file not found at {checkpoint_path}")
    sys.exit(1)
except Exception as e:
    print(f"❌ An error occurred while loading the checkpoint: {e}")
    sys.exit(1)

print(f"💾 Saving converted model to: {output_directory}")
try:
    pipe.save_pretrained(output_directory)
    print("✅ Model saved successfully.")
except Exception as e:
    print(f"❌ An error occurred while saving the model: {e}")
    sys.exit(1)

print("✅ Conversion complete!")

# --- Optional Verification ---
print("\n🔍 Verifying conversion...")
try:
    loaded_pipe = StableDiffusionPipeline.from_pretrained(output_directory, torch_dtype=torch.float16)
    print("✅ Model reloaded successfully from Diffusers format.")
except FileNotFoundError:
    print(f"❌ Error: Output directory not found at {output_directory}. Save might have failed.")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error loading converted model: {e}")
    sys.exit(1)

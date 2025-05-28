# tensorlayercheck.py
# -*- coding: utf-8 -*-
"""
TensorLayerCheck - Scan models for embedded LoRA layers and key previews.

Author: raxephion
Date: May 25, 2025
"""

import os

def check_merge_file(file_path):
    print("🔍 Scanning file for LoRA layers:")
    print(f"  📄 Path: {file_path}")
    
    model_name = os.path.basename(file_path)
    print(f"  📛 Name: {model_name}")

    try:
        if file_path.endswith(".safetensors"):
            from safetensors.torch import load_file
            state_dict = load_file(file_path)
        else:
            import torch
            state_dict = torch.load(file_path, map_location="cpu", weights_only=False)
            if "state_dict" in state_dict:
                state_dict = state_dict["state_dict"]

        lora_keys = [k for k in state_dict if "lora_" in k]

        if not lora_keys:
            print("⚠️ No LoRA-related keys found in this file.")
            print("\n🧠 Top-level keys preview:")
            for i, key in enumerate(state_dict.keys()):
                if i >= 10:
                    print("  ...and more.")
                    break
                print(f"  - {key}")
        else:
            print(f"✅ Detected {len(lora_keys)} LoRA-related layers.")
            print("📚 LoRA Layer Keys Preview:")
            for key in lora_keys[:10]:
                print(f"  - {key}")
            if len(lora_keys) > 10:
                print("  ...and more.")

    except Exception as e:
        print(f"❌ Error while reading the file: {e}")

# Example usage — replace with your actual file path
check_merge_file(r"C:\Users\YourUser\Path\To\Model.safetensors")

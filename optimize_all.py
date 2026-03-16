#!/usr/bin/env python3
from PIL import Image
import os
import glob

def convert_to_webp(directory):
    for ext in ('*.png', '*.jpg', '*.jpeg'):
        for img_path in glob.glob(os.path.join(directory, ext)):
            # Skip if it's already a webp or a specialized icon format
            if 'favicon' in img_path.lower():
                continue
                
            img = Image.open(img_path)
            # Ensure image is in RGB for JPEG conversion, though WebP supports RGBA
            if img.mode != 'RGBA' and img.mode != 'RGB':
                img = img.convert('RGBA')
                
            webp_path = os.path.splitext(img_path)[0] + '.webp'
            img.save(webp_path, 'WEBP', quality=80)
            print(f"Converted {img_path} to {webp_path}")

if __name__ == "__main__":
    convert_to_webp('images')

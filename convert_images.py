#!/usr/bin/env python3
"""Convert JPEG images to WebP format"""
from PIL import Image
import os

def convert_images():
    source_dir = 'images/dora/new'
    dest_dir = 'images/dora'
    
    images = [
        ("01_en-US-1-Introduction Large.jpeg", "01.webp"),
        ("02_en-US-2-Introduction Copy Large.jpeg", "02.webp"),
        ("03_en-US-3-Introduction Copy Copy Copy Copy Copy Large.jpeg", "03.webp"),
        ("04_en-US-4-Introduction Copy Copy Copy Large.jpeg", "04.webp"),
        ("05_en-US-5-Introduction Copy Copy Large.jpeg", "05.webp"),
        ("06_en-US-6-Introduction Copy Copy Copy Copy Large.jpeg", "06.webp"),
        ("07_en-US-7-Introduction Copy Copy Copy Large.jpeg", "07.webp"),
        ("08_en-US-8-Introduction Copy Copy Copy Large.jpeg", "08.webp"),
        ("09_en-US-9-Introduction Copy Copy Copy Copy Copy Large.jpeg", "09.webp"),
        ("10_en-US-10-Introduction Copy Copy Copy Copy Copy Copy Large.jpeg", "10.webp"),
    ]
    
    for source, dest in images:
        source_path = os.path.join(source_dir, source)
        dest_path = os.path.join(dest_dir, dest)
        
        print(f"Converting {source} -> {dest}")
        img = Image.open(source_path)
        img.save(dest_path, 'WEBP', quality=85)
        print(f"  ✓ Created {dest_path}")
    
    print(f"\n✓ Successfully converted {len(images)} images to WebP")

if __name__ == "__main__":
    convert_images()

import os
import shutil

# Root folder containing "gallery"
root = "samples_image"

gallery_dir = os.path.join(root, "gallery")
backup_dir = os.path.join(root, "gallery_backup")

# Create backup dir if missing
os.makedirs(backup_dir, exist_ok=True)

# Iterate through files in gallery
for fname in os.listdir(gallery_dir):
    # Match files like "sample_xxxx-1.png"
    if fname.endswith("-1.png"):
        src = os.path.join(gallery_dir, fname)
        dst = os.path.join(backup_dir, fname)
        print(f"Moving: {src} -> {dst}")
        shutil.move(src, dst)

print("Done!")

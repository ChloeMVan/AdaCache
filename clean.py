import os
import glob
import shutil

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------
ROOT_DIR = "samples_image"
GALLERY_PATTERN = os.path.join(ROOT_DIR, "gallery*")  # find gallery, gallery123, galleryXYZ, etc.

# ------------------------------------------------------------
# Find matching gallery directories
# ------------------------------------------------------------
gallery_dirs = [d for d in glob.glob(GALLERY_PATTERN) if os.path.isdir(d)]

if not gallery_dirs:
    raise FileNotFoundError(f"No gallery directories match pattern: {GALLERY_PATTERN}")

print("Found gallery directories:")
for d in gallery_dirs:
    print(f"  - {d}")

# ------------------------------------------------------------
# Process each gallery directory
# ------------------------------------------------------------
for gallery_dir in gallery_dirs:
    # Create a backup directory specifically for THIS gallery
    backup_dir = gallery_dir + "_backup"
    os.makedirs(backup_dir, exist_ok=True)

    print(f"\nProcessing: {gallery_dir}")
    print(f"Backup dir: {backup_dir}")

    # Move matching files
    for fname in os.listdir(gallery_dir):
        if fname.endswith("-1.png"):   # match whatever pattern you want
            src = os.path.join(gallery_dir, fname)
            dst = os.path.join(backup_dir, fname)

            print(f"  Moving: {src} -> {dst}")
            shutil.move(src, dst)

print("\nDone!")

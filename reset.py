import os
import shutil

def empty_directory(directory_path):
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        # Remove the directory and all its contents
        shutil.rmtree(directory_path)
        # Recreate an empty directory
        os.makedirs(directory_path)
    else:
        # Create the directory if it doesn't exist
        os.makedirs(directory_path)

def remove(directory_path):
    try:
        shutil.rmtree(directory_path)
        print(f"Directory '{directory_path}' and its contents deleted successfully.")
    except FileNotFoundError:
        print(f"Error: Directory '{directory_path}' not found.")
    except OSError as e:
        print(f"Error deleting directory: {e}")

empty_directory("samples_video/gallery")
empty_directory("samples_video/metrics")

empty_directory("samples_image/gallery")
empty_directory("samples_image/gallery_backup")
empty_directory("samples_image/metrics")

empty_directory("samples_video/gallery")
empty_directory("samples_video/metrics")

d = "_d"
remove("samples_image/gallery" + d)
remove("samples_image/gallery_backup"  + d)
remove("samples_image/metrics" + d)

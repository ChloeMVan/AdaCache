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

def add(path):
    try:
        with open(path, "x") as f:
            print("File 'new_exclusive_file.txt' created successfully.")
    except FileExistsError:
        print("Error: File 'new_exclusive_file.txt' already exists.")

def empty_directories_and_files(root_path: str) -> None:
    """
    Recursively empties all directories under `root_path`.
    - Deletes all non-txt/csv files.
    - Empties the contents of any .txt or .csv files.
    - Keeps directory structure intact.
    """

    if not os.path.isdir(root_path):
        raise ValueError(f"Path does not exist or is not a directory: {root_path}")

    # Walk the tree
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)

            # For .txt or .csv: empty them
            if filename.lower().endswith(".txt") or filename.lower().endswith(".csv"):
                try:
                    with open(file_path, "w", encoding="utf-8") as f:
                        pass  # writing nothing truncates the file
                    print(f"Emptied: {file_path}")
                except Exception as e:
                    print(f"Error emptying {file_path}: {e}")

            # For all other files: delete them
            else:
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

empty_directories_and_files("samples_video")
empty_directories_and_files("samples_image")

# empty_directory("samples_video/gallery")
# empty_directory("samples_video/metrics")

# empty_directory("samples_image/gallery")
# empty_directory("samples_image/gallery_backup")
# empty_directory("samples_image/metrics")
# add("samples_image/metrics/latency.txt")
# add("samples_image/metrics/adacache_metrics.csv")

# empty_directory("samples_video/gallery")
# empty_directory("samples_video/metrics")
# add("samples_video/gallery/metrics/latency.txt")
# add("samples_video/metrics/adacache_metrics.csv")

# d = "_d"
# remove("samples_image/gallery" + d)
# remove("samples_image/gallery_backup"  + d)
# remove("samples_image/metrics" + d)

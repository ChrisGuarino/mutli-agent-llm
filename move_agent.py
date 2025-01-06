import os
import shutil
from utilities import log_action

def move_files(categorized_files, destination_folder):
    """
    Moves files into categorized subfolders with error handling for duplicates and permissions.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for category, file_list in categorized_files.items():
        category_folder = os.path.join(destination_folder, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        for file in file_list:
            source_path = file["file_path"]
            destination_path = os.path.join(category_folder, file["file_name"])

            # Handle duplicate file names
            counter = 1
            while os.path.exists(destination_path):
                base, ext = os.path.splitext(file["file_name"])
                destination_path = os.path.join(category_folder, f"{base}_{counter}{ext}")
                counter += 1

            # Try moving the file with permission error handling
            try:
                shutil.move(source_path, destination_path)
                log_action(f"Moved: {source_path} -> {destination_path}")
            except PermissionError:
                log_action(f"PermissionError: Unable to move {source_path}", error=True)
            except Exception as e:
                log_action(f"Error moving {source_path}: {str(e)}", error=True)
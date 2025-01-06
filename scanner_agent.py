import os

def scan_folder(folder_path):
    """
    Scans the given folder and lists all files with basic metadata.
    """
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return []

    file_list = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_metadata = {
                "file_name": file,
                "file_path": file_path,
                "file_size": os.path.getsize(file_path),
                "file_extension": os.path.splitext(file)[1].lower()
            }
            file_list.append(file_metadata)
    
    return file_list

# Example usage
folder_path = input("Enter the folder path to scan: ")
files = scan_folder(folder_path)

if files:
    print("Scanned files:")
    for file in files:
        print(f"{file['file_name']} | Size: {file['file_size']} bytes | Type: {file['file_extension']}")
else:
    print("No files found or folder is empty.")
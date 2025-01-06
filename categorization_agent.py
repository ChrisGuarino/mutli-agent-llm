def categorize_files(file_list):
    """
    Categorizes files into predefined categories based on their file extensions.
    """
    # Define categories and associated file extensions
    categories = {
        "Documents": [".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Code": [".py", ".java", ".cpp", ".js", ".html", ".css", ".sql"],
        "Others": []  # Catch-all category for unknown file types
    }

    # Initialize categorized files dictionary
    categorized_files = {category: [] for category in categories}

    for file in file_list:
        file_extension = file["file_extension"]
        categorized = False

        # Check each category for the file extension
        for category, extensions in categories.items():
            if file_extension in extensions:
                categorized_files[category].append(file)
                categorized = True
                break
        
        # If no matching category, add to "Others"
        if not categorized:
            categorized_files["Others"].append(file)

    return categorized_files


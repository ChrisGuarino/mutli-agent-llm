from utilities import log_action
from scanner_agent import scan_folder
from categorization_agent import categorize_files
from move_agent import move_files

def main_workflow(source_folder, destination_folder):
    """
    Combines all agents into a single workflow for scanning, categorizing, and moving files.
    """
    # Step 1: Scan the folder
    log_action("Starting file scan...")
    files = scan_folder(source_folder)
    if not files:
        log_action("No files found to process.", error=True)
        return

    # Step 2: Categorize the files
    log_action("Categorizing files...")
    categorized_files = categorize_files(files)

    # Step 3: Move the files with error handling
    log_action("Moving files to categorized folders...")
    move_files(categorized_files, destination_folder)

    log_action("Workflow completed successfully!")

# Example usage
source_folder = input("Enter the source folder path: ")
destination_folder = input("Enter the destination folder path: ")
main_workflow(source_folder, destination_folder)
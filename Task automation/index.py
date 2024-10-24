import os
import shutil

# Path to the folder that needs to be organized.
download_folder = 'C:/Users/Administrator/Downloads'

# File types mapped to their respective folder names.
file_categories = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif'],
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx'],
    "Videos": ['.mp4', '.mkv', '.avi'],
    "Archives": ['.zip', '.rar', '.tar'],
}

# Create necessary folders if they don't already exist.
def setup_folders():
    for category in file_categories.keys():
        folder_path = os.path.join(download_folder, category)
        if not os.path.exists(folder_path):
            print(f"Creating folder: {folder_path}")
            os.mkdir(folder_path)

# Move files to the appropriate folder based on their extensions.
def organize_files():
    for file in os.listdir(download_folder):
        file_path = os.path.join(download_folder, file)

        # Ignore folders and only handle files.
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1].lower()

            # Find which category the file belongs to.
            for category, extensions in file_categories.items():
                if file_extension in extensions:
                    destination = os.path.join(download_folder, category)
                    print(f"Moving {file} to {destination}")
                    shutil.move(file_path, destination)
                    break

if __name__ == "__main__":
    print("Starting the file organization process...")

    # Step 1: Set up folders.
    setup_folders()

    # Step 2: Move files to their respective folders.
    organize_files()

    print("All files have been organized!")

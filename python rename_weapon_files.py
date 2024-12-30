import os

def rename_images_in_directory(directory_path):
    """
    Renames all image files in the specified directory if their extension is `.PNG`.
    The extension is changed to `.png`.

    :param directory_path: The path of the directory to scan.
    """
    try:
        # List all files in the directory
        files = os.listdir(directory_path)

        for file_name in files:
            # Check if the file ends with '.PNG'
            if file_name.endswith('.PNG'):
                # Construct full file paths
                old_file_path = os.path.join(directory_path, file_name)
                new_file_name = file_name[:-4] + '.png'
                new_file_path = os.path.join(directory_path, new_file_name)

                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {file_name} -> {new_file_name}")

    except FileNotFoundError:
        print("Error: Directory not found. Please provide a valid path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = r"C:/Users/User/Documents/GitHub/image/items"  # Replace this with your directory path
rename_images_in_directory(directory_path)

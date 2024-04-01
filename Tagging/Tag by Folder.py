import os
from mutagen.id3 import ID3, TCON, TIT2

# Function to set genre and title for all MP3 files in a folder and its subfolders
def set_genre_and_title_in_folders(root_folder):
    for folder_path, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".mp3"):
                file_path = os.path.join(folder_path, filename)
                folder_name = os.path.basename(folder_path)
                try:
                    audio = ID3(file_path)
                    audio["TCON"] = TCON(encoding=3, text=folder_name)
                    
                    # Remove ".mp3" from the filename and set it as the Title
                    title = os.path.splitext(filename)[0]
                    audio["TIT2"] = TIT2(encoding=3, text=title)
                    
                    audio.save()
                    print(f"Genre and Title set for {filename} in folder {folder_name}")
                except Exception as e:
                    print(f"Error setting Genre and Title for {filename}: {str(e)}")

# Specify the root folder where you want to start tagging genres and titles
root_folder = "."  # You can change this to the desired root folder

# Call the function to set genres and titles in all folders and subfolders
set_genre_and_title_in_folders(root_folder)

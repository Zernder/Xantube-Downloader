import os
from mutagen.id3 import ID3, TCON
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Function to set genre for all MP3 files in a folder
def set_genre(folder_path, genre, progress_var):
    mp3_files = [filename for filename in os.listdir(folder_path) if filename.endswith(".mp3")]
    total_files = len(mp3_files)

    for index, filename in enumerate(mp3_files):
        file_path = os.path.join(folder_path, filename)
        try:
            audio = ID3(file_path)
            audio["TCON"] = TCON(encoding=3, text=genre)
            audio.save()
            progress_var.set((index + 1) / total_files * 100)  # Update progress bar
            progress_bar.update()
        except Exception as e:
            print(f"Error setting genre for {filename}: {str(e)}")

# Function to choose a folder using a file dialog
def choose_folder():
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_path)

# Function to start the genre setting process
def start_process():
    folder_path = folder_path_entry.get()
    genre = genre_entry.get()
    if folder_path and genre:
        set_genre(folder_path, genre, progress_var)
        tk.messagebox.showinfo("Complete", "Genre setting process completed.")
    else:
        tk.messagebox.showerror("Error", "Please provide a folder path and genre.")

# Create the main window
root = tk.Tk()
root.title("MP3 Genre Setter")

# Create and configure the progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.grid(row=0, column=0, columnspan=2, pady=10)

# Label and entry for folder path
folder_label = tk.Label(root, text="Folder Path:")
folder_label.grid(row=1, column=0, padx=10, pady=5)
folder_path_entry = tk.Entry(root)
folder_path_entry.grid(row=1, column=1, padx=10, pady=5)

# Button to choose folder
choose_folder_button = tk.Button(root, text="Choose Folder", command=choose_folder)
choose_folder_button.grid(row=1, column=2, padx=10, pady=5)

# Label and entry for genre
genre_label = tk.Label(root, text="Genre:")
genre_label.grid(row=2, column=0, padx=10, pady=5)
genre_entry = tk.Entry(root)
genre_entry.grid(row=2, column=1, padx=10, pady=5)

# Button to start the process
start_button = tk.Button(root, text="Start", command=start_process)
start_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the GUI application
root.mainloop()

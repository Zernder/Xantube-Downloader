import yt_dlp
import os
import threading
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

ydl_opts = {
    'format': 'best',
    'outtmpl': './Media/%(title)s.%(ext)s',
}


def on_click():
    url = url_entry.get()
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("URL:", url)

root = tk.Tk()
root.title("Tamaki's Download Manager")

root.geometry("800x400")
root.resizable(False, False)

# Load background image
background_image = Image.open("Data\\background.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Text Entry for URL
url_label = tk.Label(root, text="Enter URL: ", font=("Helvetica", 16))
url_label.place(relx=0.4, rely=0.1)
url_entry = tk.Entry(root, font=("Helvetica", 14), width=20)
url_entry.place(relx=0.4, rely=0.2)

# Dropdown menu for file type
# file_type_label = tk.Label(root, text="File Type:", font=("Helvetica", 16))
# file_type_label.place(relx=0.4, rely=0.4)
# file_type_var = tk.StringVar()
# file_type_dropdown = ttk.Combobox(root, textvariable=file_type_var, values=[".mp3", ".webm"], font=("Helvetica", 16), width=2)
# file_type_dropdown.place(relx=0.4, rely=0.5, relwidth=0.25)
# file_type_dropdown.current(0)
# file_type_dropdown.current(0)

download_button = tk.Button(root, text="Start", command=on_click, width=15, height=2, bg="Purple", fg="Black", font=("Helvetica", 16, "bold"))
download_button.place(relx=0.53, rely=0.8, anchor="center")


root.mainloop()

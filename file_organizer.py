import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue") 

file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Applications": [".exe", ".msi", ".bat"],
    "Sounds": [".mp3", ".m4a"]
}

def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            for folder, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(folder_path, folder)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    break  

def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        organize_folder(folder)
        messagebox.showinfo("✅ Done", f"Files organized in:\n{folder}")

app = ctk.CTk()
app.title("File Organizer - by IxHazm")
app.geometry("500x150")

ctk.CTkLabel(app, text="Organize your folder", font=("Arial", 18)).pack(pady=(20, 10))

choose_button = ctk.CTkButton(app, text="Choose Folder", command=choose_folder, width=240, height=40)
choose_button.pack(pady=(0, 10))

app.mainloop()

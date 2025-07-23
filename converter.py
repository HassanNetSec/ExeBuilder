import os
import subprocess
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Set theme
ctk.set_appearance_mode("System")  # Options: "Light", "Dark", "System"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

# Main App
app = ctk.CTk()
app.title("Python to EXE Converter")
app.geometry("750x600")
app.grid_columnconfigure(0, weight=1)

# Variables
py_file_var = ctk.StringVar()
output_folder_var = ctk.StringVar()
onefile_var = ctk.BooleanVar()
console_var = ctk.BooleanVar()
windowed_var = ctk.BooleanVar()

# Helpers
def verify_path(path):
    return os.path.exists(path)

def create_folder(foldername):
    if not os.path.exists(foldername):
        os.makedirs(foldername)

def browse_py_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if file_path:
        py_file_var.set(file_path)

def browse_output_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_folder_var.set(folder_path)

def run_pyinstaller():
    command = ["pyinstaller"]

    if onefile_var.get():
        command.append("--onefile")
    if console_var.get():
        command.append("--console")
    if windowed_var.get():
        command.append("--windowed")  # --noconsole

    py_file = py_file_var.get()
    output_folder = output_folder_var.get()

    if not verify_path(py_file):
        messagebox.showerror("Error", "Python file does not exist.")
        return

    if not output_folder:
        messagebox.showerror("Error", "Please select an output folder.")
        return

    create_folder(output_folder)
    command.append(f"--distpath={output_folder}")
    command.append(py_file)

    output_textbox.delete("0.0", "end")
    output_textbox.insert("end", f"Running command: {' '.join(command)}\n\n")

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            output_textbox.insert("end", line)
            output_textbox.see("end")
        process.wait()
    except Exception as e:
        output_textbox.insert("end", f"Error: {str(e)}")

# UI Layout
ctk.CTkLabel(app, text="Python File Path:").grid(row=0, column=0, sticky="w", padx=10, pady=(20, 5))
frame1 = ctk.CTkFrame(app, fg_color="transparent")
frame1.grid(row=1, column=0, padx=10, sticky="we")
frame1.grid_columnconfigure(0, weight=1)

ctk.CTkEntry(frame1, textvariable=py_file_var).grid(row=0, column=0, sticky="we", padx=(0, 10))
ctk.CTkButton(frame1, text="Browse", command=browse_py_file).grid(row=0, column=1)

ctk.CTkLabel(app, text="Output Folder:").grid(row=2, column=0, sticky="w", padx=10, pady=(20, 5))
frame2 = ctk.CTkFrame(app, fg_color="transparent")
frame2.grid(row=3, column=0, padx=10, sticky="we")
frame2.grid_columnconfigure(0, weight=1)

ctk.CTkEntry(frame2, textvariable=output_folder_var).grid(row=0, column=0, sticky="we", padx=(0, 10))
ctk.CTkButton(frame2, text="Browse", command=browse_output_folder).grid(row=0, column=1)

ctk.CTkLabel(app, text="PyInstaller Options:").grid(row=4, column=0, sticky="w", padx=10, pady=(20, 5))
options_frame = ctk.CTkFrame(app, fg_color="transparent")
options_frame.grid(row=5, column=0, sticky="w", padx=10)
ctk.CTkCheckBox(options_frame, text="--onefile", variable=onefile_var).grid(row=0, column=0, padx=10)
ctk.CTkCheckBox(options_frame, text="--console", variable=console_var).grid(row=0, column=1, padx=10)
ctk.CTkCheckBox(options_frame, text="--windowed (--noconsole)", variable=windowed_var).grid(row=0, column=2, padx=10)

ctk.CTkButton(app, text="Convert to EXE", command=run_pyinstaller, fg_color="green", hover_color="#006400", text_color="white").grid(row=6, column=0, pady=20)

ctk.CTkLabel(app, text="Output Log:").grid(row=7, column=0, sticky="w", padx=10, pady=(5, 5))
output_textbox = ctk.CTkTextbox(app, height=200)
output_textbox.grid(row=8, column=0, padx=10, pady=(0, 10), sticky="nsew")
app.grid_rowconfigure(8, weight=1)

app.mainloop()

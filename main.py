import os 
from tkinter import filedialog
import subprocess

name = input("Name of the .command file:")
venv_name = input("Name of the virtual environment (leave blank if none):")

file_path = filedialog.askopenfilename(title="Select your file", initialdir="/", filetypes=[("Python scripts", "*.py"), ("All files", "*.*")])

with open(f"{name}.command", "w") as f:
    f.write("#!/bin/bash\n")
    if venv_name:
        f.write(f"source {venv_name}/bin/activate\n")
    f.write(f"python3 {file_path}\n")
    subprocess.run(["chmod", "+x", f"{name}.command"])
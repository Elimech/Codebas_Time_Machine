import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from App.Logic.CTM import build_Z
from App.Logic.Agent import analyze_commit
import threading
import os
import sys
from git import Repo, InvalidGitRepositoryError


def resource_path(relative_path):
    """Obtiene la ruta correcta tanto en .py como en .exe"""
    try:
        base_path = sys._MEIPASS  # PyInstaller
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# ======================
# Window
# ======================
root = tk.Tk()
root.title("Codebase Time Machine")
root.iconbitmap(resource_path("Icon.ico"))
root.geometry("900x650")
root.configure(bg="#1e1e1e")

# ======================
# Variables
# ======================
path_var = tk.StringVar()

# ======================
# Functions
# ======================


def select_repo():
    folder = filedialog.askdirectory()
    if folder:
        path_var.set(folder)


def reset_app():
    path_var.set("")
    output.delete("1.0", "end")
    progress.stop()
    progress.pack_forget()


def validate_repo(path):
    try:
        Repo(path)
        return True
    except InvalidGitRepositoryError:
        return False
    except Exception:
        return False


def run_analysis():
    repo = path_var.get()

    if not repo:
        root.after(0, lambda: messagebox.showwarning(
            "Warning", "Select a repository first"))
        return

    if not validate_repo(repo):
        root.after(0, lambda: messagebox.showerror(
            "Error", "Selected folder is not a valid Git repository"))
        return

    root.after(0, start_progress)
    root.after(0, lambda: output.insert("end", "Analysis started...\n\n"))

    Z = build_Z(repo)

    for i, commit in enumerate(Z):
        result = analyze_commit(commit)
        if not result:
            result = "[Analysis failed]"

        root.after(
            0,
            lambda i=i, r=result: output.insert(
                "end", f"\n=== Commit {i + 1} ===\n{r}\n"
            )
        )

    root.after(0, stop_progress)


def start_analysis():
    threading.Thread(target=run_analysis, daemon=True).start()


def start_progress():
    progress.pack(fill="x", padx=20, pady=10)
    progress.start(10)


def stop_progress():
    progress.stop()


# ======================
# UI – Top
# ======================
tk.Label(
    root, text="Git Repository",
    bg="#1e1e1e", fg="white", font=("Segoe UI", 12, "bold")
).pack(pady=(10, 5))

path_frame = tk.Frame(root, bg="#1e1e1e")
path_frame.pack(fill="x", padx=20)

tk.Entry(
    path_frame, textvariable=path_var,
    bg="#2d2d2d", fg="white", insertbackground="white",
    relief="flat", font=("Consolas", 10)
).pack(side="left", fill="x", expand=True, padx=(0, 10))

tk.Button(
    path_frame, text="Browse",
    command=select_repo, bg="#3a3d41", fg="white",
    relief="flat"
).pack(side="right")

# ======================
# Progress Bar
# ======================
progress = ttk.Progressbar(
    root, mode="indeterminate"
)

# ======================
# Output
# ======================
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(fill="both", expand=True, padx=20, pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

output = tk.Text(
    frame, yscrollcommand=scrollbar.set,
    bg="#252526", fg="#d4d4d4",
    insertbackground="white",
    wrap="word", font=("Consolas", 10),
    relief="flat"
)
output.pack(side="left", fill="both", expand=True)
scrollbar.config(command=output.yview)

# ======================
# Buttons
# ======================
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame, text="Analyze Repo",
    command=start_analysis,
    bg="#FF0000", fg="white",
    relief="flat", width=15
).pack(side="left", padx=10)

tk.Button(
    btn_frame, text="Reset",
    command=reset_app,
    bg="#3a3d41", fg="white",
    relief="flat", width=10
).pack(side="left")

# ======================
root.mainloop()

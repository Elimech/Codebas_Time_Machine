# Codebase Time Machine

**Codebase Time Machine** is a desktop application that analyzes the
full history of a Git repository and uses **AI-powered semantic
reasoning** to explain *why* changes happened --- not just *what*
changed.

Instead of raw diffs, the app interprets commits as **design
decisions**, **feature evolution**, and **architectural intent**.

------------------------------------------------------------------------

## ✨ Features

-   📂 Select any local Git repository
-   🧠 AI-powered semantic commit analysis (Google Gemini)
-   📜 Commit-by-commit explanations
-   🧩 Detects:
    -   Feature additions
    -   Refactors
    -   Architectural changes
    -   Version evolution (X.Y.Z)
-   🖥️ Desktop GUI built with **Tkinter**
-   🚀 Standalone `.exe` version (no Python required)

------------------------------------------------------------------------

## 🧠 How It Works

1.  The app reads the Git commit history (The Git Repo must be a cloned one)
2.  For each commit, it extracts:
    -   Author
    -   Date
    -   Commit message
    -   File stats
    -   Cleaned diffs
3.  Each commit is sent **one at a time** to Gemini
4.  The AI analyzes:
    -   Developer intent
    -   Type of change
    -   Impact level
    -   Project direction

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python 3.11+
-   Tkinter (GUI)
-   GitPython
-   Google Gemini API
-   PyInstaller

------------------------------------------------------------------------

## 📁 Project Structure

    Machine/
    │
    ├── Icon.ico
    │
    └── App/
        ├── GitTimeMachine.py
        ├── Logic/
        │   ├── CTM.py
        │   ├── Agent.py
        │   └── __init__.py
        ├── Files/
        │   ├── Interface.py
        │   └── __init__.py
        └── __init__.py

------------------------------------------------------------------------

## 🔐 Gemini API Key Setup

The application reads the Gemini API key from an environment variable.

### Get an API Key

https://aistudio.google.com/app/apikey

### Windows (PowerShell)

``` powershell
setx GEMINI_API_KEY "YOUR_API_KEY_HERE"
```

Restart your session after setting it.

### Linux / macOS

``` bash
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

------------------------------------------------------------------------

## ▶️ Run the App

``` bash
python -m App.GitTimeMachine
```

------------------------------------------------------------------------

## 📦 Build EXE

``` powershell
pyinstaller --onefile --windowed --name GitTimeMachine --icon Icon.ico App/GitTimeMachine.py
```

The executable will appear in the `dist/` folder.

------------------------------------------------------------------------

## 📜 License

Educational and experimental use.

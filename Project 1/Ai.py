"""
╔══════════════════════════════════════════════════════════╗
║         FILE MANAGEMENT SYSTEM — CLI Based               ║
║         Built with Python File Handling Concepts         ║
╚══════════════════════════════════════════════════════════╝

Modules Used  : os, pathlib
Operations    : Create, Read, Update (Rename / Overwrite / Append), Delete
Author        : Ai.py (Project 1)
"""

import os
from pathlib import Path

# ─────────────────────────────────────────────
#  Working Directory — only this folder is used
# ─────────────────────────────────────────────
WORKSPACE = Path(__file__).parent   # folder where Ai.py lives


# ══════════════════════════════════════════════
#  HELPER UTILITIES
# ══════════════════════════════════════════════

def separator(char="─", width=55):
    """Print a visual separator line."""
    print(char * width)


def header(title: str):
    """Print a styled section header."""
    separator("═")
    print(f"  {title}")
    separator("═")


def pause():
    """Wait for user to press Enter before continuing."""
    input("\n  [Press Enter to continue...]")


# ══════════════════════════════════════════════
#  1. DISPLAY FILES AND FOLDERS
# ══════════════════════════════════════════════

def read_file_and_folder():
    """
    Display all files and folders present in the workspace directory
    with serial numbers for easy identification.
    """
    header("📂  WORKSPACE — Current Directory")
    print(f"  Location : {WORKSPACE}\n")

    items = sorted(WORKSPACE.iterdir())          # get all items

    files   = [item for item in items if item.is_file()]
    folders = [item for item in items if item.is_dir()]

    # ── Files ──────────────────────────────────
    print("  📄  FILES")
    separator()
    if files:
        for idx, f in enumerate(files, start=1):
            size = f.stat().st_size
            print(f"  {idx:>3}.  {f.name:<35}  ({size} bytes)")
    else:
        print("  No files found.")

    print()

    # ── Folders ────────────────────────────────
    print("  📁  FOLDERS")
    separator()
    if folders:
        for idx, d in enumerate(folders, start=1):
            print(f"  {idx:>3}.  {d.name}")
    else:
        print("  No folders found.")

    separator()


# ══════════════════════════════════════════════
#  2. CREATE FILE
# ══════════════════════════════════════════════

def create_file():
    """
    Create a new file in the workspace.
    - Prompts for file name and optional initial content.
    - Validates: name not empty, file should not already exist.
    """
    header("➕  CREATE FILE")

    # ── Get file name ──────────────────────────
    file_name = input("  Enter file name (with extension): ").strip()

    if not file_name:
        print("\n  ❌  Error: File name cannot be empty.")
        pause()
        return

    target = WORKSPACE / file_name

    if target.exists():
        print(f"\n  ⚠️   File Already Exists — '{file_name}'")
        pause()
        return

    # ── Optional content ───────────────────────
    print("  Enter initial content (leave blank to create an empty file):")
    print("  (Type your content and press Enter twice to finish)")
    lines = []
    try:
        while True:
            line = input()
            if line == "" and lines and lines[-1] == "":
                break
            lines.append(line)
    except EOFError:
        pass

    content = "\n".join(lines).rstrip()

    # ── Write file ─────────────────────────────
    try:
        with open(target, "w", encoding="utf-8") as fp:
            fp.write(content)
        print(f"\n  ✅  File Created Successfully — '{file_name}'")
    except PermissionError:
        print(f"\n  ❌  Permission Denied: Cannot create '{file_name}'.")
    except OSError as e:
        print(f"\n  ❌  Unexpected Error: {e}")

    pause()


# ══════════════════════════════════════════════
#  3. READ FILE
# ══════════════════════════════════════════════

def read_file():
    """
    Display the full contents of an existing file.
    - Validates: file must exist and must be a file (not a folder).
    """
    header("📖  READ FILE")

    file_name = input("  Enter file name to read: ").strip()

    if not file_name:
        print("\n  ❌  Error: File name cannot be empty.")
        pause()
        return

    target = WORKSPACE / file_name

    if not target.exists() or not target.is_file():
        print(f"\n  ❌  File Does Not Exist — '{file_name}'")
        pause()
        return

    # ── Display content ────────────────────────
    try:
        with open(target, "r", encoding="utf-8") as fp:
            content = fp.read()

        separator()
        print(f"  📄  Contents of '{file_name}':\n")
        if content:
            print(content)
        else:
            print("  (File is empty)")
        separator()

    except PermissionError:
        print(f"\n  ❌  Permission Denied: Cannot read '{file_name}'.")
    except UnicodeDecodeError:
        print(f"\n  ❌  Encoding Error: Cannot read '{file_name}' as UTF-8 text.")
    except OSError as e:
        print(f"\n  ❌  Unexpected Error: {e}")

    pause()


# ══════════════════════════════════════════════
#  4. UPDATE FILE  (Rename / Overwrite / Append)
# ══════════════════════════════════════════════

def _rename_file(target: Path):
    """Sub-operation: Rename an existing file."""
    new_name = input("  Enter new file name (with extension): ").strip()

    if not new_name:
        print("\n  ❌  Error: New name cannot be empty.")
        return

    new_target = WORKSPACE / new_name

    if new_target.exists():
        print(f"\n  ⚠️   A file named '{new_name}' already exists.")
        return

    try:
        target.rename(new_target)
        print(f"\n  ✅  File Updated Successfully — renamed to '{new_name}'")
    except PermissionError:
        print(f"\n  ❌  Permission Denied: Cannot rename '{target.name}'.")
    except OSError as e:
        print(f"\n  ❌  Unexpected Error: {e}")


def _overwrite_file(target: Path):
    """Sub-operation: Overwrite (replace) full content of a file."""
    print("  Enter new content (press Enter twice when done):")
    lines = []
    try:
        while True:
            line = input()
            if line == "" and lines and lines[-1] == "":
                break
            lines.append(line)
    except EOFError:
        pass

    content = "\n".join(lines).rstrip()

    try:
        with open(target, "w", encoding="utf-8") as fp:
            fp.write(content)
        print(f"\n  ✅  File Updated Successfully — content overwritten.")
    except PermissionError:
        print(f"\n  ❌  Permission Denied: Cannot write to '{target.name}'.")
    except OSError as e:
        print(f"\n  ❌  Unexpected Error: {e}")


def _append_file(target: Path):
    """Sub-operation: Append new content at the end of the file."""
    print("  Enter content to append (press Enter twice when done):")
    lines = []
    try:
        while True:
            line = input()
            if line == "" and lines and lines[-1] == "":
                break
            lines.append(line)
    except EOFError:
        pass

    content = "\n".join(lines).rstrip()

    try:
        with open(target, "a", encoding="utf-8") as fp:
            fp.write("\n" + content)
        print(f"\n  ✅  File Updated Successfully — content appended.")
    except PermissionError:
        print(f"\n  ❌  Permission Denied: Cannot append to '{target.name}'.")
    except OSError as e:
        print(f"\n  ❌  Unexpected Error: {e}")


def update_file():
    """
    Modify an existing file with one of three sub-operations:
      4.1 Rename File
      4.2 Overwrite Content
      4.3 Append Content
    """
    header("✏️   UPDATE FILE")

    file_name = input("  Enter file name to update: ").strip()

    if not file_name:
        print("\n  ❌  Error: File name cannot be empty.")
        pause()
        return

    target = WORKSPACE / file_name

    if not target.exists() or not target.is_file():
        print(f"\n  ❌  File Does Not Exist — '{file_name}'")
        pause()
        return

    # ── Sub-menu ───────────────────────────────
    print(f"\n  File found: '{file_name}'")
    separator()
    print("  What would you like to do?")
    print("    1.  Rename File")
    print("    2.  Overwrite Content")
    print("    3.  Append Content")
    separator()

    choice = input("  Enter choice (1-3): ").strip()

    if choice == "1":
        _rename_file(target)
    elif choice == "2":
        _overwrite_file(target)
    elif choice == "3":
        _append_file(target)
    else:
        print("\n  ❌  Invalid choice. Returning to main menu.")

    pause()


# ══════════════════════════════════════════════
#  5. DELETE FILE
# ══════════════════════════════════════════════

def delete_file():
    """
    Remove an existing file from the workspace.
    - Validates: file must exist and must be a file.
    - Asks for confirmation before deletion.
    """
    header("🗑️   DELETE FILE")

    file_name = input("  Enter file name to delete: ").strip()

    if not file_name:
        print("\n  ❌  Error: File name cannot be empty.")
        pause()
        return

    target = WORKSPACE / file_name

    if not target.exists() or not target.is_file():
        print(f"\n  ❌  No Such File Exists — '{file_name}'")
        pause()
        return

    # ── Confirmation ───────────────────────────
    confirm = input(f"\n  ⚠️   Are you sure you want to delete '{file_name}'? (yes/no): ").strip().lower()

    if confirm not in ("yes", "y"):
        print("\n  Deletion cancelled.")
        pause()
        return

    try:
        target.unlink()
        print(f"\n  ✅  File Removed Successfully — '{file_name}'")
    except PermissionError:
        print(f"\n  ❌  Permission Denied: Cannot delete '{file_name}'.")
    except OSError as e:
        print(f"\n  ❌  Unexpected Error: {e}")

    pause()


# ══════════════════════════════════════════════
#  MAIN MENU
# ══════════════════════════════════════════════

def main_menu():
    """Display the interactive main menu and route user choices."""
    while True:
        os.system("cls" if os.name == "nt" else "clear")   # clear screen

        # ── Banner ─────────────────────────────
        print()
        print("  ╔══════════════════════════════════════════════════╗")
        print("  ║       📂  FILE MANAGEMENT SYSTEM  📂             ║")
        print("  ║          CLI Based | Python Project              ║")
        print("  ╚══════════════════════════════════════════════════╝")
        print()

        # ── Show current files ──────────────────
        read_file_and_folder()
        print()

        # ── Menu options ───────────────────────
        print("  ┌─────────────────────────────────┐")
        print("  │           OPERATIONS            │")
        print("  ├─────────────────────────────────┤")
        print("  │  1.  ➕  Create File             │")
        print("  │  2.  📖  Read File               │")
        print("  │  3.  ✏️   Update File             │")
        print("  │  4.  🗑️   Delete File             │")
        print("  │  5.  🚪  Exit                    │")
        print("  └─────────────────────────────────┘")
        print()

        choice = input("  Enter your choice (1-5): ").strip()

        if choice == "1":
            create_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            update_file()
        elif choice == "4":
            delete_file()
        elif choice == "5":
            print("\n  👋  Goodbye! Exiting File Management System.\n")
            break
        else:
            print("\n  ❌  Invalid Input — Please enter a number between 1 and 5.")
            pause()


# ══════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════

if __name__ == "__main__":
    main_menu()

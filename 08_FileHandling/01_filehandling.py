"""A hands-on tour of Python file handling.

The examples create files inside a temporary directory and clean them up at the
end, so running the tour does not leave practice files in the current folder.
"""

import csv
import json
import tempfile
from pathlib import Path


def main():
    print("=" * 68)
    print("PYTHON FILE HANDLING: A HANDS-ON TOUR")
    print("=" * 68)

    # Use a temporary folder so the examples are safe to rerun.
    with tempfile.TemporaryDirectory() as temporary_folder:
        folder = Path(temporary_folder)
        notes_path = folder / "notes.txt"

        # 1. Write text. Mode 'w' creates or replaces the file.
        print("\n1. WRITING TEXT")
        with notes_path.open("w", encoding="utf-8") as file:
            file.write("Python file handling\n")
            file.write("Files keep data between program runs.\n")
        print(f"Created file: {notes_path.name}")

        # 2. Read the whole file as one string.
        print("\n2. READING THE WHOLE FILE")
        with notes_path.open(encoding="utf-8") as file:
            contents = file.read()
        print(contents, end="")

        # 3. Append adds to the existing contents instead of replacing them.
        print("\n3. APPENDING TEXT")
        with notes_path.open("a", encoding="utf-8") as file:
            file.write("A third line was appended.\n")
        with notes_path.open(encoding="utf-8") as file:
            for line in file:
                print(line.rstrip("\n"))

        # 4. pathlib helps inspect and create paths.
        print("\n4. PATH INFORMATION")
        print(f"File name: {notes_path.name}")
        print(f"Suffix: {notes_path.suffix}")
        print(f"Exists? {notes_path.exists()}")
        print(f"Is a file? {notes_path.is_file()}")

        # 5. Catch a common error with a specific handler.
        print("\n5. HANDLING A MISSING FILE")
        missing_path = folder / "missing.txt"
        try:
            with missing_path.open(encoding="utf-8") as file:
                file.read()
        except FileNotFoundError:
            print(f"Could not find {missing_path.name}; continuing safely.")

        # 6. Write and read JSON (structured Python data as text).
        print("\n6. JSON")
        progress_path = folder / "progress.json"
        progress = {"Strings": "complete", "File Handling": "in progress"}
        with progress_path.open("w", encoding="utf-8") as file:
            json.dump(progress, file, indent=2)
        with progress_path.open(encoding="utf-8") as file:
            loaded_progress = json.load(file)
        print(f"Loaded JSON data: {loaded_progress}")

        # 7. Write and read CSV with the csv module.
        print("\n7. CSV")
        csv_path = folder / "progress.csv"
        rows = [
            ["topic", "status"],
            ["Strings", "complete"],
            ["Lists", "in progress"],
        ]
        with csv_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        with csv_path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

        print("\nPractice files are in a temporary folder and will be cleaned up now.")

    print("\n" + "=" * 68)
    print("TOUR COMPLETE — try changing the text and structured data examples.")
    print("=" * 68)


if __name__ == "__main__":
    main()

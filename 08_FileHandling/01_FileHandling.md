# Python File Handling

> **A visual, beginner-friendly deep dive into working with files in Python**  
> Learn to read, write, append, navigate paths, and handle common file problems safely.

---

## The one-minute picture

A file lets a program keep information after it stops running. Python opens a file, performs an operation, and then closes it. The safest everyday pattern is a `with` block, which closes the file automatically.

```mermaid
flowchart LR
    A[Choose a path and mode] --> B[Open file]
    B --> C[Read or write]
    C --> D[with block ends]
    D --> E[File closes automatically]
```

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

Think of `with` as borrowing a file handle for a clearly marked stretch of code: Python gives it to you at the start and tidies it up at the end, even if an error occurs.

---

## 1. Paths: where is the file?

A **path** identifies a file's location. A relative path is interpreted from the program's current working directory; an absolute path starts from the filesystem root.

```text
project/
├── main.py
└── data/
    └── notes.txt
```

If the program runs with `project/` as its working directory, the relative path is `data/notes.txt`.

The current working directory is not necessarily the folder where the Python file lives. Inspect it with `Path.cwd()`:

```python
from pathlib import Path
print(Path.cwd())
```

### Prefer `pathlib` for building paths

`pathlib.Path` joins path pieces in a platform-friendly way:

```python
from pathlib import Path

data_folder = Path("data")
notes_path = data_folder / "notes.txt"
print(notes_path)  # data/notes.txt on many systems
```

To build a path relative to the current Python file, use `__file__`:

```python
from pathlib import Path

project_folder = Path(__file__).resolve().parent
notes_path = project_folder / "data" / "notes.txt"
```

This is more predictable than assuming the program was launched from a particular directory.

---

## 2. Opening a file with `open()`

The general shape is:

```python
open(path, mode, encoding=...)
```

Common text modes:

| Mode | Meaning |
|---|---|
| `"r"` | Read; file must already exist |
| `"w"` | Write from scratch; creates file or **replaces existing contents** |
| `"a"` | Append to the end; creates file if needed |
| `"x"` | Create a new file; fail if it already exists |

For text files, specify an encoding such as UTF-8:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    contents = file.read()
```

If the encoding is omitted, Python uses a platform-dependent default. Explicit UTF-8 makes text handling more consistent across computers.

### Binary mode

Add `"b"` to a mode to read or write raw bytes—for example, `"rb"` for reading an image. Binary data is not decoded text, so do not supply a text encoding.

```python
with open("picture.png", "rb") as file:
    image_data = file.read()
```

---

## 3. Why `with` is important

A file should be closed when you finish with it. A `with` statement manages this automatically, including when an exception occurs inside the block.

```python
with open("notes.txt", encoding="utf-8") as file:
    contents = file.read()

# The file is closed here.
```

Without `with`, you would need to call `file.close()` yourself and ensure it happens on every path. For everyday file work, use `with open(...)`.

---

## 4. Reading text files

### Read the entire file

`read()` returns the remaining file contents as one string.

```python
with open("notes.txt", encoding="utf-8") as file:
    contents = file.read()
```

This is convenient for small files. A very large file may use too much memory if loaded all at once.

### Read one line at a time

Loop over the file to process each line without loading the entire file into memory first.

```python
with open("notes.txt", encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())  # remove line-ending whitespace for display
```

Each line usually includes its newline character. `rstrip("\n")` removes only newline characters; `.strip()` removes whitespace from both ends, which may also remove meaningful spaces.

### Read all lines into a list

```python
with open("notes.txt", encoding="utf-8") as file:
    lines = file.readlines()
```

For most line-by-line processing, `for line in file` is simpler and more memory-efficient than `readlines()`.

---

## 5. Writing and appending text

### Write from scratch

Mode `"w"` creates a file if necessary and replaces its contents if it already exists. Be sure that replacement is what you intend.

```python
with open("summary.txt", "w", encoding="utf-8") as file:
    file.write("Python file handling\n")
    file.write("Files keep data between runs.\n")
```

`write()` does not add a newline automatically. Include `\n` when you want the next text on a new line.

### Append to an existing file

Mode `"a"` writes at the end instead of replacing the existing contents.

```python
with open("summary.txt", "a", encoding="utf-8") as file:
    file.write("This line was added later.\n")
```

### Write a collection of lines

`writelines()` writes each string as-is; it does not insert line breaks for you.

```python
lines = ["Strings\n", "Lists\n", "Files\n"]
with open("topics.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)
```

---

## 6. File position and reading in steps

A file object keeps track of the current position. After reading, the position moves forward.

```python
with open("notes.txt", encoding="utf-8") as file:
    first_part = file.read(5)  # read up to five characters
    rest = file.read()         # read the remaining text
```

For simple text processing, reading a file once or looping over its lines is usually enough. Methods such as `seek()` and `tell()` give more control over a file position, but are more common in specialized tasks.

---

## 7. Safe paths and folders with `pathlib`

Use `Path` methods to inspect and manage paths:

```python
from pathlib import Path

path = Path("data") / "notes.txt"
print(path.exists())  # Does this path exist?
print(path.is_file()) # Is it a file?
print(path.name)      # notes.txt
print(path.suffix)    # .txt
```

Create a folder and any missing parent folders with:

```python
Path("output/reports").mkdir(parents=True, exist_ok=True)
```

`exist_ok=True` means Python should not raise an error if the directory already exists.

---

## 8. Handling common file exceptions

File operations may fail because a file is missing, permission is denied, or a path points to the wrong kind of object. Handle the errors you expect and can respond to.

```python
from pathlib import Path

path = Path("notes.txt")
try:
    with path.open(encoding="utf-8") as file:
        contents = file.read()
except FileNotFoundError:
    print(f"Could not find {path}.")
except PermissionError:
    print(f"You do not have permission to read {path}.")
else:
    print(contents)
```

Common exceptions:

- `FileNotFoundError`: the path does not identify an existing file;
- `PermissionError`: the process is not allowed to access it;
- `IsADirectoryError`: code tried to open a directory as a file;
- `UnicodeDecodeError`: bytes in the file do not match the chosen text encoding.

Avoid a bare `except:` around file operations. It can hide programming mistakes unrelated to the file.

---

## 9. Structured text: JSON

JSON is a common format for structured data. Python's `json` module converts between Python dictionaries/lists and JSON text.

### Write JSON

```python
import json

progress = {"Strings": "complete", "Lists": "in progress"}
with open("progress.json", "w", encoding="utf-8") as file:
    json.dump(progress, file, indent=2)
```

### Read JSON

```python
import json

with open("progress.json", encoding="utf-8") as file:
    progress = json.load(file)
```

`dump`/`load` work with files. `dumps`/`loads` work with JSON strings.

```python
json_text = json.dumps(progress)
restored = json.loads(json_text)
```

JSON supports common data types such as objects (Python dictionaries), arrays (lists), strings, numbers, booleans, and `null` (`None` in Python). It does not preserve arbitrary Python objects automatically.

---

## 10. Structured text: CSV

CSV stores rows and columns as text. Use the `csv` module rather than splitting each row on commas by hand: quoted fields may themselves contain commas.

```python
import csv

rows = [
    ["topic", "status"],
    ["Strings", "complete"],
    ["Lists", "in progress"],
]

with open("progress.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
```

Read rows back:

```python
with open("progress.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

`newline=""` is the recommended setting for CSV files so the CSV module can handle newline details consistently.

For named columns, `csv.DictWriter` and `csv.DictReader` work with dictionaries.

---

## 11. Temporary and safe writing practices

For important files, overwriting the only copy can be risky. A common safer approach is to write a new temporary file, then replace the original after writing succeeds. For more complex needs, Python provides tools such as `tempfile` and `pathlib.Path.replace()`.

Also consider:

- use `"x"` when you want to ensure a new file is not overwritten;
- use `"a"` when you intentionally want to preserve earlier contents;
- keep user-provided filenames within the intended output directory;
- do not assume a path is safe merely because it is a string.

---

## 12. A practical mini-project: save and load a topic tracker

This example stores a small dictionary as JSON so it can be used again later.

```python
import json
from pathlib import Path

progress_path = Path("study_progress.json")
progress = {
    "Strings": "complete",
    "Lists": "complete",
    "File Handling": "in progress",
}

# Save structured data as readable JSON.
with progress_path.open("w", encoding="utf-8") as file:
    json.dump(progress, file, indent=2)

# Load the saved JSON back into a Python dictionary.
with progress_path.open(encoding="utf-8") as file:
    loaded_progress = json.load(file)

print(loaded_progress)
```

The file contains readable text similar to:

```json
{
  "Strings": "complete",
  "Lists": "complete",
  "File Handling": "in progress"
}
```

The example writes in the current working directory. In a real project, choose a deliberate location and consider what should happen if the file is missing or invalid.

---

## 13. Common file-handling mistakes

### Forgetting `encoding="utf-8"`

The default encoding can vary by system. Specify an encoding for text files.

### Using `"w"` when you meant `"a"`

`"w"` replaces existing contents. Use `"a"` to append.

### Forgetting newline characters

`write()` and `writelines()` do not add `\n` automatically.

### Forgetting `with`

A `with` block closes the file reliably, even if an exception occurs.

### Assuming relative paths are relative to the script

They are generally relative to the current working directory. Check `Path.cwd()` or build a path from `__file__`.

### Splitting CSV by commas manually

Quoted commas make hand-splitting unreliable. Use the `csv` module.

### Catching every error and continuing silently

Handle expected exceptions specifically and make failures visible enough to diagnose.

---

## 14. Quick reference map

```text
READ TEXT      with open(path, "r", encoding="utf-8") as file:
WRITE TEXT     with open(path, "w", encoding="utf-8") as file:
APPEND         with open(path, "a", encoding="utf-8") as file:
READ ALL       file.read()
READ LINES     for line in file: ...
WRITE          file.write(text)
PATHS          from pathlib import Path
JSON           json.dump / json.load
CSV            csv.writer / csv.reader (use newline="")
ERRORS         FileNotFoundError, PermissionError, UnicodeDecodeError
```

### The most important mental checklist

1. **Where is the file relative to the working directory?** Use `Path.cwd()` to check.
2. **Should this operation read, replace, append, or create-only?** Pick the mode deliberately.
3. **Is this text or binary data?** Use an encoding for text; binary mode has no encoding.
4. **Will the file close if something fails?** Use `with`.
5. **Is the data structured as JSON or CSV?** Use the matching standard-library module.

---

## 15. Practice (answers below)

1. Which file mode replaces existing contents?
2. Which mode adds text to the end?
3. Why is `with open(...)` recommended?
4. What does `read()` return for a text file?
5. Does `write()` add a newline automatically?
6. What is the purpose of `encoding="utf-8"`?
7. Which module should you use to handle CSV rows safely?
8. What is the difference between `json.dump()` and `json.dumps()`?
9. What does a relative path depend on?
10. Which exception is commonly raised when a file does not exist?

<details>
<summary><strong>Show the answers</strong></summary>

1. `"w"`.
2. `"a"`.
3. It closes the file automatically, including when an exception occurs.
4. The remaining file contents as a string.
5. No; include `\n` when needed.
6. It explicitly selects the text encoding used to translate file bytes and Python text.
7. Python's `csv` module.
8. `dump()` writes JSON to a file-like object; `dumps()` returns JSON text.
9. The current working directory (or the path context used to launch the program).
10. `FileNotFoundError`.

</details>

---

## Final idea

File handling is a small cycle: choose a path, choose the right mode, read or write using the right format and encoding, and let `with` close the file. Once you understand paths and the difference between reading, replacing, and appending, you can safely make files part of your Python programs.


---

# 🗂️ Python File Manager

A simple command-line Python file manager using the `pathlib` module.
It supports the following operations:

* 📄 Create a file
* 📖 Read a file
* ✏️ Update a file (rename, overwrite, append)
* 🗑️ Delete a file
* 📂 List all files and folders recursively

---

## 📦 Features

### ✅ 1. Read Files and Folders

Displays a recursive list of all files and folders in the current working directory.

```python
from pathlib import Path

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i + 1}: {item}")
```

---

### 📝 2. Create a File

* Checks if the file already exists.
* If not, creates a new file and writes custom content into it.

```python
def createFile():
    name = input("Enter your file name: ")
    p = Path(name)
    if not p.exists():
        with open(p, "w") as fs:
            data = input("What do you want to write in this file: ")
            fs.write(data)
        print("✅ FILE CREATED SUCCESSFULLY ❤")
    else:
        print("⚠️ File already exists.")
```

---

### 📖 3. Read a File

* Reads and prints the content of a file.
* Validates if the file exists and is readable.

```python
def readFile():
    name = input("Which file do you want to read: ")
    p = Path(name)
    if p.exists() and p.is_file():
        with open(p, "r") as fs:
            data = fs.read()
            print(data)
    else:
        print("❌ File does not exist.")
```

---

### ✏️ 4. Update a File

You can choose one of three operations:

1. **Rename the file**
2. **Overwrite content**
3. **Append new content**

```python
def upDateFile():
    name = input("Which file do you want to update: ")
    p = Path(name)
    if p.exists() and p.is_file():
        print("1. Rename")
        print("2. Overwrite")
        print("3. Append")
        res = int(input("Select your operation: "))
        
        if res == 1:
            new_name = input("New file name: ")
            p.rename(Path(new_name))
            print("✅ File renamed.")
        elif res == 2:
            with open(p, "w") as fs:
                data = input("Enter new content: ")
                fs.write(data)
            print("✅ File overwritten.")
        elif res == 3:
            with open(p, "a") as fs:
                data = input("Enter content to append: ")
                fs.write(data)
            print("✅ Content appended.")
        else:
            print("❌ Invalid option.")
```

---

### 🗑️ 5. Delete a File

Deletes the specified file if it exists.

```python
def deleteFile():
    name = input("Which file do you want to delete: ")
    p = Path(name)
    if p.exists() and p.is_file():
        p.unlink()
        print("🗑️ File deleted successfully.")
    else:
        print("❌ File not found.")
```

---

## 📋 Menu-Driven Interface

```python
print("1. Create a file")
print("2. Read a file")
print("3. Update a file")
print("4. Delete a file")

check = int(input("Please enter your choice: "))

if check == 1:
    createFile()
elif check == 2:
    readFile()
elif check == 3:
    upDateFile()
elif check == 4:
    deleteFile()
else:
    print("❌ Invalid choice.")
```

---

## 🧰 Requirements

* Python 3.6+
* No external libraries needed

---

## 🚀 How to Run

```bash
python main.py
```

---

## 🧠 Concepts Used

* `pathlib` for working with paths
* File operations: `open()`, `read()`, `write()`, `append()`, `rename()`, `unlink()`
* Exception handling using `try-except`
* `input()` for user interaction
* `enumerate()` to index files/folders

---

## 📌 Notes

* Always run the script from the folder where you want to manage files.
* The script does not handle directories—only files.
* You can expand this by adding directory creation and file type filters.

---



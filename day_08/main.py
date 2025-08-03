from pathlib import Path

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i + 1}: {item}")

# ===================================
# 📁 CREATE FILE FUNCTION
# ===================================
def createFile():
    try:
        readFileAndFolder()
        name = input("Enter your file name: ")
        p = Path(name)

        # ✅ Corrected: File should be created if it does NOT exist
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What do you want to write in this file: ")
                fs.write(data)
            print("✅ FILE CREATED SUCCESSFULLY ❤")
        else:
            print("⚠️ File already exists.")
    except Exception as err:
        print(f"❌ An error occurred: {err}")

# ===================================
# 📖 READ FILE FUNCTION
# ===================================
def readFile():
    try:
        readFileAndFolder()
        name = input("Which file do you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print("\n📄 File Content:\n")
                print(data)
            print("\n✅ File read successfully.")
        else:
            print("❌ File does not exist.")
    except Exception as err:
        print(f"❌ An error occurred: {err}")

# ===================================
# ✏️ UPDATE FILE FUNCTION
# ===================================
def upDateFile():
    try:
        readFileAndFolder()
        name = input("Which file do you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 to rename the file")
            print("Press 2 to overwrite file content")
            print("Press 3 to append to the file")

            res = int(input("Tell me what you want to do: "))
            if res == 1:
                name2 = input("Enter the new name of your file: ")
                p2 = Path(name2)
                p.rename(p2)
                print("✅ File renamed successfully.")
            elif res == 2:
                with open(p, "w") as fs:
                    data = input("Write here what you want to overwrite: ")
                    fs.write(data)
                print("✅ File content overwritten.")
            elif res == 3:
                with open(p, "a") as fs:  # FIXED: added `fs` to use in next line
                    data = input("Write here what you want to append: ")
                    fs.write(data)
                print("✅ File content appended.")
            else:
                print("❌ Invalid option.")
        else:
            print("❌ File not found.")
    except Exception as err:
        print(f"❌ An error occurred: {err}")

# ===================================
# ❌ DELETE FILE FUNCTION
# ===================================
def deleteFile():
    try:
        readFileAndFolder()
        name = input("Which file do you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("🗑️ File deleted successfully.")
        else:
            print("❌ File not found.")
    except Exception as err:
        print(f"❌ An error occurred: {err}")

# ===================================
# 📋 MENU
# ===================================
print("\n--- File Manager ---")
print("Press 1 to create a file")
print("Press 2 to read a file")
print("Press 3 to update a file")
print("Press 4 to delete a file")

try:
    check = int(input("Please enter your choice: "))
except ValueError:
    print("❌ Please enter a valid number.")
    exit()

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

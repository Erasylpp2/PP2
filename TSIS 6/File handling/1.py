import os

def list_directories_files(path):
    directories = []
    files = []
    all_contents = []

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            directories.append(entry)
        else:
            files.append(entry)
        all_contents.append(entry)

    print("Directories:", directories)
    print("Files:", files)
    print("All contents:", all_contents)

path = input("Enter path: ")
list_directories_files(path)

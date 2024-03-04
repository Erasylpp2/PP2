import os

def analyze_path(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Filename:", os.path.basename(path))
        print("Directory portion:", os.path.dirname(path))
    else:
        print("Path does not exist.")

path = input("Enter path: ")
analyze_path(path)

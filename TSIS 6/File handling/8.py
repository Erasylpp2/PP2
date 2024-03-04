import os

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        print("File deleted successfully.")
    else:
        print("File does not exist.")

path = input("Enter path of file to delete: ")
delete_file(path)

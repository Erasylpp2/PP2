def copy_file(source, destination):
    with open(source, 'r') as src:
        with open(destination, 'w') as dest:
            dest.write(src.read())

source = input("Enter source filename: ")
destination = input("Enter destination filename: ")
copy_file(source, destination)

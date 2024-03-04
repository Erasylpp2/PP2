def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print("Number of lines:", len(lines))

filename = input("Enter filename: ")
count_lines(filename)

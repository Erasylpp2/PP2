def write_list_to_file(filename, content_list):
    with open(filename, 'w') as file:
        for item in content_list:
            file.write(str(item) + '\n')

filename = input("Enter filename to write to: ")
content_list = input("Enter list elements separated by space: ").split()
write_list_to_file(filename, content_list)

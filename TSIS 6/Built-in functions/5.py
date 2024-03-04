def all_true(elements):
    return all(elements)

my_tuple = eval(input("Enter a tuple: "))  # Input should be provided in the form of (True, False, True, ...)
if all_true(my_tuple):
    print("All elements of the tuple are true.")
else:
    print("Some elements of the tuple are not true.")

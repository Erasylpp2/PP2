def count_case_letters(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

string = input("Enter a string: ")
upper, lower = count_case_letters(string)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)

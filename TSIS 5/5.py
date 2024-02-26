#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
#Напишите программу на Python, которая соответствует строке,
#за которой следует буква «a», заканчивающаяся на «b».
import re

def m(s):
    p = r"a.*b"
    if re.fullmatch(p, s):
        return True
    else:
        return False

s = input()
if m(s):
    print("String matches the pattern.")
else:
    print("String does not match the pattern.")
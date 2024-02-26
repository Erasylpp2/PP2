#Write a Python program to find sequences of lowercase letters joined with a underscore.
#Напишите программу на Python для поиска последовательности строчных букв, соединенных подчеркиванием.

import re

def f(s):
    pattern = r'\b[a-z]+(?:_[a-z]+)+\b'
    sequences = re.findall(pattern, s)
    return sequences

s = input()
result = f(s)
print(result)
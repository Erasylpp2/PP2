#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
#Напишите программу на Python, чтобы заменить все вхождения пробела, запятой или точки двоеточием.
import re

def re(s):
    pattern = r'[ ,.]'
    res = re.sub(pattern, ':', s)
    return res

s = input()
result = re(s)
print(result)
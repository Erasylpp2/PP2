#Write a python program to convert snake case string to camel case string.

def stoc(s):
    elements = s.split('_')
    c = ''.join(x.capitalize() for x in elements[0:])
    return c


s = input()
c = stoc(s)
print(c)

# Function to print all permutations of a string
from itertools import permutations
def print_permutations(string):
    perms = [''.join(p) for p in permutations(string)]
    print(perms)

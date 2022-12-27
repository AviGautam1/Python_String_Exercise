# Write a Python program to print all permutations with given repetition number of characters of a given string.

from itertools import product

def get_permutation(string, rno):
    char = list(string)
    results = []
    for c in product(char, repeat = rno ):
        results.append(c)
    return results


print(get_permutation("avi", 3))
print(get_permutation("avi", 2))

'''
output = 
[('a', 'a', 'a'), ('a', 'a', 'v'), ('a', 'a', 'i'), ('a', 'v', 'a'), ('a', 'v', 'v'), ('a', 'v', 'i'), ('a', 'i', 'a'), ('a', 'i', 'v'), ('a', 'i', 'i'), ('v', 'a', 'a'), ('v', 'a', 'v'), ('v', 'a', 'i'), ('v', 'v', 'a'), ('v', 'v', 'v'), ('v', 'v', 'i'), ('v', 'i', 'a'), ('v', 'i', 'v'), ('v', 'i', 'i'), ('i', 'a', 'a'), ('i', 'a', 'v'), ('i', 'a', 'i'), ('i', 'v', 'a'), ('i', 'v', 'v'), ('i', 'v', 'i'), ('i', 'i', 'a'), ('i', 'i', 'v'), ('i', 'i', 'i')]
[('a', 'a'), ('a', 'v'), ('a', 'i'), ('v', 'a'), ('v', 'v'), ('v', 'i'), ('i', 'a'), ('i', 'v'), ('i', 'i')]
'''



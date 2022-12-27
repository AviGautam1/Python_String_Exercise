# Write A Python Program to Compute all the Permutation of the String.

from itertools import permutations

words = [''.join(p) for p in permutations('avi')]

print(words)


# output = ['avi', 'aiv', 'vai', 'via', 'iav', 'iva']
'''
Write a Python program to find the first repeated character of
a given string where the index of first occurrence is smallest.
'''

def first_smallest_char_index(string):
    a = {}
    for char in string:
        if char in a:
            return char, string.index(char)

        else:
            a[char] = 0
    return 'None'


print(first_smallest_char_index("hello"))
print(first_smallest_char_index("avi"))


'''
output = 
('l', 2)
None
'''
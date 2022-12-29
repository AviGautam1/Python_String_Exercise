'''
Write a Python program to create two strings from a given string.
Create the first string using those character which occurs only once
and create the second string which consists of multi-time occurring characters in the said string.
'''


from collections import Counter
str = input("Enter A String : ")

def create_str(str):
    '''
    Using the Python Counter tool, you can count the key-value pairs
    in an object, also called a hashtable object.

    '''

    str_char = Counter(str)
    str1 = [key for (key, count) in str_char.items() if count == 1]     # In Python Dictionary, items() method is used to return the list with all dictionary keys with values.
    str2 = [key for (key, count) in str_char.items() if count > 1]
    str1.sort()     # The sort() method is a built-in Python method that, by default, sorts the list in ascending order.
    str2.sort()
    return str1, str2

s1 , s2  = create_str(str)


print("".join(s1))
print("".join(s2))

'''
output = 
Enter A String : aaabbcdefgg
cdef
abg
'''

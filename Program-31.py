'''
Write a Python program to check whether a given string contains a capital letter,
a lower case letter, a number and a minimum length.
'''


str = input("Enter the string: ")
res = []
if not any(x.isupper() for x in str):       # The any() function returns True if any item in an iterable are true, otherwise it returns False.
    res.append("String must have 1 Uppercase Character.")
if not any(x.islower() for x in str):
    res.append("String must have 1 Lowercase Character.")
if not any(x.isdigit() for x in str):
    res.append("String must have 1 Number.")
if len(str) < 8:
    res.append("String length should be atleast 8.")
if not res:
    res.append("Valid string.")

for i in res:
    print(i)


'''
output = 
Case-1
Enter the string: aviAVI12
Valid string.

Case-2
Enter the string: avinesh
String must have 1 Uppercase Character.
String must have 1 Number.
String length should be atleast 8.
'''
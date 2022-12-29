# Write a Python program to remove all consecutive duplicates of a given string.

# remove consecutive duplicates from string
n = input("Enter A String : ")

s = ""
for char in n:
    if s == "" or char != s[len(s) - 1]:
        s += char

print(s)

'''
output = 
Enter A String : AAABBBBAABBCDE
ABABCDE
'''
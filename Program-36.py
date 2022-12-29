# Write a Python program to extract numbers from a given string.

str = input("Enter String With Numbers : ")

print("Original String : " + str)
num = ""
for c in str:
    if c.isdigit():             # The isdigit() method returns True if all the characters are digits, otherwise False.
        num = num + c


print("Extracted numbers from the list : " + num)

'''
output = 
Enter String With Numbers : avinesh123 with avi12
Original String : avinesh123 with avi12
Extracted numbers from the list : 12312
'''
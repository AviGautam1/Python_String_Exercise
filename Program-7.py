# Write a Python program to move spaces to the front of a given string.

str1 = input("Enter Spaces String : ")

print("Original String :",str1)
no_spaces = [char for char in str1 if char!=' ']
space= len(str1) - len(no_spaces)
result = ' '*space
print("After moving all spaces to the front:",result + ''.join(no_spaces))


'''
output = 
Enter Spaces String : avinesh gautam
Original String : avinesh gautam
After moving all spaces to the front:  avineshgautam
'''
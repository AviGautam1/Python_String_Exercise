# Write a Python program to remove spaces from a given string.

# Method - 1
str = input("Enter String With Spaces : ")
print(str.replace(" ", ""))


# Method - 2
str = input("Enter String With Spaces : ")
print("".join(str.split()))


'''
output = 
Enter String With Spaces : hi  there how   are    you
hitherehowareyou
'''
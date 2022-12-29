# Write a Python program to decapitalize the first letter of a given string.


str = input("Enter A String : ")
print("The original string is : " , str)

# Using lower() + string slicing
# Lowercase first character of String
res = str[0].lower() + str[1:]

print("The string after decapitalize initial character : ", res)


'''
output = 
Enter A String : AviGautam
The original string is :  AviGautam
The string after decapitalize initial character :  aviGautam
'''



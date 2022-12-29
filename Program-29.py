# Write a Python program to delete all occurrences of a specified character in a given string.

str1 = input("Enter A String : ")
def removeChar(str, char):
    result = str.replace(char, "")
    return(result)


char='a'
print("After Removing a : ", removeChar(str1, char))


'''
output = 
Enter A String : avinesh gautam
After Removing a :  vinesh gutm
'''
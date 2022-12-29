'''
Write a Python program to create a string from two given strings
concatenating uncommon characters of the said strings.
'''

'''
Step 1: Convert both string into set st1 and st2.
Step 2: use the intersection of two sets and get common characters.
Step 3: now separate out characters in each string which are not common in both string.
Step 4: join each character without space to get a final string.
'''

str1 = input("Enter First String : ")
str2 = input("Enter Second String : ")

string1 = set(str1)
string2 = set(str2)

lst = list(string1 & string2)

finallist = [i for i in str1 if i not in lst] +  [i for i in str2 if i not in lst]
print("CONCATENATED STRING IS : ", ''.join(finallist))


'''
output = 
Enter First String : abcdpqr
Enter Second String : xyzabcd
CONCATENATED STRING IS :  pqrxyz
'''
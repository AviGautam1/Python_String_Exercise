# Write a Python program to remove all extra spaces of a given string in single traversal.

str = input("Enter A String : ")

s = ""

for i in range(len(str)):
    if str[i] == " " and str[i+1] == " ":
        continue

    else:
        s = s + str[i]

print(s)


'''
output = 
Enter A String : hi    avinesh     gautam
hi avinesh gautam
'''
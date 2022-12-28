# Write a Python program to remove duplicate characters of a given string.


str = input("Enter A String : ")

print("Before Removing Duplicate Value : ", str)
i = 0
s = ""

for x in str:
    if str.index(x) == i:
        s += x

    i += 1

print("After Removing Duplicate Value : ", s)


'''
output = 
Enter A String : avinesh gautam
Before Removing Duplicate Value :  avinesh gautam
After Removing Duplicate Value :  avinesh gutm

Process finished with exit code 0
'''
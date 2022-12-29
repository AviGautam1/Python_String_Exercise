# Write a Python program find the common values that appear in two given strings.


'''
1. User must enter two input strings and store it in separate variables.
2. Both of the strings are converted into sets and the common letters between both the sets are found using the ‘&’ operator.
3. These common letters are stored in a list.
4. A for loop is used to print the letters of the list.
'''


str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

a = list(set(str1) & set(str2))             # Sets are used to store multiple items in a single variable.
print("The common letters are : ")
for i in a:
    print(i)


'''
output = 
Enter first string : avinesh gautam
Enter second string : avi gautam
The common letters are : 
a
i
t
 
v
g
m
u
'''
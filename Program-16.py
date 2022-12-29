# Python program to find uncommon words from the two string.


str1 = input("Enter First String : ")
str2 = input("Enter Second String : ")

print(set(str1.split()) ^ set(str2.split()))        # ^ returns a set that contains all items from both set, but not the items that are present in both sets.


'''
output = 
Enter First String : hello world in python
Enter Second String : hello world in java
{'java', 'python'}
'''
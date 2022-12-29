# Write a Python program to remove duplicate words from a given string.


string = input("Enter Duplicate Word String : ")

words = string.split()
print ("After Removing Duplicate Words : ", " ".join(sorted(set(words), key=words.index)))

'''
output = 
Enter Duplicate Word String : hi avi hi atul hi udit
After Removing Duplicate Words :  hi avi atul udit
'''
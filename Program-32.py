# Write a Python program to remove unwanted characters from a given string.

string = input("Enter A Unwanted String : ")
print("After Removing Unwanted Character : ", string)

'''
Python String isalnum() method checks whether all the characters in a given string are alphanumeric or not. 
It returns a boolean as True – If all the characters are alphanumeric or else false – 
If one or more characters are not alphanumeric.
'''

test_str = ''.join(letter for letter in string if letter.isalnum())

print("After Removing Unwanted Character : ", test_str)


'''
output = 
Enter A Unwanted String : Pyth*^on Exercis^es
After Removing Unwanted Character :  Pyth*^on Exercis^es
After Removing Unwanted Character :  PythonExercises
'''
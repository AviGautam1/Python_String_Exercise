# Write a Python program to remove punctuations from a given string.


punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# take input from the user
my_str = input("Enter a string: ")
# remove punctuation from the string

no_punct = ""
for char in my_str:
   if char not in punctuation:
       no_punct = no_punct + char


# display the unpunctuated string
print(no_punct)


'''
output = 
Enter a string: Oh! Are You Sad? 
Oh Are You Sad
'''
'''
Write a Python program to check whether any word in a given sting
contains duplicate characrters or not. Return True or False.
'''

text = input("Enter A String : ")
def duplicate_letters(text):
	word_list = text.split()
	for word in word_list:
		if len(word) > len(set(word)):
			return False
	return True


print(duplicate_letters(text))


'''
output = 
Enter A String : hi ankur ankur is a good boy
False
'''
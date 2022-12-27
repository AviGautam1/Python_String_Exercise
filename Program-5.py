# Write a Python program to find the first repeated word in a given string.


str = input("Enter A String : ")

'''
set() method is used to convert any of the iterable 
to sequence of iterable elements with distinct elements.
'''
t = set()
for txt in str.split():
	if txt in t:
	  print(txt)
	else:
	  t.add(txt)

'''
output = 
Enter A String : hello sir hello
hello
'''

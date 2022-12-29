# Write a Python program to count number of non-empty substrings of a given string.

def sub_str(str):
	str_len = len(str);
	return int(str_len * (str_len + 1) / 2);

str1 = input("Input a string: ")
print("Number of substrings:")
print(sub_str(str1))


'''
output = 
Input a string: avinesh
Number of substrings:
28
'''

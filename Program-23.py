# Write a Python program to count number of substrings with same first and last characters of a given string.

str = input("Input a string: ")
def checkEquality(str):
	result = 0
	n = len(str)
	for i in range(n):
		for j in range(i, n):
			if (str[i] == str[j]):
				result = result + 1
	return result


print("Number Of Substring With Equal Ends Is: ", checkEquality(str))


'''
output = 
Input a string: abcab
Number Of Substring With Equal Ends Is:  7
'''

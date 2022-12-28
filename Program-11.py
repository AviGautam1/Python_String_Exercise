# Write a Python program to compute sum of digits of a given string.


str = input("Enter A String : ")

sum_num = 0
for x in str:
	if x.isdigit() == True:
		z = int(x)
		sum_num = sum_num + z


print(sum_num)


'''
output = 
Enter A String : 123abcd45
15
'''
# Write a Python program to convert a given Bytearray to Hexadecimal string.


test_list = [ 133, 53, 234, 241 ]

print("The original string is : " + str(test_list))

# using join() + format()
# Converting bytearray to hexadecimal string
res = ''.join(format(x, '02x') for x in test_list)

print("The string after conversion : " + str(res))


'''
output = 
The original string is : [133, 53, 234, 241]
The string after conversion : 8535eaf1
'''
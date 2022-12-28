# Write a Python program to find maximum length of consecutive 0’s in a given binary string.


str = input("Enter A Binary String : ")

print("Original string: ", str)
def maxConsecutive_of_zero(str):
'''
map() is useful when you need to apply a transformation
function to each item in an iterable and transform them into a new iterable.
'''

    return max(map(len, str.split('0')))

print("Maximum length of consecutive 0’s: ", maxConsecutive_of_zero(str))


'''
output +
Enter A Binary String : 11000111101010111
Original string:  11000111101010111
Maximum length of consecutive 0’s:  4
'''


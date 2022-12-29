'''
Write a Python program to add two strings as they are numbers (Positive integer values).
Return a message if the numbers are string.
'''


def test(n1, n2):

    n1, n2 = '0' + n1, '0' + n2
    if (n1.isnumeric() and n2.isnumeric()):
        return str(int(n1) + int(n2))
    else:
        return 'Error in input!'


print(test("5", "3"))
print(test("1", "2.6"))
print(test("10", "-20"))


'''
output = 
8
Error in input!
Error in input!
'''
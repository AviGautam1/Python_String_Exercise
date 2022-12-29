'''
Write a Python program to print four values decimal, octal,
hexadecimal (capitalized), binary in a single line of a given integer.
'''



i = int(input("Input an integer: "))
o = str(oct(i))[2:]
h = str(hex(i))[2:]
h = h.upper()
b = str(bin(i))[2:]
d = str(i)
print("Decimal : ",d)
print("Octal : ",o)
print("Hexadecimal (capitalized) :",h)
print("Binary :",b)


'''
output = 
Input an integer: 20
Decimal :  20
Octal :  24
Hexadecimal (capitalized) : 14
Binary : 10100
'''
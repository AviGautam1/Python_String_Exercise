# Write a Python program to capitalize first and last letters of each word of a given string.

string = input("Enter A String : ")
print("String Before: ", string)
a = string.split()
b = []
for i in a:
    x = i[0].upper() + i[1:-1] + i[-1].upper()
    b.append(x)

print("String After : ", " ".join(b))


'''
output = 
Enter A String : avinesh gautam
String Before:  avinesh gautam
String After :  AvinesH GautaM
'''

# Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.


str = "Avinesh Gautam 123@gmail.com"
print("Original strings : " ,str)
upr, lwr, num, spl = 0, 0, 0, 0
for i in range(len(str)):
    if str[i] >= 'A' and str[i] <= 'Z':
        upr += 1
    elif str[i] >= 'a' and str[i] <= 'z':
        lwr += 1
    elif str[i] >= '0' and str[i] <= '9':
        num += 1
    else:
        spl += 1

print("UpperCase : " ,upr)
print("LowerCase : " ,lwr)
print("NumberCase : " ,num)
print("SpecialCase : " ,spl)


'''
output = 
Original strings :  Avinesh Gautam 123@gmail.com
UpperCase :  2
LowerCase :  19
NumberCase :  3
SpecialCase :  4
'''
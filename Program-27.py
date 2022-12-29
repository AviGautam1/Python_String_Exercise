# Write a Python program to swap cases of a given string.


str = input("Enter A String : ")

res = ""
for ch in str:
   if ch.isupper():
	   res += ch.lower()
   else:
	   res += ch.upper()
print("Swap Strings Are :", res)


'''
output = 
Enter A String : Hi Avinesh Gautam
Swap Strings Are : hI aVINESH gAUTAM
'''
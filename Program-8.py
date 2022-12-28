# Write a Python program to find the maximum occurring character in a given string.

# Solution - 1
string= input("Enter A String : ")
print(string)

char_freq={}

for i in string:
    if i in char_freq:
        char_freq[i]=char_freq[i]+1
    else:
        char_freq[i] = 1
result= max(char_freq, key = char_freq.get)

print("Most frequent character: ",result)


'''
output = 
Enter A String : hi i am avinesh
hi i am avinesh
Most frequent character:  i
'''

# Solution - 2 using Counter() and max()
from collections import Counter

string= input("Enter A String : ")
print(string)

result= Counter(string)         # Call the Counter() and pass the string
result= max(result, key=result.get)     # To get the maximum count use max() and store the value returned by it in a variable

print("Most frequent character: ",result)


'''
output = 
Enter A String : hello
hello
Most frequent character:  l
'''
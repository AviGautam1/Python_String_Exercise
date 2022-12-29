# Write a Python program to find smallest and largest word in a given string.

str = input("Enter A String : ")

word = str.split()
largest = small = word[0]

for i in range(0, len(word)):
    if len(largest) < len(word[i]):
        largest = word[i]

    if len(small) > len(word[i]):
        small = word[i]

print("Largest Word Is: ", largest)
print("Smallest Word Is: ", small)


'''
output = 
Enter A String : hello avinesh gautam
Largest Word Is:  avinesh
Smallest Word Is:  hello
'''
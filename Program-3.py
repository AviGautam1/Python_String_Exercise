# Write a Python program to find the first repeated character in a given string.


my_string = input("Enter A String : ")

for index, letter1 in enumerate(my_string):
    for letter2 in my_string[index+1:]:
        if letter1 == letter2:
            print("First Repeated Character Is : ", letter2)
            exit(0)

else:
    print("String Does Not Have Repoeated Characters")

'''
output = 
Case-1
Enter A String : hello
First Repeated Character Is :  l

Case-2
Enter A String : avinesh
String Does Not Have Repoeated Characters
'''

# Write a Python program to extract and display the name from a given email address.


email = input("Enter Your Email : ")

username, email = email.split("@")

print("Your Username Is : ", username)

'''
output = 
Enter Your Email : avifet@gmail.com
Your Username Is :  avifet
'''
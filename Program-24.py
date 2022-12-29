'''
Write a Python program to find the index of a given string at which a given substring starts.
If the substring is not found in the given string return 'Not found'.
'''

str1 = input("Enter A String : ")
pos = "au"
if len(pos) > len(str1):
    print("Not found")

for i in range(len(str1)):

    for j in range(len(pos)):

        if str1[i + j] == pos[j] and j == len(pos) - 1:
            print(i)

        elif str1[i + j] != pos[j]:
            break

print("Not found")


'''
output = 
Enter A String : avinesh gautam
9
Not found
'''
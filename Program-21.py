'''
Write a Python program to count characters at same position
in a given string (lower and uppercase characters) as in English alphabet.
'''

str = input("Enter A String : ")
def findCount(str):
    result = 0

    # Traverse the input string
    for i in range(len(str)):

        if ((i == ord(str[i]) - ord('a')) or
                (i == ord(str[i]) - ord('A'))):
            result += 1
    return result

print(findCount(str))


'''
output = 
Case-1
Enter A String : alphabetical
3

Case-2
Enter A String : XBCEFG
2
'''
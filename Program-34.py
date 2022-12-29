# Write a Python program to convert a given heterogeneous list of scalars into a string.

#s = input("Enter A List of String: ")
def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1

s = ["apple", "banana", "kiwi"]
print("List To String : ", listToString(s))


# output = List To String :  applebananakiwi


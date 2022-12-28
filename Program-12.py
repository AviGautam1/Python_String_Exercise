# Write a Python program to remove leading zeros from an IP address.

ip = input("Enter IP Address : ")


# converts the words to integers to remove leading removeZeros
# convert back the integer to string and join them back to a string
ip2 = ".".join([str(int(i)) for i in ip.split(".")])

print("IP Address Is: ", ip2)

'''
output = 
Enter IP Address : 02.02.005.006
IP Address Is:  2.2.5.6
'''
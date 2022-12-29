# Write a Python program to wrap a given string into a paragraph of given width.

str = input("Enter A String : ")
w = int(input("Input the width of the paragraph: "))
'''
Text Wrapping Methods
Module (textwrap.wrap(text, width = 70, **kwargs)) − This method wraps the input paragraph. ...
Module (textwrap.fill(text, width = 70, **kwargs)) − The fill() method is similar to the wrap method, but it does not generate a list
'''

import textwrap
def solve(str, w):
   return textwrap.fill(str, w)

print(solve(str, w))


'''
output = 
Enter A String : hello avinesh gautam how are you
Input the width of the paragraph: 5
hello
avine
sh ga
utam
how
are
you
'''
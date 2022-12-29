# Write a Python program to convert a given string to camelcase.

'''
Use re.sub() to replace any - or _ with a space, using the regexp r"(_|-)+".
Use str.title() to capitalize the first letter of each word and convert the rest to lowercase.
Finally, use str.replace() to remove spaces between words.
'''

from re import sub

def camel(s):
  s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
  return ''.join([s[0].lower(), s[1:]])

print(camel('some_string_with_underscore'))
print(camel('Some string with Spaces'))
print(camel('some-string-with-dashes'))
print(camel('some string-with dashes_underscores and spaces'))


'''
output = 
someStringWithUnderscore
someStringWithSpaces
someStringWithDashes
someStringWithDashesUnderscoresAndSpaces
'''
'''
Write a Python program to convert the values of RGB components
to a hexadecimal color code.
'''

def rgb_to_hex(r, g, b):
  return ('{:X}{:X}{:X}').format(r, g, b)


print(rgb_to_hex(255, 165, 1))
print(rgb_to_hex(192, 192, 192))


'''
output =
FFA51
C0C0C0
'''
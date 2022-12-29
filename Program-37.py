'''Write a Python program to convert a hexadecimal color code
to a tuple of integers corresponding to its RGB components.'''
def hex_to_rgb(hex):
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex[i: i +2], 16)
        rgb.append(decimal)

    return tuple(rgb)

print(hex_to_rgb('FFA501'))
print(hex_to_rgb('FF0000'))
print(hex_to_rgb('000000'))

'''
output = (255, 165, 1)
'''
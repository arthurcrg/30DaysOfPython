import random
import string

# Hexadecimal colors
def list_of_hexa_colors():
    hex_chars = string.digits + 'abcdef'
    return ["#" + "".join(random.choice(hex_chars) for _ in range(6)) for _ in range(10)]
print(list_of_hexa_colors())

# RGB colors
def list_of_rgb_colors():
    return ["rgb({}, {}, {})".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(10)]
print(list_of_rgb_colors())

# Generate any number of colors in hexadecimal or RGB format
def generate_colors(color_type, number_of_colors):
    if color_type == 'hexa':
        hex_chars = string.digits + 'abcdef'
        return ["#" + "".join(random.choice(hex_chars) for _ in range(6)) for _ in range(number_of_colors)]
    elif color_type == 'rgb':
        return ["rgb({}, {}, {})".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(number_of_colors)]

print(generate_colors('hexa', 3)) # ['#a3e12f','#03ed55','#eb3d2b'] 
print(generate_colors('hexa', 1)) # ['#b334ef']
print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
print(generate_colors('rgb', 1))  # ['rgb(33,79, 176)']
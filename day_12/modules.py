# Importing a module
import mymodule
print(mymodule.generate_full_name("John", "Doe"))  # Output: John Doe

# Importing more than one function from a module
from mymodule import generate_full_name, add_two_numbers
print(generate_full_name("Alice", "Johnson"))  # Output: Alice Johnson
print(add_two_numbers())  # Output: The result is: 15

# Modifying the name of the function from a module
from mymodule import generate_full_name as full_name
print(full_name("Jane", "Smith"))  # Output: Jane Smith

# Modifying the name of functions from a module
from mymodule import generate_full_name as full_name, add_two_numbers as add_nums
print(full_name("Bob", "Brown"))  # Output: Bob Brown
print(add_nums())  # Output: The result is: 15

# Built-in modules

# OS module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()

# Sys module
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version

# Statistics module
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3 

# Math module
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

# String module
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Random module
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive




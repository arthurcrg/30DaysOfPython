# Function as Parameter
from functools import reduce


def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<
print(sum_numbers([1, 2, 3, 4, 5]))  # 15

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

# Function as Return Value
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

# Python closures: Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure. 
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add
closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

# Decorators: A decorator is a function that takes another function as an argument, adds some kind of functionality and returns another function without altering the source code of the original function that was passed in.

# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper(): # This wrapper function is a closure that has access to the outer function's variables and parameters
        func = function() # This is where the original function is called and its return value is stored in a variable
        make_uppercase = func.upper() # This is where the original function's return value is modified and stored in a variable
        return make_uppercase # This is where the modified return value is returned to the caller
    return wrapper # This is where the wrapper function is returned to the caller
g = uppercase_decorator(greeting) # This is where the original function is passed as an argument to the decorator function
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator # This is where the decorator is applied to the original function
def greeting(): # This is where the original function is defined
    return 'Welcome to Python' # This is where the original function is called and its return value is stored in a variable
print(greeting())   # WELCOME TO PYTHON

# Multiple decorators to a function

'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

#Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']

# Accepting parameters in decorators
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(pokemon, level, region):
    print("I am a level {} {}.".format(
        pokemon, level, region))

print_full_name("Bulbasaur", "5", 'Kanto')

# Built in higher order functions: map(), filter(), reduce() and zip()

# map()
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers) # map() function applies the square function to each element of the numbers list and returns a map object
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]

# filter()
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers) # filter() function applies the is_even function to each element of the numbers list and returns a filter object
print(list(even_numbers))       # [2, 4]

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]

# reduce()
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str) # reduce() function applies the add_two_nums function to the elements of the numbers_str list and returns a single value
print(total)    # 15
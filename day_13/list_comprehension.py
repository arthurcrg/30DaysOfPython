# List comprehension is a concise way to create lists in Python. It is a compact way of creating a list from a sequence

# One way
pokemon = "Bulbasaur"
pokemon_lst = list(pokemon)
print(type(pokemon_lst))
print(pokemon_lst)

# Another way using list comprehension
pokemon_lst = [letter for letter in pokemon] # This is a list comprehension that iterates over each letter in the string "Bulbasaur" and creates a list of those letters.
print(type(pokemon_lst))
print(pokemon_lst)

numbers = [n for n in range(1, 11)] # This is a list comprehension that creates a list of numbers from 1 to 10.
print(numbers)

squares = [n**2 for n in range(1, 11)] # This is a list comprehension that creates a list of squares of numbers from 1 to 10.
print(squares)

# List of tuples
numbers = [(n, n**2) for n in range(1, 11)] # This is a list comprehension that creates a list of tuples where each tuple contains a number and its square.
print(numbers)

# Combining with if statements
even_numbers = [n for n in range(1, 11) if n % 2 == 0] # This is a list comprehension that creates a list of even numbers from 1 to 10.
print(even_numbers)

# Flatten a list of lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row] # This is a list comprehension that flattens a list of lists into a single list.
print(flat_list)

# Lambda functions are anonymous functions in Python. They are defined using the lambda keyword and can take any number of arguments, but can only have one expression.
# Named function
def add_two_nums(a, b):
    return a + b
print(add_two_nums(2, 3))     # 5

# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

square = lambda x : x ** 2
print(square(3))    # 9

cube = lambda x : x ** 3
print(cube(3))    # 27

# Self invoking lambda function
print((lambda a, b: a + b)(2,3))    # 5

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22

# Lambda functions inside another function
def power(x):
    return lambda n : x ** n
cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8



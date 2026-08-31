# Declaring a function
def greet():
    name = "Link"
    print("Hey " + name + ", listen!")

# Calling the function
greet()

# Function without parameters
def add_two_numbers(): # without anything (parameters) inside the parentheses 
    num1 = 5
    num2 = 10
    result = num1 + num2
    print("The result is:", result)
add_two_numbers()

# Function returning a value (part 1)
def add_two_numbers():
    num1 = 5
    num2 = 10
    result = num1 + num2
    return result
print("The result is:", add_two_numbers())

# Function with parameters
def add_two_numbers(num1, num2): # parameters inside the parentheses
    result = num1 + num2
    return result
print("The result is:", add_two_numbers(5, 10)) # arguments inside the parentheses

def sum_of_numbers(n = int(input("Enter a number: "))): # default parameter value
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers())  # Uses the default value
print(sum_of_numbers(100))  # Uses the provided value

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age 

print('Age: ', calculate_age(2021, 1819))

# Function returning a value (part 2)
def is_even (n):
    if n % 2 == 0:
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False

def find_even_numbers(n):
    evens = []
    for i in range(n + 1): # to include n in the range
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

# Functions with default parameter values
def greet(name = "Link"):
    print("Hey " + name + ", listen!")
greet() # Uses the default value
greet("Zelda") # Uses the provided value

# Arbitrary number of arguments
def greet(*names): # *names allows for an arbitrary number of arguments
    for name in names:
        print("Hey " + name + ", listen!")
    return names
greet("Link", "Zelda", "Ganondorf") # Can pass any number of arguments

# Default and arbitrary number of arguments
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i) 
generate_groups('Team-1','Link','Zelda','Impa') # Can pass any number of arguments

# Dictionary unpacking
# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
    # Print a greeting message using the provided arguments
    print("Hi there", name, "how is the weather in", location)

# Call the function using keyword arguments
greet(name="Alice", location="New York")  
# Output: Hi there Alice how is the weather in New York

# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "New York"}

# Call the function using dictionary unpacking
greet(**my_dict)  
# The ** operator unpacks the dictionary, passing its key-value pairs 
# as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York

# Function as parameter of another function
#You can pass functions around as parameters
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27

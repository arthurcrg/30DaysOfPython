# Except: Handles exceptions that occur during the execution of the code.
try:
    print(10 + '5')
except:
    print('Something went wrong') # This will be triggered because you cannot add an integer and a string together.

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong') # this will be triggered because you cannot subtract a string from an integer.

# Using except to identify error types
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError: # This will be triggered if you try to subtract a string from an integer (TypeError means that the types are incompatible).
    print('Type error occurred') 
except ValueError: # this will be triggered if you try to convert a string to an integer and the string is not a valid number (ValueError means that the value is not appropriate for the operation).
    print('Value error occurred')
except ZeroDivisionError: # this will be triggered if you try to divide a number by zero (ZeroDivisionError means that the operation is not defined for division by zero).
    print('zero division error occurred')

# Finally: The finally block will always be executed, regardless of whether an exception occurred or not. It is often used for cleanup actions.
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')
finally:
    print('This will always be executed')

# Packing and Unpacking arguments:
# * for packing arguments into a tuple
# ** for packing arguments into a dictionary

# Unpacking
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst)) # If there wasn't a * before lst, it would have been treated as a single argument and would have raised an error.

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7] # grabs the first and last elements of the list and unpacks them into the range function
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]

# Another way of Unpacking
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

# Packing
def sum_all(*args): # the * makes so that the function can take any number of arguments and packs them into a tuple called args.
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

def packing_person_info(**kwargs): # the ** makes so that the function can take any number of keyword arguments and packs them into a dictionary called kwargs.
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(pokemon="Bulbasaur",
      region="Kanto", pokemon_type = "Grass/Poison", level=5))

# Spreading
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

# Enumerate: prints the index and the value of each item in a list.
for index, item in enumerate([20, 30, 40]):
    print(index, item)

# Zip: combines two or more lists into a single list of tuples, where each tuple contains one element from each of the input lists.
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)


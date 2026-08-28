# Creating a Tuple
empty_tuple = tuple()  # Empty Tuple
pokeball_types = ("Pokeball", "Great Ball", "Ultra Ball")  # Tuple with values (a tuple is made with PARENTHESES())

# Tuple length
print(f"The length of the empty tuple is {len(empty_tuple)}")
print(f"The length of the pokeball_types tuple is {len(pokeball_types)}")

# Accessing tuple items
print(pokeball_types[0])  # Accessing the first item in the tuple
print(pokeball_types[1])  # Accessing the second item in the tuple
last_index = len(pokeball_types) - 1
print(pokeball_types[last_index])  # Accessing the last item in the tuple
print(pokeball_types[-1])  # Accessing the last item in the tuple using negative indexing

# Slicing tuples
print(pokeball_types[0:2])  # Slicing the first two items
print(pokeball_types[1:3])  # Slicing the second and third items
print(pokeball_types[:2])  # Slicing the first two items
print(pokeball_types[1:])  # Slicing from the second item to the end
print(pokeball_types[::2])  # Slicing every second item

# Slicing with negative indexing
print(pokeball_types[-3:-1])  # Slicing the first two items
print(pokeball_types[-2:])  # Slicing the last two items
print(pokeball_types[:-1])  # Slicing all items except the last one

# Changing tuple to list
pokeball_types = list(pokeball_types)  # Converting tuple to list
pokeball_types.append("Master Ball")  # Adding a new item to the list
pokeball_types = tuple(pokeball_types)  # Converting the list back to a tuple
print(pokeball_types)  # Printing the modified list

# Checking if an item exists in a tuple
pokeball_types = ("Pokeball", "Great Ball", "Ultra Ball")  # Resetting the tuple
print("Pokeball" in pokeball_types)  # Checking if "Pokeball" exists in the tuple (True)
print("Master Ball" in pokeball_types)  # Checking if "Master Ball" exists in the tuple (False)

# Joining tuples
more_pokeball_types = ("Premier Ball", "Safari Ball", "Quick Ball", "Timer Ball")  # Another tuple
combined_pokeball_types = pokeball_types + more_pokeball_types  # Joining two tuples
print(combined_pokeball_types)  # Printing the combined tuple

# Deleting a tuple
del pokeball_types  # Deleting the original tuple
del more_pokeball_types  # Deleting the second tuple
del combined_pokeball_types  # Deleting the combined tuple (IT IS NOT POSSIBLE TO DELETE AN ITEM IN A TUPLE)

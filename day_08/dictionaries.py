# Syntax
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'} # brackets are used to define a dictionary

# Dictionary Length
print(len(dct)) # returns the number of items in the dictionary

# Accessing Items
bulbasaur = {'name': 'Bulbasaur', 'type': 'Grass / Poison', 'level': 5}
print(bulbasaur['name']) # returns 'Bulbasaur'
print(bulbasaur['level']) # returns 5

# If the key does not exist, it will raise a KeyError
# But if you use the get() method, it will return None instead of raising an error
print(bulbasaur.get('type')) # returns 'Grass / Poison'
print(bulbasaur.get('evolution')) # returns None
print(bulbasaur.get('moves')) # returns None

# Adding Items
bulbasaur['moves'] = ['Tackle', 'Growl'] # adds a new key-value pair to the dictionary
bulbasaur['moves'].append('Vine Whip') # adds a new move to the moves list
print(bulbasaur) # prints the updated dictionary

# Modifying Items
bulbasaur['level'] = 6 # modifies the value of the 'level' key
print(bulbasaur) # prints the updated dictionary

# Checking if a Key Exists
print('type' in bulbasaur) # returns True
print('evolution' in bulbasaur) # returns False

# Removing Items
del bulbasaur['level'] # removes the 'level' key-value pair from the dictionary
bulbasaur.pop('moves') # removes the 'moves' key-value pair from the dictionary
bulbasaur.popitem() # removes the last inserted key-value pair from the dictionary
print(bulbasaur) # prints the updated dictionary

# Changing Dictionary to list of items
print(bulbasaur.items()) # returns a list of tuples containing the key-value pairs in the dictionary

# Clearing a Dictionary
bulbasaur.clear() # removes all key-value pairs from the dictionary
print(bulbasaur) # prints an empty dictionary

# Copying a Dictionary
bulbasaur_copy = bulbasaur.copy() # creates a shallow copy of the dictionary
print(bulbasaur_copy) # prints the copied dictionary

# Deleting a Dictionary
del bulbasaur_copy # deletes the copied dictionary
del bulbasaur # deletes the original dictionary

# Getting Values as List
bulbasaur = {'name': 'Bulbasaur', 'type': 'Grass / Poison', 'level': 5}
print(list(bulbasaur.values())) # returns a list of the values in the dictionary




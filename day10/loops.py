# While Loop
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
#prints from 0 to 4 and then prints 5 after the loop ends

# Break and Continue
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3: 
        break # makes the loop stop when count is 3

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue # makes the loop skip the print statement when count is 3
    print(count)
    count = count + 1

# For Loop
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

# Looping through a string
pokemon = 'Bulbasaur'
for letter in pokemon:
    print(letter)
# or
for i in range(len(pokemon)):
    print(pokemon[i])

# For Loop on a Tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# For Loop wih a Dictionary gives you the keys
pokemon = {
    'name': "Bulbasaur",
    'nickname': "Saur",
    'typing': "Grass/Poison",
    'level': 10,
    'region': "Kanto",
    'moveset': ["Tackle", "Growl", "Leech Seed", "Vine Whip"],
    'ability': "Overgrow",
}

for key in pokemon:
    print(key) #prints the keys of the dictionary

for key, value in pokemon.items():
    print(key, value) # this way we get both keys and values printed out

# For in a Set
hyrule_items = {'Master Sword', 'Hylian Shield', 'Hookshot', 'Bow', 'Boomerang'}
for item in hyrule_items:
    print(item) # prints the items in the set, but not in order

# Break and Continue (again) (part 2)
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

# range() function
#range(start, end, step) - start is inclusive, end is exclusive, step is optional and defaults to 1
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end 
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]

for number in range(11):
    print(number)   # prints 0 to 10, not including 11

# Loops in Loops
pokemon = {
    'name': "Bulbasaur",
    'nickname': "Saur",
    'typing': "Grass/Poison",
    'level': 10,
    'region': "Kanto",
    'moveset': ["Tackle", "Growl", "Leech Seed", "Vine Whip"],
    'ability': "Overgrow",
}

for key in pokemon: #will analise the dictionary's keys and values
    if key == 'moveset': # stops the loop when it finds the key 'moveset'
        for move in pokemon['moveset']: #will analise the list of moves in the 'moveset' key
            print(move) #will print the moves in the list, one by one, line by line

# For Else
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)


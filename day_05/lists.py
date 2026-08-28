# Syntax
lst = list()
empty_list = list()  # empty list
print(len(empty_list))  # 0

# Using brackets
list = []  # way easier
print(len(list))  # it's also empty

# Using len() to find the length of a list
bulbasaur_evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur"]
print(
    f"{bulbasaur_evolution_line}. Length: {len(bulbasaur_evolution_line)}"
)  # ['Bulbasaur', 'Ivysaur', 'Venusaur']. Length: 3

# A list can have different types of data
mixed_list = [
    "Bulbasaur",
    {"Typing": "Grass and Poison", "Region": "Kanto"},
    1,
    1.5,
    True,
]

# Positive Indexing
bulbasaur_evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur"]
print(bulbasaur_evolution_line[0])  # Bulbasaur
print(bulbasaur_evolution_line[1])  # Ivysaur
print(bulbasaur_evolution_line[2])  # Venusaur

# Negative Indexing
bulbasaur_evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur"]
print(bulbasaur_evolution_line[-1])  # Venusaur
print(bulbasaur_evolution_line[-2])  # Ivysaur
print(bulbasaur_evolution_line[-3])  # Bulbasaur

# Unpacking a list
bulbasaur_evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur"]
first, second, third = bulbasaur_evolution_line
print(first)  # Bulbasaur
print(second)  # Ivysaur
print(third)  # Venusaur

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first, second, third, *rest, tenth = numbers
print(first)  # 1
print(second)  # 2
print(third)  # 3
print(rest)  # [4, 5, 6, 7, 8, 9]
print(tenth)  # 10

# Slicing a list
bulbasaur_evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur"]
print(bulbasaur_evolution_line[0:2])  # ['Bulbasaur', 'Ivysaur']
print(
    bulbasaur_evolution_line[1:3]
)  # ['Ivysaur', 'Venusaur'] (ONE IS NOT THE FIRST ITEM< IT'S THE SECOND)
print(bulbasaur_evolution_line[0:3])  # ['Bulbasaur', 'Ivysaur', 'Venusaur']
print(
    bulbasaur_evolution_line[1::]
)  # ['Ivysaur', 'Venusaur'] (from the number you put to the end of the list)
print(
    bulbasaur_evolution_line[::2]
)  # ['Bulbasaur', 'Venusaur'] (changes the STEP, so it will take every second item in the list)

# works with negative indexing too
bulbasaur_evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur"]
print(bulbasaur_evolution_line[-3:-1])  # ['Bulbasaur', 'Ivysaur']
print(bulbasaur_evolution_line[-2:])  # ['Ivysaur', 'Venusaur']
print(
    bulbasaur_evolution_line[::-1]
)  # ['Venusaur', 'Ivysaur', 'Bulbasaur'] (A NEGATIVE STEP WILL REVERSE THE LIST)

# Lists are mutable, meaning you can change their content without changing their identity. You can add, remove, or change items in a list.
pikachu_evolution_line = ["Pikachu", "Raichu"]
pikachu_evolution_line[0] = "Pichu"  # changing the first item in the list
print(pikachu_evolution_line)  # ['Pichu','Raichu']
last_pokemon = len(pikachu_evolution_line) - 1
pikachu_evolution_line[last_pokemon] = "Pikachu"  # changing the last
print(pikachu_evolution_line)  # ['Pichu', 'Pikachu']

# Checking if an item is in a list
common_kanto_pokemon = ["Ratatta, Pidgey", "Zubat", "Caterpie", "Weedle"]
does_exist = "Pidgey" in common_kanto_pokemon
print(does_exist)  # True
does_exist = "Bidoof" in common_kanto_pokemon
print(does_exist)  # False

# Adding items to a list
bulbasaur_evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur"]
bulbasaur_evolution_line.append("Mega Venusaur")  # adds an item to the  END of the list
print(bulbasaur_evolution_line)  # ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Mega Venusaur']

# Adding items to a list at a specific index
pikachu_evolution_line = ["Pikachu", "Raichu"]
pikachu_evolution_line.insert(
    0, "Pichu"
)  # adds an item to a specific index in the list
print(pikachu_evolution_line)  # ['Pichu', 'Pikachu', 'Raichu']

# Removing items from a list
bulbasaur_evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur", "Mega Venusaur"]
bulbasaur_evolution_line.remove("Mega Venusaur")  # removes an item from the list
print(bulbasaur_evolution_line)  # ['Bulbasaur', 'Ivysaur', 'Venusaur']

# Removing using pop() method
pikachu_evolution_line = ["Pichu", "Pikachu", "Raichu"]
pikachu_evolution_line.pop(
    0
)  # removes the index inside the pop() method (IF NOT SPECIFIED, IT WILL REMOVE THE LAST ITEM IN THE LIST)
print(pikachu_evolution_line)  # ['Pikachu', 'Raichu']

# Deleting items using del
fruits = ["banana", "orange", "mango", "lemon", "kiwi", "lime"]
del fruits[0]
print(fruits)  # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[
    1
]  # ORANGE IS THE NEW 0, MANGO IS THE NEW 1, LEMON IS THE NEW 2, KIWI IS THE NEW 3, LIME IS THE NEW 4
print(fruits)  # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[
    1:3
]  # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)  # ['orange', 'lime']
del fruits  # deleted the whole thing :(
# If we print fruits now, it should give: NameError: name 'fruits' is not defined

# Clearing a list
bulbasaur_evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur"]
bulbasaur_evolution_line.clear()  # clears the list
print(bulbasaur_evolution_line)  # []

# Copying a list
fruits = ["banana", "orange", "mango", "lemon", "kiwi", "lime"]
fruits_copy = fruits.copy()  # copies the list
print(fruits_copy)  # ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']

# Joining lists
bulbasaur_evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur"]
charmander_evolution_line = ["Charmander", "Charmeleon", "Charizard"]
squirtle_evolution_line = ["Squirtle", "Wartortle", "Blastoise"]
kanto_starters_evolution_lines = (
    bulbasaur_evolution_line + charmander_evolution_line + squirtle_evolution_line
)
print(
    kanto_starters_evolution_lines
)  # ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise']

# Joining lists using extend()
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print("Numbers:", num1)  # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print("Integers:", negative_numbers)  # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# Counting the times an item appears in a list
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
print(ages.count(25))           # 2
print(ages.count(26))           # 1

# Finding the index of an item in a list
bulbasaur_evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur"]
print(bulbasaur_evolution_line.index("Ivysaur"))  # 1(bulbasaur is at index 0)
print(bulbasaur_evolution_line.index("Venusaur"))  # 2

# Reversing a list
bulbasaur_evolution_line = ["Bulbasaur", "Ivysaur", "Venusaur"]
bulbasaur_evolution_line.reverse()  # reverses the list (you have to reverse first, and then print it)
print(bulbasaur_evolution_line)  # ['Venusaur', 'Ivysaur', 'Bulbasaur']

# Sorting a list
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()  # sorts the list in ascending order (or in alphabetical order if the list contains strings)
print(ages)  # [19, 22, 24, 24, 24, 25, 25, 26]
ages.sort(reverse=True)  # sorts the list in descending order (or in reverse alphabetical order if the list contains strings)
print(ages)  # [26, 25, 25, 24, 24, 24, 22, 19]


fruits = ("orange", "lime", "banana", "grape", "kiwi", "mango")  # Tuple of fruits
vegetables = ("carrot", "broccoli", "spinach", "cabbage", "cauliflower")  # Tuple of vegetables
animals = ("dog", "cat", "mouse", "rabbit", "hamster")  # Tuple of animals
food_stuff = fruits + vegetables + animals  # Joining the tuples
food_stuff = list(food_stuff)  # Converting the tuple to a list
middle_index = len(food_stuff)//2  # Getting the middle index of the list
print(f'The middle item in the food_stuff list is: {food_stuff[middle_index]}, wich is number {middle_index}')  # Printing the middle item in the list
del food_stuff[middle_index:middle_index]  # Removing the middle item from the list
del food_stuff[0:3]  # Removing the first two items from the list
del food_stuff[-3:]  # Removing the last three items from the list
food_stuff = tuple(food_stuff)  # Converting the list back to a tuple
print(f'The remaining items in the food_stuff list are: {food_stuff}')  # Printing the remaining items in the list
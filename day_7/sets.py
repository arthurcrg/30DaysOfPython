# Syntax
st = () # to create an empty set we use parentheses
st = {1, 2, 3} # to create a set with elements we use curly braces

# Using the len() function to get the number of elements in a set
hyrule_regions = {"Hyrule Field", "Death Mountain", "Zora's Domain", "Gerudo Desert", "Kokiri Forest"}
print(len(hyrule_regions)) # Output: 5

# Checking if an element is in a set using the 'in' keyword
print("Is Kokiri Forest in Hyrule?", "Kokiri Forest" in hyrule_regions) # Output: True

# Adding an element to a set using the add() method
hyrule_regions.add("Lake Hylia") 
print(hyrule_regions)

# Using update() to add multiple elements to a set
hyrule_regions.update(["Lost Woods", "Hyrule Castle"]) # we put the update elements in a list
print(hyrule_regions)

# Removing an element from a set
hyrule_regions.remove("Death Mountain") # remove() raises an error if the element is not found
print(hyrule_regions)

hyrule_regions.discard("Zora's Domain") # discard() does not raise an error if the element is not found
print(hyrule_regions)

removed_hyrule_region = hyrule_regions.pop() # pop() removes a random element from the set and then returns who it was
print(f"Removed region: {removed_hyrule_region}")
print(hyrule_regions)

hyrule_regions.clear() # clear() removes all elements from the set
print(hyrule_regions) # Output: set()

# Deleting a set using the del keyword
del hyrule_regions # if we try to print hyrule_regions after this line, it will raise an error because the set no longer exists

# Converting a list to a set to remove duplicates
hyrule_races = ["Hylians", "Gorons", "Zoras", "Gerudo", "Hylians", "Zoras", "Kokiri"]
hyrule_races_set = set(hyrule_races) # converting the list to a set removes duplicates
print(hyrule_races_set) # the order of the elements are random because sets are unordered collections

# Joining sets
hyrule_regions_1 = {"Hyrule Field", "Death Mountain", "Zora's Domain"}
hyrule_regions_2 = {"Gerudo Desert", "Kokiri Forest", "Lake Hylia"}

hyrule_regions_joined = hyrule_regions_1.union(hyrule_regions_2) # joining two sets using the union() method
print(hyrule_regions_joined)

print(hyrule_regions_1 | hyrule_regions_2) # joining two sets using the | operator to join sets

hyrule_regions_1.update(hyrule_regions_2) # joining two sets using the update() method
print(hyrule_regions_1)

del hyrule_regions_1, hyrule_regions_2, hyrule_regions_joined

# Finding the intersection of two sets
hero_items = {"Master Sword", "Hylian Shield", "Bow", "Hookshot", "Bombs", "Boomerang"}
sold_items = {"Hylian Shield","Bow", "Bombs",}
print(hero_items)
print(sold_items)

common_items = hero_items.intersection(sold_items) # finding the intersection of two sets using
print(f'Common items: {common_items}') # returns the items that are in both sets

# Checking if a set is a subset or superset of another set
print(hero_items.issubset(sold_items)) # False, because hero_items is a superset of sold_items
print(hero_items.issuperset(sold_items)) # True, because hero_items is a superset of sold_items
print(sold_items.issubset(hero_items)) # True, because sold_items is a subset of hero_items
print(sold_items.issuperset(hero_items)) # False, because sold_items is a subset of hero_items

# Checking difference between two sets
print(hero_items.difference(sold_items)) # returns the items that are in hero_items but not in sold_items
print(sold_items.difference(hero_items)) # returns the items that are in sold_items but not in hero_items (which are none in this case)

# Symmetrical difference between two sets
print(hero_items.symmetric_difference(sold_items)) # returns the items that are in either set but NOT IN BOTH

# Disjoint sets (two sets that have no elements in common)
venusaur_moveset = {"Giga Drain", "Sludge Bomb", "Sleep Powder", "Growth"}
charizard_moveset = {"Flamethrower", "Fly", "Dragon Claw", "Brick Break"}
venusaur_moveset.isdisjoint(charizard_moveset) # returns True because the two sets have no elements in common




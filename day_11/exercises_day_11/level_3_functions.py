# Checking if a number is prime or not
def is_prime(n):
    if n <= 1: # Numbers less than or equal to 1 are not prime
        return False
    for i in range(2, int(n**0.5) + 1): # Check for factors from 2 to the square root of n
        if n % i == 0:
            return False
    return True # If no factors were found, n is prime

print(is_prime(17)) # True
print(is_prime(15)) # False

# Checking if all items are unique in a list
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, 4, 5, 1]
def are_all_items_unique(lst):
    return len(lst) == len(set(lst)) # Convert list to set and compare lengths
print(are_all_items_unique(lst1)) # True
print(are_all_items_unique(lst2)) # False

# Checking if all items in a list are of the same type
def are_all_items_same_type(lst):
    if not lst: # Check for empty list
        return True
    first_type = type(lst[0]) # Get the type of the first item
    for item in lst:
        if type(item) != first_type: # Compare types of all items
            return False
    return True

print(are_all_items_same_type([1, 2, 3])) # True
print(are_all_items_same_type([1, '2', 3])) # False


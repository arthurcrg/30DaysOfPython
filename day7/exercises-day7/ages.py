age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)

print(age) # Output: [22, 19, 24, 25, 26, 24, 25, 24] - duplicates are present
print(len(age)) # Output: 8
print(age_set) # Output: {19, 22, 24, 25, 26} - duplicates are removed
print(len(age_set)) # Output: 5

# String: text data, can be a single character or multiple characters, is ordered, and is immutable
# List: has multiple items, can have duplicates, is ordered, and is mutable
# Tuple: has multiple items, can have duplicates, is ordered, and is immutable
# Set: has multiple items, cannot have duplicates, is unordered, and is mutable

sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
print(words)
unique_words = set(words)
print(unique_words)
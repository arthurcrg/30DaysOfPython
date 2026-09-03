# Most frequent word in the paragraph
import re
paragraph = '''I love teaching. If you do not love teaching what else can you love.
I love Python if you do not love something which can give you all the capabilities
to develop an application what else can you love.'''

paragraph = paragraph.replace('.', '') # Remove the full stop from the paragraph
words = paragraph.split()
word_count = []
for word in words:
    count = words.count(word)
    word_count.append((count, word))
word_count.sort(reverse=True)
print(word_count)

# Position of particles
import re

text = '''The position of some particles on the horizontal x-axis are -12, -4, -3 
and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'''

numbers = re.findall(r'-?\d+', text)

numbers = [int(number) for number in numbers]

print(numbers) # [-12, -4, -3, -1, 0, 4, 8]

distance = max(numbers) - min(numbers)
print(distance) # 20




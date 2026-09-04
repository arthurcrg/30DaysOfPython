romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

# Most Frequently Used Words in the text Romeo and Juliet
import requests
response = requests.get(romeo_and_juliet)
text = response.text
text = text.lower()  # converting the text to lower case
for character in '.,!?;:"()[]':
    text = text.replace(character, '')

words = text.split()  # splitting the text into words
word_count = []
for word in set(words):  # using set to get unique words
    word_count.append((word, words.count(word)))  # counting the frequency of each word
    word_count.sort(key=lambda x: x[1], reverse=True)  # sorting the words by frequency
print(word_count[:10])  # printing the top 10 most frequent words
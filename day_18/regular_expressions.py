import re # this module allows us to use regular expressions in Python

# RegEx help us find patterns in strings
# To find patterns we use different methods from the re module

#re.match() - This method checks for a match only at the beginning of the string.
txt = 'Bulbasaur, the seed Pokémon. Bulbasaur can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun\'s rays, the seed grows progressively larger.'
match = re.match('Bulbasaur', txt, re.I)
print(match) # <re.Match object; span=(0, 9), match='Bulbasaur'>

span = match.span() # returns a tuple containing the start and end positions of the match
print(span) # (0, 9)

start, end = span # unpacking the tuple into two variables
print(start, end) # 0 9
substring = txt[start:end] # slicing the string using the start and end positions
print(substring) # Bulbasaur

# re.search() - This method searches for a match anywhere in the string.
search = re.search('seed', txt, re.I)
print(search) # <re.Match object; span=(4, 8), match='seed

span = search.span() # returns a tuple containing the start and end positions of the match
print(span) # (4, 8)

start, end = span # unpacking the tuple into two variables
print(start, end) # 4 8
substring = txt[start:end] # slicing the string using the start and end positions
print(substring) # seed

# re.findall() - This method returns a list of all matches in the string.
# OBS: re.search() returns only the first match, while re.findall() returns all matches.
findall = re.findall('seed', txt, re.I)
print(findall) # ['seed', 'seed']

# re.sub() - This method replaces all matches in the string with a specified string.
replaced = re.sub('seed', 'bulb', txt, re.I)
print(replaced) # Bulbasaur, the bulb Pokémon. Bulbasaur can be seen napping in bright sunlight. There is a bulb on its back. By soaking up the sun's rays, the bulb grows progressively larger.


confusing_txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)

# re.split() - This method splits the string at each match and returns a list of substrings.
split = re.split('.', txt)
print(split)

# RegEx patterns - We can use special characters to create patterns that match specific types of strings.
import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

# Square brackets [] - makes the match case insensitive, we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

# Escape character \ - we can use the escape character to match special characters in the string.
regex_pattern = r'\d'  # this means we are looking for any digit in the string
txt = 'There are 2 apples and 3 bananas in the basket.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2', '3']

# One or more times + - we can use the + character to match one or more occurrences of the preceding character.
regex_pattern = r'\d+'  # this means we are looking for one or more digits
txt = 'There are 2 apples and 3 bananas in the basket in 2026.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2', '3', '2026']

# Period . - we can use the . character to match any character except a newline.
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

# Zero or more times * - we can use the * character to match zero or more occurrences of the preceding character.
regex_pattern = r'[a].*'  # . any character, * any character zero or more times
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

# Zero or one time ? - we can use the ? character to match zero or one occurrence of the preceding character.
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

# Quantifiers in RegEx - we can use quantifiers to specify how many times a character or group of characters should be matched.
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}' # between one and four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] 

# Cart^ - we can use the ^ character to match the beginning of a string.
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # this means we are looking for the word 'This' at the beginning of the string
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

regex_pattern = r'[^A-Za-z ]+'  # this means we are looking for any character that is not a letter (A-Z or a-z) one or more times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8,', '2021']  # this means we are looking for any character that is not a letter (A-Z or a-z) one or more times


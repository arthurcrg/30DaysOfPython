# Escape Sequence Strings
print("I hope everyone is enjoying the Python Challenge.\nAre you ?")  # line break
print("Days\tTopics\tExercises")  # adding tab space or 4 spaces
print("Day 1\t5\t5")
print("Day 2\t6\t20")
print("Day 3\t5\t23")
print("Day 4\t1\t35")
print("This is a backslash  symbol (\\)")  # To write a backslash
print(
    'In every programming language it starts with "Hello, World!"'
)  # to write a double quote inside a single quote

# F Strings
a = 4
b = 3
print(f"{a} + {b} = {a +b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

# Unpacking Characters from a String
language = "Python"
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

# Accessing Characters in Strings by Index
language = "Python"
print(language[0])  # P
print(language[1])  # y
print(language[-1])  # n
print(language[-2])  # o

# Slicing Strings
language = "Python"
first_three = language[0:3]  # starts at zero index and up to 3 but DOES NOT INCLUDE 3
print(first_three)  # Pyt
last_three = language[3:6]
print(last_three)  # hon
pto = language[0:6:2]
print(pto)  # Pto

# Another way
last_three = language[-3:]
print(last_three)  # hon
last_three = language[3:]
print(last_three)  # hon

# Reversing a String
pokemon = "Bulbasaur"
print(pokemon)  # Bulbasaur
print(pokemon[::-1])  # rauasluB

# String Methods
pokemon = "Bulbasaur"
print(pokemon.capitalize())  # Bulbasaur
print(pokemon.upper())  # BULBASAUR
print(pokemon.lower())  # bulbasaur
print(pokemon.count("a"))  # Quantos caracteres 'a' existem na string (2)
print(pokemon.find("l"))  # Primeira ocorrência do caractere 'l' na string (1)
print(pokemon.rfind("o"))  # Ultima ocorrência do caractere 'o' na string (4)
print(pokemon.index("saur"))  # Encontra a primeira ocorrência de uma substring na string (4)
print(pokemon.rindex("Bulba"))  # Encontra a última ocorrência de uma substring na string (4)
print(pokemon.endswith("saur")) # True
print(pokemon.startswith("Bulba")) # True
print(pokemon.isalnum())  # Verifica se todos os caracteres da string são alfanuméricos (True)
print(pokemon.isdigit())  # Verifica se todos os caracteres da string são dígitos (False)
print(pokemon.isdecimal())  # Verifica se todos os caracteres da string são decimais (False)
print(pokemon.isnumeric())  # Verifica se todos os caracteres da string são numéricos (aceita mais números do que isdigit) (False)
print(pokemon.isidentifier())  # Verifica se a string é um identificador válido (True)
print(pokemon.islower())  # Verifica se todos os caracteres da string são minúsculos (False)
print(pokemon.isupper())  # Verifica se todos os caracteres da string são maiúsculos (False)

print('Bulbasaur \n Charmander \n Squirtle')  # Quebra de linha
print(' Bulbasaur \t Charmander \t Squirtle \n Grass/Poison \t Fire \t \t Water')  # Tabulação

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")
print(f' 8 / 6 = {8 / 6:.2f}')


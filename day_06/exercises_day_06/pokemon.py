# The original exercise told me to use my family. There's no way I'm putting my family here

kanto_starters = ("Bulbasaur", "Charmander", "Squirtle")  # Tuple of Kanto starters
johto_starters = ("Chikorita", "Cyndaquil", "Totodile")  # Tuple of Johto starters

starters = kanto_starters + johto_starters  # Joining two tuples
print(f'The total of starters from Kanto and Johto is {len(starters)}')  # Printing the total number of starters
print(f'The starters from Kanto and Johto are: {starters}')  # Printing the starters

starters = list(starters)  # Converting the tuple to a list
grass_starters = starters[0:4] #Removing Charmander and Squirtle from the list
del grass_starters[1:3]  # Removing Cyndaquil and Totodile from the list
grass_starters = tuple(grass_starters)  # Converting the list back to a tuple
print(f'The grass starters from Kanto and Johto are: {grass_starters}')  # Printing the grass starters
starters = tuple(starters)  # Converting the list back to a tuple

print(starters)  # Printing the starters
starters = list(starters)  # Converting the tuple to a list
kanto_starters = starters[0:3]  # Getting the Kanto starters from the list
johto_starters = starters[3:6]  # Getting the Johto starters from the list
kanto_starters = tuple(kanto_starters)  # Converting the list back to a tuple
johto_starters = tuple(johto_starters)  # Converting the list back to a tuple
print(f'Kanto:{kanto_starters}, Johto: {johto_starters}')  # Printing the Kanto and Johto starters
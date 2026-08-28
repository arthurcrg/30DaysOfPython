"""Regras de nomenclatura de variáveis em Python:

O nome de uma variável deve começar com uma letra ou o caractere underscore
O nome de uma variável não pode começar com um número
Um nome de variável só pode conter caracteres alfanuméricos e underscores (A-z, 0-9 e _ )
Os nomes de variáveis diferenciam maiúsculas de minúsculas (firstname, Firstname, FirstName e FIRSTNAME são variáveis diferentes)
"""

# Exemplo do uso da nomenclatura padrão de variáveis em Python:
pokemon_name = "Bulbasaur"
pokemon_type = "Grass/Poison"
pokedex_number = 1
pokedex_entry = "Bulbasaur, the seed Pokémon. A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon."
region = "Kanto"
has_evolution = True
common_moves = ["Tackle", "Growl", "Leech Seed", "Vine Whip"]
pokemon_info = {
    "name": pokemon_name,
    "type": pokemon_type,
    "pokedex_number": pokedex_number,
    "pokedex_entry": pokedex_entry,
    "region": region,
    "has_evolution": has_evolution,
    "common_moves": common_moves,
}

print("Informações do Pokémon:", pokemon_info)

# Exemplo do uso da função len() para verificar o tamanho de uma variável:

print("Pokémon name: ", pokemon_name)
print("Pokémon name (tamanho): ", len(pokemon_name))
print("Type: ", pokemon_type)
print("Type (tamanho): ", len(pokemon_type))
print("Pokédex number: ", pokedex_number)
print("Pokédex number (tamanho): ", len(str(pokedex_number)))
print("Pokédex entry: ", pokedex_entry)
print("Pokédex entry (tamanho): ", len(pokedex_entry))
print("Region: ", region)
print("Region (tamanho): ", len(region))
print("Has evolution: ", has_evolution)
print("Has evolution (tamanho): ", len(str(has_evolution)))
print("Common moves: ", common_moves)
print("Common moves (tamanho): ", len(common_moves))

# Exemplo de várias variáveis em uma única linha:
(
    pokemon_name,
    pokemon_type,
    pokedex_number,
    pokedex_entry,
    region,
    has_evolution,
    common_moves,
) = (
    "Bulbasaur",
    "Grass/Poison",
    1,
    "Bulbasaur, the seed Pokémon. A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.",
    "Kanto",
    True,
    ["Tackle", "Growl", "Leech Seed", "Vine Whip"],
)
print(
    "Variáveis em uma única linha: ",
    pokemon_name,
    pokemon_type,
    pokedex_number,
    pokedex_entry,
    region,
    has_evolution,
    common_moves,
)

# Obtendo entradas do usuário para as variáveis usando input()
favorite_pokemon = input("Qual é o seu Pokémon favorito? ")
print("Então seu Pokémon favorito é", favorite_pokemon, "!")

# Descobrindo o tipo de uma variável usando type()
print("O tipo da variável pokemon_name é: ", type(pokemon_name))
print("O tipo da variável pokedex_number é: ", type(pokedex_number))

# Podemos usar as funções int(), float() e str() para converter variáveis de um tipo para outro:

# int para float
num_int = 10
print("num_int:", num_int)  # 10
num_float = float(num_int)
print("num_float:", num_float)  # 10.0

# float para int
gravity = 9.81
print(int(gravity))  # 9

# int para str
num_int = 10
print("num_int:", num_int)  # 10
num_str = str(num_int)
print("num_str:", num_str)  # '10'


# str para list
print(favorite_pokemon)  # 'nome do Pokémon favorito do usuário'
str_to_list = list(favorite_pokemon)
print(str_to_list)  # cada caractere da string é convertido em um elemento da lista

pokemon = {
    'name': "Bulbasaur",
    'nickname': "Saur",
    'typing': "Grass/Poison",
    'level': 10,
    'region': "Kanto",
    'moveset': ["Tackle", "Growl", "Leech Seed", "Vine Whip"],
    'ability': "Overgrow",
}

if 'moveset' in pokemon:
    middle_move = len(pokemon['moveset']) / 2
    if len(pokemon['moveset']) % 2 == 0:
        print(pokemon['moveset'][int(middle_move) - 1], 'and', pokemon['moveset'][int(middle_move)], 'are the middle moves')
    else:
        print(pokemon['moveset'][int(middle_move)], 'is the middle move')
    if 'Leech Seed' in pokemon['moveset']:
        print('Leech Seed is in the moveset')
    else:
        print('Leech Seed is not in the moveset')
    if len(pokemon['moveset']) < 4:
        print('Bulbasaur hasn\'t learned all 4 moves yet')
    else:
        print('Bulbasaur has learned all 4 moves')
    if pokemon['name'] == 'Bulbasaur' and pokemon['region'] == 'Kanto':
        print(f'This is a {pokemon['name']}, and it was caught in the {pokemon['region']} region.')

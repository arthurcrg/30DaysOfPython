numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_and_zero = [n for n in numbers if n <= 0]
print(neg_and_zero)


list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in list_of_lists for num in row]
print(flat_list)

numbers = [(n, *[n**power for power in range(6)]) for n in range(11)]
print(numbers)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_flat = [
    [country.upper(), country[:3].upper(), city.upper()]
    for country, city in countries
]
print(countries_flat)

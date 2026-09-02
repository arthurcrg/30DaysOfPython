countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)

def upper_function(country):
    return country.upper()

countries_upper = map(upper_function, countries)
print(list(countries_upper))  # ['ESTONIA', 'FINLAND', 'SWEDEN', 'DENMARK', 'NORWAY', 'ICELAND']

def square_function(number):
    return number ** 2

numbers_squared = map(square_function, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16,

def filter_function(country):
    if "land" in country:
        return True
    return False

countries_land = filter(filter_function, countries)
print(list(countries_land))  # ['Finland', 'Iceland']

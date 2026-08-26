a = 3
b = 2

# Arithmetic Operations and Assigning them to Variables
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
remainder = a % b
exponentiation = a ** b

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division (divisão sem resto):", floor_division)
print("Remainder (resto da divisão):", remainder)
print("Exponentiation:", exponentiation)

#Comparison Operators
print('3>2:', 3>2)  # True
print('3>=2:', 3>=2)  # True
print('3<2:', 3<2)  # False
print('3<=2:', 3<=2)  # False
print('3==2:', 3==2)  # False
print('3!=2:', 3!=2)  # True

print("Length of 'Bulbasaur' equals length of 'Venusaur':", len('Bulbasaur') == len('Venusaur'))  # False
print("Length of 'Bulbasaur' not equals length of 'Venusaur':", len('Bulbasaur') != len('Venusaur'))  # True
print('Length of Bulbasaur greater than length of Venusaur:', len('Bulbasaur') > len('Venusaur'))  # False
print('Length of Bulbasaur less than length of Venusaur:', len('Bulbasaur') < len('Venusaur'))  # True

print('Bulbasaur is Venusaur:', 'Bulbasaur' is 'Venusaur')  # False
print('Bulbasaur is not Venusaur:', 'Bulbasaur' is not 'Venusaur')  # True
print('"saur" is in Bulbasaur:', 'saur' in 'Bulbasaur')  # True
print('"saur" is not in Venusaur:', 'saur' not in 'Venusaur')  # True

print('"Bulbasaur" is not "Venusaur" and "saur" is in "Bulbasaur":', 'Bulbasaur' is not 'Venusaur' and 'saur' in 'Bulbasaur')  # True (Retorna True porque ambas condições são verdadeiras)
print('"Length of Bulbasaur equals length of Venusaur or "saur" is in "Venusaur":', len('Bulbasaur') == len('Venusaur') or 'saur' in 'Venusaur')  # True (Retorna True porque uma das condições é verdadeira)
print("'Bulbasaur' is not is 'Venusaur'", not('Bulbasaur' is 'Venusaur'))  # True (Retorna True porque a condição é falsa, e o operador not inverte o resultado)

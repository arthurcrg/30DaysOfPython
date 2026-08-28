import math

r = 30 # Raio do círculo

#Área do Círculo:
area = math.pi * r **2
print(f'A área do círculo de raio {r}m é: {area:.2f}m²')

#Perímetro do Círculo:
per = 2 * math.pi * r
print(f'O perímetro do círculo de raio {r}m é: {per:.2f}m')

#Área de um Círculo com raio fornecido pelo usuário:
r_user = int(input('Digite o valor do raio do círculo (em metros): '))
area_user = math.pi * r_user **2
print(f'A área do círculo de raio {r_user}m é: {area_user:.2f}m²')

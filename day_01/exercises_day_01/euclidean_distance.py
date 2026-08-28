q1 = int(input('Digite o valor de q1:'))
q2 = int(input('Digite o valor de q2:'))
p1 = int(input('Digite o valor de p1:'))
p2 = int(input('Digite o valor de p2:'))

dist = ((q1 - p1)**2 + (q2 - p2)**2)**(1 / 2)

print(f'A distância euclidiana entre os pontos P({p1}, {p2}) e Q({q1}, {q2}) é: {dist:.2f}')

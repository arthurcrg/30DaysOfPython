A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A | B)

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

BA = B.union(A)
AB = A.union(B)
print(BA)
print(AB)

print(A.symmetric_difference(B))

del A, B, BA, AB

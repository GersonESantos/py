lista = [8, 1, 3, 5, 16, 7, 9, 41, 2, 10]
x = lista[0]
for valor in lista:
    if valor % 2 == 0 or valor > x: 
            x = valor
print("Resultado: %d "% x)
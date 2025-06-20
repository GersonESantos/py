import numpy as calculadora
dados1 = calculadora.array([[21, 32, 28], [34, 25, 29], [17, 19, 22]])
dadost = dados1.Transpost  # Corrigido para transposta
soma = calculadora.sum(dadost, axis=1)
for valor in soma:
    print(valor / 3)
import numpy as calculadora

#rr
dados1 = calculadora.array([[21, 32, 28], [34, 25, 29], [17, 19, 22]])

dadost = dados1.Transpost

soma = calculadora.sum(dadost,axis=1)

total = 3

for valor in soma:
    total = valor
    
    print(total/3)
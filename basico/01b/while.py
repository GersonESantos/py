contador = 1
while contador <= 5:
    print(contador)
    contador += 1
print("Fim do loop")


while True:
    x = input("Digite um número (0 para sair): ")
    if x == "0":
        break
    print(f"Você digitou: {x}")

print("Fim do loop")
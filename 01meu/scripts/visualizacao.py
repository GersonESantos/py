import pandas as pd
import matplotlib.pyplot as plt

# Criar um DataFrame simples
dados = {
    "Categoria": ["A", "B", "C", "D"],
    "Valores": [23, 45, 12, 67]
}
df = pd.DataFrame(dados)

# Criar um gráfico de barras
plt.bar(df["Categoria"], df["Valores"], color="skyblue")

# Adicionar título e rótulos
plt.title("Exemplo de Gráfico de Barras")
plt.xlabel("Categoria")
plt.ylabel("Valores")

# Mostrar o gráfico
plt.show()
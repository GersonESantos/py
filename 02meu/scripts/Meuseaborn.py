import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Criar DataFrame
dados = {
    "Categoria": ["A", "B", "C", "D"],
    "Valores": [23, 45, 12, 67]
}
df = pd.DataFrame(dados)

# Usar estilo do seaborn
sns.set(style="whitegrid")

# Criar gráfico de barras com seaborn
sns.barplot(x="Categoria", y="Valores", data=df, palette="viridis")

# Adicionar título
plt.title("Gráfico de Barras com Seaborn", fontsize=16)

# Mostrar
plt.show()
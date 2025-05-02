import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados com datas
datas = pd.date_range(start="2023-01-01", periods=6, freq="M")
valores = [100, 120, 130, 110, 140, 150]
df = pd.DataFrame({"Data": datas, "Vendas": valores})

# Configurar estilo
sns.set(style="darkgrid")

# Gráfico de linhas
plt.figure(figsize=(10, 6))  # Tamanho do gráfico
sns.lineplot(x="Data", y="Vendas", data=df, marker="o", color="teal")

# Título e rótulos
plt.title("Vendas Mensais", fontsize=18)
plt.xlabel("Data")
plt.ylabel("Vendas")

# Mostrar
plt.show()
import pandas as pd

# Criar um DataFrame a partir de um dicionário
dados = {
    "Nome": ["Alice", "Bob", "Carlos"],
    "Idade": [25, 30, 35],
    "Cidade": ["São Paulo", "Rio", "Belo Horizonte"]
}

df = pd.DataFrame(dados)

# Mostrar o DataFrame
print(df)

# Filtrar dados
maiores_30 = df[df["Idade"] > 30]
print(maiores_30)

# Agrupar e calcular média
df.groupby("Cidade")["Idade"].mean()
import pandas as pd

# Criar DataFrame
df = pd.DataFrame({
    "Produto": ["A", "B", "C"],
    "Preço": [10, 20, 30]
})

# Salvar em CSV
df.to_csv("dados/produtos.csv", index=False)

# Carregar e mostrar
df_lido = pd.read_csv("dados/produtos.csv")
print(df_lido)
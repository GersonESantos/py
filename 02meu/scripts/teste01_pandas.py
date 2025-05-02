import pandas as pd

# Criar DataFrame com mais colunas
df = pd.DataFrame({
    "Produto": ["A", "B", "C"],
    "Preço": [10, 20, 30],
    "Quantidade": [100, 50, 20]
})

# Salvar em CSV
df.to_csv("dados/produtos.csv", index=False)

# Carregar e mostrar
df_lido = pd.read_csv("dados/produtos.csv")

# Calcular valor total por produto (nova coluna)
df_lido["Valor_Total"] = df_lido["Preço"] * df_lido["Quantidade"]

# Mostrar resultados
print(df_lido)

# Salvar novamente com a nova coluna
df_lido.to_csv("dados/produtos_atualizados.csv", index=False)
# Filtrar produtos com preço maior que 15
filtrados = df_lido[df_lido["Preço"] > 15]
print("\nProdutos com preço > 15:")
print(filtrados)

# Agrupar por categoria (exemplo simples)
# (Você pode expandir isso depois!)
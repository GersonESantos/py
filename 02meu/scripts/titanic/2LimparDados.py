import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o dataset
df = sns.load_dataset("titanic")

# Mostrar primeiras linhas
print(df.head())
df.dropna(inplace=True)  # Remove linhas com valores nulos
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o dataset
df = sns.load_dataset("titanic")

# Mostrar primeiras linhas
print(df.head())
df.dropna(inplace=True)  # Remove linhas com valores nulos
sns.countplot(x="survived", data=df, palette="Set2")
plt.title("Sobreviventes vs. Não Sobreviventes")
plt.xlabel("Sobreviveu (0 = Não, 1 = Sim)")
plt.ylabel("Contagem")
plt.show()
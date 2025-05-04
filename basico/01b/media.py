import pandas as pd
# Dados com algumas notas (e um valor ausente)
dados = {
    "Nome": ["Alice", "Bob", "Carlos", "Diana"],
    "Matemática": [85, 90, 70, None],  # Carlos não fez a prova
    "Português": [75, 80, 85, 90],
    "História": [90, 85, None, 80]  # Carlos e Alice não fizeram a prova
}

# Criar o DataFrame
df = pd.DataFrame(dados)
print("DataFrame original:")
print(df)

# Calcular a média da coluna 'Matemática'
media_matematica = df["Matemática"].mean()
print(f"\nMédia em Matemática: {media_matematica:.2f}")
# Média por disciplina (colunas)
media_por_disciplina = df[["Matemática", "Português", "História"]].mean()
print("\nMédia por disciplina:")
print(media_por_disciplina)
# Calcular média por aluno (ignorando NaN)
df["Média"] = df[["Matemática", "Português", "História"]].mean(axis=1)
print("\nMédia por aluno:")
print(df[["Nome", "Média"]])
# Substituir NaN por 0
df_preenchido = df.fillna(0)

# Recalcular a média por aluno
df_preenchido["Média_Preenchida"] = df_preenchido[["Matemática", "Português", "História"]].mean(axis=1)
print("\nMédia por aluno (com NaN substituído por 0):")
print(df_preenchido[["Nome", "Média_Preenchida"]])
# Calcular a mediana da coluna 'Matemática'
mediana_matematica = df["Matemática"].median()
print(f"\nMediana em Matemática: {mediana_matematica}")
# Mediana por disciplina (colunas)
mediana_por_disciplina = df[["Matemática", "Português", "História"]].median()
print("\nMediana por disciplina:")
print(media_por_disciplina)

# Calcular mediana por aluno (ignorando NaN)
df["Mediana"] = df[["Matemática", "Português", "História"]].median(axis=1)
print("\nMediana por aluno:")
print(df[["Nome", "Mediana"]])
# Substituir NaN por 0
df_preenchido = df.fillna(0)

# Recalcular a mediana por aluno
df_preenchido["Mediana_Preenchida"] = df_preenchido[["Matemática", "Português", "História"]].median(axis=1)
print("\nMediana por aluno (com NaN substituído por 0):")
print(df_preenchido[["Nome", "Mediana_Preenchida"]])
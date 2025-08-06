import pandas as pd
import numpy as np 

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print(df.head(10))
print(df.info())
print(df.describe())
linhas, colunas = df.shape
print(f"Linhas: {linhas} | Colunas: {colunas}")
print(df.isnull().sum())
print(df.columns)
df.dropna(inplace=True)
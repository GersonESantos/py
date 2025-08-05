import pandas as pd
import numpy as np 

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

df.head(10)
df.info()
df.describe()

df.isnull().sum()   
df.dropna(inplace=True)
df.isnull().sum()
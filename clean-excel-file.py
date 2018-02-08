import numpy as np
import pandas as pd


df = pd.read_excel("Raw-Text-Master.xlsx")

df = df.groupby('ID').agg(lambda x: x.tolist())

# Remove Brackets from CSV for cleaner dataset
df['Post'] = df['Post'].str[0]

df.to_csv("Cleaned-Text.csv")

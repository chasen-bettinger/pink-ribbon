import numpy as np
import pandas as pd


df = pd.read_excel("Raw-Text-Master.xlsx")

# I have to rename the column headers because Excel thinks if your column is 
# ID, it is in SKYL format, whatever that means

df.columns = ['id', 'date', 'post']

df['day'] = df['date'].dt.day
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

df = df.groupby('id').agg(lambda x: x.tolist())

# Remove Brackets from CSV for cleaner dataset

df['id'] = df['id'].str[0]
df['date'] = df['date'].str[0]
df['post'] = df['post'].str[0]
df['day'] = df['day'].str[0]
df['month'] = df['month'].str[0]
df['year'] = df['year'].str[0]


df.to_csv("Cleaned-Text.csv")

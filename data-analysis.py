import numpy as np
import pandas as pd

df = pd.read_csv("Cleaned-Text.csv")


def checkPink(sentence):
    if 'pink' in sentence:
        return 1
    else:
        return 0


df['contains_pink'] = df.Post.apply(lambda x: checkPink(x))

# These are the target blogs we want to analyze
pinkBlogs = df[df['contains_pink'] == 1]

# These are the blogs that will serve as our baseline
nonPinkBlogs = df[df['contains_pink'] == 0]

pinkIDs = []

for index, row in pinkBlogs.iterrows():
    pinkIDs.append(row['ID'])

print(pinkIDs)

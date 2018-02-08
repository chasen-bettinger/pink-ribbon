import numpy as np
import pandas as pd
from textblob import TextBlob


df = pd.read_csv("Cleaned-Text.csv")


def checkPink(sentence):
    if 'pink' in sentence:
        return 1
    else:
        return 0

# Code retrieved from https://dev.to/rodolfoferro/sentiment-analysis-on-trumpss-tweets-using-python-


def analyze_sentiment(post):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(post)
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1


df['contains_pink'] = df.Post.apply(lambda x: checkPink(x))

# These are the target blogs we want to analyze
pinkBlogs = df[df['contains_pink'] == 1]

# These are the blogs that will serve as our baseline
# nonPinkBlogs = df[df['contains_pink'] == 0]

pinkBlogs['SA'] = np.array([analyze_sentiment(post)
                            for post in pinkBlogs['Post']])

pos_thoughts = 0
neu_thoughts = 0
neg_thoughts = 0

for index, row in pinkBlogs.iterrows():
    if row['SA'] > 0:
        pos_thoughts += 1
    if row['SA'] == 0:
        neu_thoughts += 1
    if row['SA'] < 0:
        neg_thoughts += 1

y = len(pinkBlogs('Post'))
print(y)
# print(pinkBlogs)

import numpy as np
import pandas as pd
from textblob import TextBlob


df = pd.read_csv("Cleaned-Text.csv")

df['post-id'], df['post-no'] = df['id'].str.split('-', 1).str
cols = df.columns.tolist()

a, b = cols.index('post-id'), cols.index('date')
cols[b], cols[a] = cols[a], cols[b]

a, b = cols.index('post-no'), cols.index('post')
cols[b], cols[a] = cols[a], cols[b]

cols.remove('id')

df = df[cols]

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

# To see the raw data, retrieve the polarity

def retrieve_polarity(post):

    analysis = TextBlob(post)
    return analysis.sentiment.polarity

#######################################################
#######################################################

# Create a column evaluating if the post contains Pink
df['contains_pink'] = df.post.apply(lambda x: checkPink(x))

# These are the target blogs we want to analyze
pinkBlogs = df[df['contains_pink'] == 1]

# This these ids are important because these people discuss pink in their blogs
idsToAnalyze = []

for index, row in pinkBlogs.iterrows():
    if row['post-id'] not in idsToAnalyze:
        idsToAnalyze.append(row['post-id'])

print(idsToAnalyze)

pinkBlogs['SA'] = np.array([analyze_sentiment(post)
                            for post in pinkBlogs['post']])

pinkBlogs['Polarity'] = [retrieve_polarity(post) for post in pinkBlogs['post']]

pinkBlogs.to_csv("Pink-Blogs.csv")

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

print("Percentage of positive posts: {}%".format(pos_thoughts*100/len(pinkBlogs['post'])))
print("Percentage of neutral posts: {}%".format(neu_thoughts*100/len(pinkBlogs['post'])))
print("Percentage of negative posts: {}%".format(neg_thoughts*100/len(pinkBlogs['post'])))

# These are the blogs that will serve as our baseline
nonPinkBlogs = df[df['contains_pink'] == 0]

# Only keep the blogs that discuss Pink
nonPinkBlogs = nonPinkBlogs[nonPinkBlogs['post-id'].isin(idsToAnalyze)]

nonPinkBlogs['SA'] = np.array([analyze_sentiment(post)
                            for post in nonPinkBlogs['post']])

nonPinkBlogs['Polarity'] = [retrieve_polarity(post) for post in nonPinkBlogs['post']]

nonPinkBlogs.to_csv("Non-Pink-Blogs.csv")

pos_thoughts = 0
neu_thoughts = 0
neg_thoughts = 0

for index, row in nonPinkBlogs.iterrows():
    if row['SA'] > 0:
        pos_thoughts += 1
    if row['SA'] == 0:
        neu_thoughts += 1
    if row['SA'] < 0:
        neg_thoughts += 1

print("################################")

print("Percentage of positive posts: {}%".format(pos_thoughts*100/len(nonPinkBlogs['post'])))
print("Percentage of neutral posts: {}%".format(neu_thoughts*100/len(nonPinkBlogs['post'])))
print("Percentage of negative posts: {}%".format(neg_thoughts*100/len(nonPinkBlogs['post'])))

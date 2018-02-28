import numpy as np
import pandas as pd
from textblob import TextBlob

# Functions

def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val < 0 else 'green'
    return 'color: %s' % color


pinkBlogs = pd.read_csv("Pink-Blogs.csv")
nonPinkBlogs = pd.read_csv("Non-Pink-Blogs.csv")

# Editing the Pink Columns
pinkCols = pinkBlogs.columns.tolist()

pinkCols.remove('contains_pink')
pinkCols.remove('SA')
pinkCols.remove('date')
pinkCols.remove('Unnamed: 0')

pinkBlogs = pinkBlogs[pinkCols]

# Editing the Non-Pink Columns
nonPinkCols = nonPinkBlogs.columns.tolist()


nonPinkCols.remove('date') 
nonPinkCols.remove('post')
nonPinkCols.remove('contains_pink')
nonPinkCols.remove('SA')
nonPinkCols.remove('Unnamed: 0')
nonPinkCols.remove('post-no')

nonPinkBlogs = nonPinkBlogs[nonPinkCols]
 

# Get the baseline for the Non Pink Blogs

meanPolarityByID = nonPinkBlogs.groupby(['post-id']).mean()

for index, row in meanPolarityByID.iterrows():
    pinkBlogs.loc[pinkBlogs['post-id'] == index, 'polarity-baseline'] = row['Polarity']

pinkBlogs['polarity-difference'] =  pinkBlogs['Polarity'] - pinkBlogs['polarity-baseline'] 
pinkBlogs['polarity-delta'] = (pinkBlogs['polarity-difference'] / pinkBlogs['polarity-baseline']) * 100

pinkBlogs.Polarity = pinkBlogs.Polarity.round(4)
pinkBlogs['polarity-baseline'] = pinkBlogs['polarity-baseline'].round(4)
pinkBlogs['polarity-difference'] = pinkBlogs['polarity-difference'].round(4)
pinkBlogs['polarity-delta'] = pinkBlogs['polarity-delta'].round(2)



pinkBlogs = pinkBlogs.sort_values(by=['post-id','post-no'], ascending=True)



pinkBlogs.to_csv("Polarity-Analysis.csv")

pinkBlogsPolarity = pinkBlogs.sort_values(by='Polarity', ascending=False)

pinkBlogsPolarity.to_csv("Polarity-Analysis-By-Polarity.csv")

pinkBlogsDateAnalysis = pinkBlogs.sort_values(by=['year', 'month', 'day'], ascending=True)

pinkBlogsDateAnalysis.to_csv("Polarity-Analysis-Year.csv")



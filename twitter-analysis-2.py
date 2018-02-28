import tweepy
import twitterPrivate
import xlsxwriter

auth = tweepy.OAuthHandler(twitterPrivate.consumer_key, twitterPrivate.consumer_secret)
auth.set_access_token(twitterPrivate.access_token_key, twitterPrivate.access_token_secret)

api = tweepy.API(auth)

tweets = []

public_tweets = api.search("#PinkRibbon", "en")
for tweet in public_tweets:
    tweets.append(tweet.text)


workbook = xlsxwriter.Workbook('tweets.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for tweet in tweets:
    worksheet.write(row, col, tweet)
    row += 1

workbook.close()
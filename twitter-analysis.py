import twitter
import twitterPrivate


api = twitter.Api(consumer_key= twitterPrivate.consumer_key, consumer_secret= twitterPrivate.consumer_secret, access_token_key= twitterPrivate.access_token_key, access_token_secret= twitterPrivate.access_token_secret)

response = api.GetSearch(term="PinkRibbon") 

for tweet in response:
    print(tweet.text)
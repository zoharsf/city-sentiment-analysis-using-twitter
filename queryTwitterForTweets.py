from datetime import datetime

import tweepy
from prettytable import PrettyTable
from textblob import TextBlob
from release.credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def queryTwitterForTweets(geocode):
    i = 1
    scoreSum = 0
    prettyTable = PrettyTable()
    prettyTable.field_names = ["Count", "ID", "Date", "Text", "Score"]

    for tweet in tweepy.Cursor(api.search, q="*", count=200, geocode=geocode, lang="en").items(100):
        tweetId = tweet.id
        tweetDate = datetime.strptime(str(tweet.created_at)[:10], '%Y-%m-%d').strftime('%d-%m-%Y')
        tweetText = tweet.text
        tweetScore = round(TextBlob(tweetText).sentiment.polarity, 4)
        prettyTable.add_row([i, tweetId, tweetDate, tweetText, tweetScore])
        i = i + 1
        scoreSum = scoreSum + tweetScore
    print(prettyTable)
    return scoreSum / i

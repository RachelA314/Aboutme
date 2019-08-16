'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

tweetSearch = 'Automation'
tweetList = [tweetData + tb]
combinedTweets = ""
for tweet in tweetData:
    tweetBlob = TextBlob(tweet["text"])

# Continue your program below!

# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)

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

# Continue your program below!

# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.polarity)

#Create a polarity list (this list stores positive and negative numbers which tell us about tweet)
polarity_list = []


subjectivity_list = []

for tweet in tweetData:
    tweetBlob = TextBlob(tweet["text"])
    polarity_list.append(tweetBlob.polarity)

    subjectivity_list.append(tweetBlob.subjectivity)

'''sum = 0
for polarity in polarity_list:
    sum = sum + polarity
    print(sum)

avgPolarity = sum/len(polarity_list)
print("The average polarity is: %f " %(avgPolarity))

sub_sum = 0
for subjectivity in subjectivity_list:
    sub_sum = sub_sum + subjectivity

avgSubjectivity = sub_sum/len(subjectivity_list)
print("The average subjectivity is: %f " %(avgSubjectivity))'''
print(polarity_list)
#print(subjectivity_list)

#This is a histogram for Twitter Data
'''
#Create the graph
plt.hist(polarity_list, bins = [-1.1, -.75, -0.5, -0.25, 0, 0.25, 0.50, 0.75, 1.1])
plt.xlabel('Polarities')
plt.ylabel('Number of Tweets')
plt.title('Tweet Polarity')
plt.axis([-1.1,1.1,0,100])
plt.grid(True)
plt.show() #shows our graph'''


#Creating a Word Cloud with TwitterData

#initilizaing a variable called 'combinedTweets' which is an empty string that will hold all of the tweets in tweetData
combinedTweets = ""
for tweet in tweetData:
    combinedTweets += tweet['text']

tweetBlob = TextBlob(combinedTweets)

#print(dir(tweetBlob))

wordsToFiller = ["about", "https","say", "make", "from", "be", "an", "our", "got","as", "your", "see", "that", "us", "but", "we","at", "and", "of", "with", "you","is", "to", "for", "by", "it","in", "the", "thing", "will", "could", "automation"]

filteredDictionary = dict()

#point of for loop is to filter words in our big tweet

for word in tweetBlob.words:
    #the following if-statement are conditions for what types of words I want in my word cloud

    #skip small words
    if len(word) < 2:
        continue

    #skip words with random characters or numbers
    if not word.isalpha():
        continue

    #skip words in filler list
    if word.lower() in wordsToFiller:
        continue

    filteredDictionary[word.lower()] = tweetBlob.word_counts[word.lower()]

#Create the word Cloud

#this is the word cloud variable
wordCloud = WordCloud().generate_from_frequencies(filteredDictionary)
plt.imshow(wordCloud, interpolation= 'bilinear')
plt.axis("off")

#this shows our Cloud
plt.show()

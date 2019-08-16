'''
In this program, we print out all the text data from our Twitter JSON file.

'''
import json

#Open JSON file. Tag file as "r" read only because we are only
#looking at the data.
tweetFile = open("../TwitterData/tweets_small.json","r")

#we use the JSON file to get data from the file as JSON data
tweetData = json.load(tweetFile)

#Close the file now that we have locally stored the data
tweetFile.close()

#Print the data of the ONE tweet
#The [0] denotes the *first* tweet object
print("Tweet id:", tweetData[0]["id"])

#Print text of first object
print("Tweet text: ", tweetData[0]["text"])

#Print out "text" key in JSON file
for idx in range(len(tweetData)):
    print("Tweet text: " + tweetData[idx]["text"])

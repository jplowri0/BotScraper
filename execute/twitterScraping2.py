from tweepy import OAuthHandler
#from tweepy.streaming import StreamListener
import tweepy
import json
import pandas as pd
import csv
import re
from textblob import TextBlob
import string
import preprocessor as p
import os
import time

#REFERENCE: https://medium.com/python-in-plain-english/scraping-tweets-with-tweepy-python-59413046e788


# Twitter credentials
# Obtain them from your twitter developer account
consumer_key = "CONSUMER KEY HERE" #Enter your consumer key here. Use "quotations"
consumer_secret = "CONSUMER SECRET HERE" #Enter your consumer secret here. Use "quotations"
access_key = "ACCESS KEY HERE" #Enter your ACCESS KEY here. Use "quotations"
access_secret = "ACCESS SECRET HERE" #Enter your ACCESS SECRET here. Use "quotations"

# Pass your twitter credentials to tweepy via its OAuthHandler
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def scraptweets(search_words, date_since, date_until, numTweets, numRuns):
    print("Scraping Tweets ....")
    # Define a for-loop to generate tweets at regular intervals
    # We cannot make large API call in one go. Hence, let's try T times

    # Define a pandas dataframe to store the date: !!!!!!!!!!!!!!!!!editing this df table to reflect the added Pull values added below in the for tweets in tweet_list below. This must refelct the table below also.
    db_tweets = pd.DataFrame(columns = ['id','username', 'acctdesc', 'location', 'language', 'following', 'followers', 'totaltweets', 'usercreatedts', 'verified',  'tweetcreatedts', 'retweetcount', 'favouritecount', 'text', 'hashtags', 'profilePic']
                                )
    program_start = time.time()
    for i in range(0, numRuns):
        # We will time how long it takes to scrape tweets for each run:
        start_run = time.time()

        # Collect tweets using the Cursor object
        # .Cursor() returns an object that you can iterate or loop over to access the data collected.
        # Each item in the iterator has various attributes that you can access to get information about each tweet
        tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since, until=date_until, tweet_mode='extended').items(numTweets)# Store these tweets into a python list #Free
        #tweets = tp.Cursor(api.search_full_archive,environment_name='you_env_name_here', query=search_words, fromDate=date_since).items(numTweets)#Premium
        tweet_list = [tweet for tweet in tweets]# Obtain the following info (methods to call them out):
        # When adding new features here, need to add a column in the tables above and below. Around Lines: 35 and 79.
        # user.screen_name - twitter handle
        # user.description - description of account
        # user.location - where is he tweeting from
        # user.friends_count - no. of other users that user is following (following)
        # user.followers_count - no. of other users who are following this user (followers)
        # user.statuses_count - total tweets by user
        # user.created_at - when the user account was created
        # created_at - when the tweet was created
        # retweet_count - no. of retweets
        # (deprecated) user.favourites_count - probably total no. of tweets that is favourited by user
        # retweeted_status.full_text - full text of the tweet
        # tweet.entities['hashtags'] - hashtags in the tweet# Begin scraping the tweets individually:
        noTweets = 0
        for tweet in tweet_list:# Pull the values. When
            userid = tweet.user.id
            username = tweet.user.screen_name
            acctdesc = tweet.user.description
            location = tweet.user.location
            language = tweet.user.lang
            following = tweet.user.friends_count
            followers = tweet.user.followers_count
            totaltweets = tweet.user.statuses_count
            usercreatedts = tweet.user.created_at
            verified = tweet.user.verified
            tweetcreatedts = tweet.created_at
            retweetcount = tweet.retweet_count
            favouritecount = tweet.favorite_count
            #quotecount = tweet.quote_count
            hashtags = tweet.entities['hashtags']
            profilePic = tweet.user.profile_image_url #This has been added in. REF https://stackoverflow.com/questions/55899641/how-to-get-the-profile-pictures-of-tweets-using-tweepy/55903905
            try:
                text = tweet.retweeted_status.full_text
            except AttributeError:  # Not a Retweet
                text = tweet.full_text# Add the 11 variables to the empty list - ith_tweet:
            ith_tweet = [id, username, acctdesc, location, language, following, followers, totaltweets,
                         usercreatedts, verified, tweetcreatedts, retweetcount, favouritecount, text, hashtags, profilePic]# Append to dataframe - db_tweets. #This needs to reflect the table above.
            db_tweets.loc[len(db_tweets)] = ith_tweet# increase counter - noTweets
            noTweets += 1

        # Run ended:
        end_run = time.time()
        duration_run = round((end_run-start_run)/60, 2)

        print('no. of tweets scraped for run {} is {}'.format(i + 1, noTweets))
        print('time take for {} run to complete is {} mins'.format(i+1, duration_run))

        #time.sleep(920) #15 minute sleep time# Once all runs have completed, save them to a single csv file:
    from datetime import datetime

    # Obtain timestamp in a readable format
    to_csv_timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')

    # Define working path and filename
    #path = os.getcwd()
    #filename = path + '/home/jplow/capstone/code/' + to_csv_timestamp + '_sahkprotests_tweets.csv'

    #path = '/home/jplow/capstone/code/'
    #filename = 'data/scraped.csv'
    filename = saveToFile

    # Store dataframe in csv with creation date timestamp
    db_tweets.to_csv(filename, index = False)

    program_end = time.time()
    print('Scraping has completed!')
    print('Total time taken to scrap is {} minutes.'.format(round(program_end - program_start)/60, 2))

hashtag = input("Enter a hashtag: ")
datesince = input("Enter a start date in YYYY-MM-DD format: ")
dateuntil = input("Enter a end date in YYYY-MM-DD format: ")
howManyTweets = int(input("Enter the number of tweets MAX 2500: "))

# Initialise these variables:
search_words = hashtag
date_since = datesince
date_until = dateuntil
numTweets = howManyTweets
numRuns = 1

saveToFile = 'data/'+dateuntil+'scraped.csv'

# Call the function scraptweets
scraptweets(search_words, date_since, date_until, numTweets, numRuns)

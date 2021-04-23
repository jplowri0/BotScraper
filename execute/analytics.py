import pandas as pd
import re
import numpy as np
import glob

#FOR BOTS
#Removing any Unnamed column. REF /MLDate/merge.py
def startsWith():
    df = pd.read_csv('MLData/bots.csv')
    #df = df.loc[:, ~df.columns.str.startswith('Unnamed')]
    #df = df.loc[:, ~df.columns.str.startswith(' ')]
    df.to_csv('analytics/bots.csv',index=False)
    print('Unamed Columns removed')

#Extracting URLs from the text column to the url column. REF https://stackoverflow.com/questions/44444189/extracting-string-between-special-characters-in-a-csv-column
def urlExtractor(): 
    df = pd.read_csv('analytics/bots.csv')
    df['url'] = df['text'].str.extract(r'(https?://\S+)', expand=False).fillna('No URL')
    df.to_csv('analytics/botsWorking.csv',index=False)
    print('Bot URLs extracted')

#Counting the URLs 
def urlCounter():
    df = pd.read_csv('analytics/botsWorking.csv')
    #Counting URLs REF https://stackoverflow.com/questions/20076195/what-is-the-most-efficient-way-of-counting-occurrences-in-pandas
    print('Counting URLs')
    dfbotcount=df['url'].value_counts()
    dfbotcount.to_csv('analytics/botsURL.csv')
    print('Bot URL count list exported to processing/botsURL.csv')

#Counting the usernames 
def username():
    df = pd.read_csv('analytics/botsWorking.csv')
    #Counting URLs REF https://stackoverflow.com/questions/20076195/what-is-the-most-efficient-way-of-counting-occurrences-in-pandas
    print('Counting usernames')
    df=df['username'].value_counts()
    df.to_csv('analytics/botsUsername.csv')
    print('Bot Username count list exported to analytics/botsUsername.csv')

#Counting the Tweets 
def tweets():
    df = pd.read_csv('analytics/botsWorking.csv')
    #Counting Tweets REF https://stackoverflow.com/questions/20076195/what-is-the-most-efficient-way-of-counting-occurrences-in-pandas
    print('Counting Tweets')
    df=df['text'].value_counts()
    df.to_csv('analytics/botsTweet.csv',)
    print('Bot Tweets count list exported to processing/botsTweet.csv')


def sortColumnByFavourite():
    #Splitting the dataset into classified bot accouts v human classified accounts. 
    #REF https://stackoverflow.com/questions/36192633/python-pandas-split-a-data-frame-based-on-a-column-value
    dfBots = pd.read_csv('analytics/botsWorking.csv')
    #dfHumans = pd.read_csv('output/humans.csv')

    #below we must define the columns in the dataset. Sorting by Sentiment. 
    dfBots.columns = ['id','username','acctdesc','location','language','following','followers','usercreatedts','verified','tweetcreatedts','retweetcount','favouritecount','text','hashtags','profilePic','acctdescWEB','textWEB','ratio','score','username.1','cap','textSent','Sentence','Polarity','Subjectivity','url']
    dfBots=dfBots.sort_values(by=['favouritecount'],ascending=False) #the sort() is depricated. REF https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html


    dfBots.to_csv('analytics/botsFavourites.csv',index=False)

    print('Bot datasets now arranged by Favourite Count')


def sortColumnByRetweet():
    #Splitting the dataset into classified bot accouts v human classified accounts. 
    #REF https://stackoverflow.com/questions/36192633/python-pandas-split-a-data-frame-based-on-a-column-value
    dfBots = pd.read_csv('analytics/botsWorking.csv')
    #dfHumans = pd.read_csv('output/humans.csv')

    #below we must define the columns in the dataset. Sorting by Sentiment. 
    dfBots.columns = ['id','username','acctdesc','location','language','following','followers','usercreatedts','verified','tweetcreatedts','retweetcount','favouritecount','text','hashtags','profilePic','acctdescWEB','textWEB','ratio','score','username.1','cap','textSent','Sentence','Polarity','Subjectivity','url']
    dfBots=dfBots.sort_values(by=['retweetcount'],ascending=False) #the sort() is depricated. REF https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html


    dfBots.to_csv('analytics/botsReTweets.csv',index=False)

    print('Bot datasets now arranged by ReTweet Count')

def hashtagExtract():
    #extracting hashtags from the text columns. 
    #REF https://stackoverflow.com/questions/45874879/extract-hashtags-from-columns-of-a-pandas-dataframe
    df = pd.read_csv('analytics/botsWorking.csv')
    df['hashExtract'] = df.text.str.findall(r'#.*?(?=\s|$)')
    df2 = df['hashExtract']
    df2.to_csv('analytics/botsHashtags.csv')
    print('Hashtags extracted from bots')

def hashtagCounter():
    df = pd.read_csv('analytics/botsHashtags.csv')
    #Counting URLs REF https://stackoverflow.com/questions/20076195/what-is-the-most-efficient-way-of-counting-occurrences-in-pandas
    #Cleaning the hashtags
    df['hashExtract'] = df['hashExtract'].str.replace('[', '', regex=True)
    df['hashExtract'] = df['hashExtract'].str.replace(',', '', regex=True)
    df['hashExtract'] = df['hashExtract'].str.replace(']', '', regex=True)
    df['hashExtract'] = df['hashExtract'].str.replace('\'', '', regex=True)
    df['hashExtract'] = df['hashExtract'].str.replace('"', '', regex=True)

    #Counting indivisual elements in the entire dataframe. 
    df2=df.hashExtract.apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0)
    df2.to_csv('analytics/botsHashtags.csv')

    #Sorting the columns
    df = pd.read_csv('analytics/botsHashtags.csv')
    df.columns = ['','0']
    df=df.sort_values(by=['0'],ascending=False) #the sort() is depricated. REF https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
    df.to_csv('analytics/botsHashtags.csv',index=False)

    print('Bot Hashtags count list exported to processing/botsHashtags.csv')



#FOR Humans
#Removing any Unnamed column. REF /MLDate/merge.py
def startsWithHumans():
    df = pd.read_csv('MLData/humans.csv')
    df = df.loc[:, ~df.columns.str.startswith('Unnamed')]
    df = df.loc[:, ~df.columns.str.startswith(' ')]
    df.to_csv('analytics/humans.csv',index=False)
    print('Human Unamed Columns removed')

#Extracting URLs from the text column to the url column. REF https://stackoverflow.com/questions/44444189/extracting-string-between-special-characters-in-a-csv-column
def urlExtractorHumans(): 
    df = pd.read_csv('analytics/humans.csv')
    df['url'] = df['text'].str.extract(r'(https?://\S+)', expand=False).fillna('No URL')
    df.to_csv('analytics/humansWorking.csv',index=False)
    print('Humans URLs extracted')

#Counting the URLs 
def urlCounterHumans():
    df = pd.read_csv('analytics/humansWorking.csv')
    #Counting URLs REF https://stackoverflow.com/questions/20076195/what-is-the-most-efficient-way-of-counting-occurrences-in-pandas
    print('Counting URLs')
    df=df['url'].value_counts()
    df.to_csv('analytics/humansURL.csv')
    print('Humans URL count list exported to processing/humansURL.csv')

#Counting the usernames 
def usernameHumans():
    df = pd.read_csv('analytics/humansWorking.csv')
    #Counting URLs REF https://stackoverflow.com/questions/20076195/what-is-the-most-efficient-way-of-counting-occurrences-in-pandas
    print('Counting usernames')
    df=df['username'].value_counts()
    df.to_csv('analytics/humansUsername.csv')
    print('Humans Username count list exported to processing/humansUsername.csv')

#Counting the Tweets 
def tweetsHumans():
    df = pd.read_csv('analytics/humansWorking.csv')
    #Counting Tweets REF https://stackoverflow.com/questions/20076195/what-is-the-most-efficient-way-of-counting-occurrences-in-pandas
    print('Counting Tweets')
    df=df['text'].value_counts()
    df.to_csv('analytics/humansTweet.csv')
    print('Humans Tweets count list exported to processing/humansTweet.csv')

def sortColumnByFavouriteHumans():
    #Splitting the dataset into classified bot accouts v human classified accounts. 
    #REF https://stackoverflow.com/questions/36192633/python-pandas-split-a-data-frame-based-on-a-column-value
    dfBots = pd.read_csv('analytics/humansWorking.csv')
    #dfHumans = pd.read_csv('output/humans.csv')

    #below we must define the columns in the dataset. Sorting by Sentiment. 
    dfBots.columns = ['id','username','acctdesc','location','language','following','followers','usercreatedts','verified','tweetcreatedts','retweetcount','favouritecount','text','hashtags','profilePic','acctdescWEB','textWEB','ratio','score','username.1','cap','textSent','Sentence','Polarity','Subjectivity','url']
    dfBots=dfBots.sort_values(by=['favouritecount'],ascending=False) #the sort() is depricated. REF https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html


    dfBots.to_csv('analytics/humansFavourites.csv',index=False)

    print('Humans datasets now arranged by Favourite Count')


def sortColumnByRetweetHumans():
    #Splitting the dataset into classified bot accouts v human classified accounts. 
    #REF https://stackoverflow.com/questions/36192633/python-pandas-split-a-data-frame-based-on-a-column-value
    dfBots = pd.read_csv('analytics/humansWorking.csv')
    #dfHumans = pd.read_csv('output/humans.csv')

    #below we must define the columns in the dataset. Sorting by Sentiment. 
    dfBots.columns = ['id','username','acctdesc','location','language','following','followers','usercreatedts','verified','tweetcreatedts','retweetcount','favouritecount','text','hashtags','profilePic','acctdescWEB','textWEB','ratio','score','username.1','cap','textSent','Sentence','Polarity','Subjectivity','url']
    dfBots=dfBots.sort_values(by=['retweetcount'],ascending=False) #the sort() is depricated. REF https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html


    dfBots.to_csv('analytics/HumansReTweets.csv',index=False)

    print('Humans datasets now arranged by ReTweet Count')

def hashtagExtractHumans():
    #extracting hashtags from the text columns. 
    #REF https://stackoverflow.com/questions/45874879/extract-hashtags-from-columns-of-a-pandas-dataframe
    df = pd.read_csv('analytics/humansWorking.csv')
    df['hashExtract'] = df.text.str.findall(r'#.*?(?=\s|$)')
    df2 = df['hashExtract']
    df2.to_csv('analytics/humansHashtags.csv')
    print('Hashtags extracted from humans')

def hashtagCounterHumans():
    df = pd.read_csv('analytics/humansHashtags.csv')
    #Counting URLs REF https://stackoverflow.com/questions/20076195/what-is-the-most-efficient-way-of-counting-occurrences-in-pandas
    #Cleaning the hashtags
    df['hashExtract'] = df['hashExtract'].str.replace('[', '', regex=True)
    df['hashExtract'] = df['hashExtract'].str.replace(',', '', regex=True)
    df['hashExtract'] = df['hashExtract'].str.replace(']', '', regex=True)
    df['hashExtract'] = df['hashExtract'].str.replace('\'', '', regex=True)
    df['hashExtract'] = df['hashExtract'].str.replace('"', '', regex=True)

    #Counting indivisual elements in the entire dataframe. 
    df2=df.hashExtract.apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0)
    df2.to_csv('analytics/humansHashtags.csv',)

    #Sorting the columns
    df = pd.read_csv('analytics/humansHashtags.csv')
    df.columns = ['','0']
    df=df.sort_values(by=['0'],ascending=False) #the sort() is depricated. REF https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
    df.to_csv('analytics/humansHashtags.csv',index=False)

    print('Humans Hashtags count list exported to processing/botsHashtags.csv')
    print("")
    print("Bots and Humans have been classified")


#call bot processing functions
startsWith()
urlExtractor()
urlCounter()
username()
tweets()
sortColumnByFavourite()
sortColumnByRetweet()
hashtagExtract()
hashtagCounter()

#call humans processing functions
startsWithHumans()
urlExtractorHumans()
urlCounterHumans()
usernameHumans()
tweetsHumans()
sortColumnByFavouriteHumans()
sortColumnByRetweetHumans()
hashtagExtractHumans()
hashtagCounterHumans()

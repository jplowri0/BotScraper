import pandas as pd
import glob
import numpy as np
import re
import os 
import csv
from textblob import TextBlob

#This function should remove columns beginning with REF https://stackoverflow.com/questions/43822349/drop-column-that-starts-with
#It loops through all csvs in the directory #https://swcarpentry.github.io/python-novice-gapminder/14-looping-data-sets/
def startsWIthLoop():
    #for filename in glob.glob('botometer/BotScores.csv'):
    df = pd.read_csv('botometer/BotScores.csv')
    df = df.loc[:, ~df.columns.str.startswith('Unnamed')]
    #df=df.drop(['Unnamed: 0'], axis='columns', inplace=True)
    df.to_csv('MLData/mlApplied.csv',index=False)
    print('Unamed Columns removed')




#CSV file concatentation REF https://www.freecodecamp.org/news/how-to-combine-multiple-csv-files-with-8-lines-of-code-265183e0854/
def combine():
    extension = 'csv'
    all_filenames = [i for i in glob.glob('MLData/*.{}'.format(extension))]
    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    combined_csv.to_csv( "MLData/mlApplied.csv", index=False, encoding='utf-8-sig')
    print('CSVs Merged')

#This function removes any rows with offset errors REF https://stackoverflow.com/questions/26771471/remove-rows-where-column-value-type-is-string-pandas
def rowRemover(): 
    df = pd.read_csv('botometer/BotScores.csv')
    #df['cap'] = pd.to_numeric(df['cap'], errors='coerce')
    #df = df.dropna(subset=['cap']).set_index('cap')
    df['cap'] = df['cap'].apply(lambda x: pd.to_numeric(x, errors = 'coerce')).dropna()

    df.to_csv(r'MLData/mlApplied.csv', index = False)
    print('offset row errors removed')

#This function creates a new column called 'textSent' which will have all punctuation and special chars removed
#REF https://stackoverflow.com/questions/51778480/remove-certain-string-from-entire-column-in-pandas-dataframe

def textSent():
    df = pd.read_csv("MLData/mlApplied.csv")
    df['textSent'] = df['text'] #copying the text column and textSent column
    
    #the lines below are substituting the char for a space or nothing. 
    df['textSent'] = df['textSent'].str.replace('@', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('.', ' ', regex=True)
    df['textSent'] = df['textSent'].str.replace(',', ' ', regex=True)
    df['textSent'] = df['textSent'].str.replace('#', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('&', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('!', ' ', regex=True)
    df['textSent'] = df['textSent'].str.replace('%', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('(', '', regex=True)
    df['textSent'] = df['textSent'].str.replace(')', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('-', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('_', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('+', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('=', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('"', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('\'', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('\\', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('/', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('?', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('>', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('<', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('|', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('[', '', regex=True)
    df['textSent'] = df['textSent'].str.replace(']', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('{', '', regex=True)
    df['textSent'] = df['textSent'].str.replace('}', '', regex=True)
    df['textSent'] = df['textSent'].str.replace(':', ' ', regex=True)
    df['textSent'] = df['textSent'].str.replace(';', ' ', regex=True)
    
    #Removing line breaks. REF https://stackoverflow.com/questions/44227748/removing-newlines-from-messy-strings-in-pandas-dataframe-cells
    df = df.replace('\n','', regex=True)
    #Export cleaned dataframe to CSV.
    df.to_csv("MLData/mlApplied.csv",index=False)
    print('Tweet column copied and special characters removed')

def sentiment():
    with open("MLData/mlApplied.csv", 'r') as csvfile: #opening the input file.
        rows = csv.reader(csvfile)
        f = open("MLData/mlApplied1.csv", "w") #opening the output file. REF https://stackoverflow.com/questions/25115140/python-only-last-line-is-saved-to-file. Important to open this outside of the loop.
        for row in rows:
            sentence = row[21] #This picks the column.
            blob = TextBlob(sentence)
            sentimentrow = blob.sentiment.polarity #Sentiment Polarity Analysis
            subjectivityrow = blob.sentiment.subjectivity #Subjectivity Polarity Analysis
            f.write(sentence + "," + str(sentimentrow) + "," + str(subjectivityrow) + "\n") #REF https://stackoverflow.com/questions/25115140/python-only-last-line-is-saved-to-file
        f.close() #REF https://stackoverflow.com/questions/25115140/python-only-last-line-is-saved-to-file. Important to close this outside of the loop.


    #Now to add a header to the CSV REF https://stackoverflow.com/questions/28162358/append-a-header-for-csv-file
    with open("MLData/mlApplied1.csv",newline='') as header:
        r = csv.reader(header)
        data = [line for line in r]
    with open("MLData/mlApplied1.csv",'w',newline='') as header:
        w = csv.writer(header)
        w.writerow(['Sentence','Polarity','Subjectivity'])
        w.writerows(data)


    #Below we are stats from the CSV` REF https://stackoverflow.com/questions/50165953/python-dataframes-describing-a-single-column
    df3 = pd.read_csv("MLData/mlApplied1.csv",engine='python') #Converting a csv to a panda dataframe. Need to use engine=python as per https://www.shanelynn.ie/pandas-csv-error-error-tokenizing-data-c-error-eof-inside-string-starting-at-line/
    describePolarity = df3['Polarity'].describe() #Computing the common statistics of the Polarity column in the dataframe/
    print(describePolarity)
    print(df3)

    #Headers seem to be doubled up. Below is dropping row 1 (2nd). 
    df = pd.read_csv("MLData/mlApplied1.csv")
    df4 =df.drop(0) #Drop row 2. REF https://chrisalbon.com/python/data_wrangling/pandas_dropping_column_and_rows/
    df4.to_csv("MLData/mlApplied2.csv",index=False)


    #Concatenating the two dataframes. Adding the Stage3 computed df to the OG inputFile. 

    df1 = pd.read_csv("MLData/mlApplied.csv")
    df2 = pd.read_csv("MLData/mlApplied2.csv")

    df3 = pd.concat([df1,df2], axis=1)
    df3.to_csv("MLData/mlAppliedWithSentiment.csv",index=False)

    print('Sentiment Analysis Applied')

def rowSort():
    #Arrangeing the CSV bot score "cap" column into numnerical order. 
    #REF https://stackoverflow.com/questions/33172203/how-do-i-sort-data-from-a-csv-file-numerically-in-python

    df = pd.read_csv('MLData/mlAppliedWithSentiment.csv') #import

    #below we must define the columns in the dataset. 
    df.columns = ['id','username','acctdesc','location','language','following','followers','usercreatedts','verified','tweetcreatedts','retweetcount','favouritecount','text','hashtags','profilePic','acctdescWEB','textWEB','ratio','score','username.1','cap','textSent','Sentence','Polarity','Subjectivity']
    #df.coluumns=['score']
    df=df.sort_values(by=['cap'],ascending=False) #the sort() is depricated. REF https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html


    df.to_csv('MLData/mlAppliedWithSentimentSorted.csv',index=False)

    print('Rows arranged by CAP score')

def accountTypeSplit():
    #Splitting the dataset into classified bot accouts v human classified accounts. 
    #REF https://stackoverflow.com/questions/36192633/python-pandas-split-a-data-frame-based-on-a-column-value
    df = pd.read_csv('MLData/mlAppliedWithSentiment.csv')
    dfBots = df[df['cap'] >= 0.8]
    dfHumans = df[df['cap'] < 0.8]

    #Arranging the columns 
    dfBots.columns = ['id','username','acctdesc','location','language','following','followers','usercreatedts','verified','tweetcreatedts','retweetcount','favouritecount','text','hashtags','profilePic','acctdescWEB','textWEB','ratio','score','username.1','cap','textSent','Sentence','Polarity','Subjectivity']
    dfBots=dfBots.sort_values(by=['cap'],ascending=False) #the sort() is depricated. REF https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html

    #Arranging the columns 
    dfHumans.columns = ['id','username','acctdesc','location','language','following','followers','usercreatedts','verified','tweetcreatedts','retweetcount','favouritecount','text','hashtags','profilePic','acctdescWEB','textWEB','ratio','score','username.1','cap','textSent','Sentence','Polarity','Subjectivity']
    dfHumans=dfHumans.sort_values(by=['cap'],ascending=False) #the sort() is depricated. REF https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html

    #Export into CSVs. 
    dfBots.to_csv('MLData/bots.csv',index=False)
    dfHumans.to_csv('MLData/humans.csv',index=False)
    print('Bot Dataset created bots.csv')
    print('Human Dataset created humans.csv')

def sortColumnBySentiment():
    #Splitting the dataset into classified bot accouts v human classified accounts. 
    #REF https://stackoverflow.com/questions/36192633/python-pandas-split-a-data-frame-based-on-a-column-value
    dfBots = pd.read_csv('MLData/bots.csv')
    dfHumans = pd.read_csv('MLData/humans.csv')

    #below we must define the columns in the dataset. Sorting by Sentiment. 
    dfBots.columns = ['id','username','acctdesc','location','language','following','followers','usercreatedts','verified','tweetcreatedts','retweetcount','favouritecount','text','hashtags','profilePic','acctdescWEB','textWEB','ratio','score','username.1','cap','textSent','Sentence','Polarity','Subjectivity']
    dfBots=dfBots.sort_values(by=['Polarity'],ascending=False) #the sort() is depricated. REF https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html

    #below we must define the columns in the dataset. Sorting by Sentiment. 
    dfHumans.columns = ['id','username','acctdesc','location','language','following','followers','usercreatedts','verified','tweetcreatedts','retweetcount','favouritecount','text','hashtags','profilePic','acctdescWEB','textWEB','ratio','score','username.1','cap','textSent','Sentence','Polarity','Subjectivity']
    dfHumans=dfHumans.sort_values(by=['Polarity'],ascending=False) #the sort() is depricated. REF https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html


    dfBots.to_csv('MLData/bots.csv',index=False)
    dfHumans.to_csv('MLData/humans.csv',index=False)

    print('Bot and Human datasets now arranged by Sentiment Score')

#Now we run the script.
if __name__ == '__main__':

    startsWIthLoop() 
    rowRemover()
    textSent()
    sentiment()
    rowSort()
    accountTypeSplit()
    sortColumnBySentiment()
    
  
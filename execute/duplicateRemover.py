import pandas as pd
import numpy as np

df = pd.read_csv('botometer/BotScores.csv')

#this line drops duplicate rows. The chosen column was the tweet created timestamp. 
#REF https://www.interviewqs.com/ddi-code-snippets/drop-duplicate-rows-pandas
df = df.drop_duplicates(subset='tweetcreatedts', keep="first")

df.to_csv('botometer/BotScores.csv', index=False)

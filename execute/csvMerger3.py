import pandas as pd


#importing the two CSVs as dataframes. 
df1 = pd.read_csv("data/cleaning/cleanedA.csv")
df2 = pd.read_csv("botometer/idBots.csv")

#REF https://stackoverflow.com/questions/40468069/merge-two-dataframes-by-index/40468090
#the line below is combining the two csvs into one. 
df3=pd.concat([df1, df2], axis=1)

#REF https://stackoverflow.com/questions/20297317/python-dataframe-pandas-drop-column-using-int
#The line removes the middle column 
#df3=df3.drop(df3.columns[1], axis=1)

#This line exports the dataframe as CSVi
df3.to_csv(r'botometer/BotScores.csv', index = False)


import pandas as pd
import glob
import numpy as np
import re

#>>>>>>>>>>>>MERGER<<<<<<<<<<<<<<<<<<<

#REF https://www.programmersought.com/article/31515733850/

#This function merges the CSVs
def hebing(csv_list, outputfile):
    for inputfile in csv_list:
        f = open(inputfile)
        data = pd.read_csv(f)
        data.to_csv(outputfile, mode='a', index=False)
    print('Complete the merge')

#This fucntion is ignored.
def quchong(file):
    df = pd.read_csv(file, header=None)
    datalist = df.drop_duplicates()
    datalist.to_csv('result_new.csv', index=False, header=False)
    #print('complete deduplication')

#REF https://stackoverflow.com/questions/55551746/find-and-remove-duplicates-in-a-csv-file
#This function removes any duplicated rows in the CSVs
def deduplication():
    def unique_everseen(iterable, key=None):
        seen = set()
        seen_add = seen.add
        if key is None:
            for element in filterfalse(seen.__contains__, iterable):
                seen_add(element)
                yield element
        else:
            for element in iterable:
                k = key(element)
                if k not in seen:
                    seen_add(k)
                    yield element

    with open("data/cleaning/result.csv", "r") as file:
        lines = []
        for line in file:
            lines.append(line.strip("\n").split(","))

    with open("data/cleaning/results.csv", "w") as file:
        for line in unique_everseen(lines, key=frozenset):
            file.write(",".join(line)+"\n")
    print('complete deduplication')

#Now we run the script.
if __name__ == '__main__':
    csv_list = glob.glob('data/*.csv')
    output_csv_path = 'data/cleaning/result.csv'
    print(csv_list)
    hebing(csv_list, output_csv_path)
    deduplication()


#>>>>>>>>>>>>Row Remover<<<<<<<<<<<<<<<<<<<

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)

#This line imports the csv
#REF https://stackoverflow.com/questions/53668421/replace-a-string-value-with-nan-in-pandas-data-frame-python
df = pd.read_csv("data/cleaning/result.csv")

#df['profilePicOffset'] = df['profilePic']

#df['profilePicOffset'] = df['profilePicOffset'].str.contains('http')

#df.loc[df['profilePicOffset'] == True]

#df = df[df.totaltweets != 'False']

df['totaltweets'] = pd.to_numeric(df['totaltweets'], errors='coerce')
df = df.dropna(subset=['totaltweets']).set_index('totaltweets')
#df["totaltweets"].loc[df["totaltweets"].isnull()] = 0   # nan
#df = df[df.totaltweets != 'True']


#print(df2['totaltweets']

print('Offset error corrected')

df.to_csv(r'data/cleaning/resultsA.csv', index = False)

#>>>>>>>>>>>>Row Remover<<<<<<<<<<<<<<<<<<<

# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)

#This line imports the csv
#REF https://stackoverflow.com/questions/53668421/replace-a-string-value-with-nan-in-pandas-data-frame-python
data = pd.read_csv("data/cleaning/resultsA.csv")

#Cretaing a new column to print a 1 if https is present in tweet and accdesc
#REF https://stackoverflow.com/questions/32675861/copy-all-values-in-a-column-to-a-new-column-in-a-pandas-dataframe
data['acctdescWEB'] = data['acctdesc']
data['textWEB'] = data['text']

#Here the a certain string is being converted to NaN.
data["profilePic"] = data["profilePic"].replace('http://abs.twimg.com/sticky/default_profile_images/default_profile_normal.png', np.nan)


#NOW HERE WE CONVERT NaNs TO ZERO's AND STRINGS TO 1.
# REF https://stackoverflow.com/questions/37543647/how-to-replace-all-non-nan-entries-of-a-dataframe-with-1-and-all-nan-with-0
data["profilePic"].loc[~data["profilePic"].isnull()] = 1  # not nan
data["profilePic"].loc[data["profilePic"].isnull()] = 0   # nan

#The next three convert blank space of location to a 0 and the presence of any string to a 1.
data["location"] = data["location"].replace('', np.nan)
data["location"].loc[~data["location"].isnull()] = 1  # not nan
data["location"].loc[data["location"].isnull()] = 0   # nan

#The next three convert blank space of language to a 0 and the presence of any string to a 1.
data["language"] = data["language"].replace('', np.nan)
data["language"].loc[~data["language"].isnull()] = 1  # not nan
data["language"].loc[data["language"].isnull()] = 0   # nan

#The next three convert blank space of acctdesc to a 0 and the presence of any string to a 1.
data["acctdesc"] = data["acctdesc"].replace('', np.nan)
data["acctdesc"].loc[~data["acctdesc"].isnull()] = 1  # not nan
data["acctdesc"].loc[data["acctdesc"].isnull()] = 0   # nan

#Converting acctdescWEB to 1 if https is present.
#REF https://thecodingbot.com/check-if-a-column-contains-specific-string-in-a-pandas-dataframe/
data['acctdescWEB'] = data['acctdescWEB'].str.contains('http')
data['textWEB'] = data['textWEB'].str.contains('http')

#Converting NaNs to 0's.
data["acctdescWEB"].loc[data["acctdescWEB"].isnull()] = 0   # nan
data["textWEB"].loc[data["textWEB"].isnull()] = 0   # nan

#Removing numbers from verified columns
#data['verified'] = data[~data['verified'].str.contains('^\d$')]

#Converting Trues and False to 1 and 0. REF https://stackoverflow.com/questions/17383094/how-can-i-map-true-false-to-1-0-in-a-pandas-dataframe
data['acctdescWEB'] = data['acctdescWEB'].astype(int)
data['textWEB'] = data['textWEB'].astype(int)
data['verified'] = data['verified'].astype(int)

#Computing the ratio of followers to following.
data["ratio"] = data["following"] / data["followers"]

#REF https://datatofish.com/export-dataframe-to-csv/
#Exporting the dataframe to a new CSV.
data.to_csv(r'data/cleaning/cleanedA.csv', index = False)

print("Dont worry about the slice warning above.")
print('Dataset cleaned. ')

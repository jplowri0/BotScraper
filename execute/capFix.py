#THere was issues with the cap scores. This script correct the scores below so it 
#can be read by pandas CSV reader. The scores below threw errors. 

#REF https://stackoverflow.com/questions/17140886/how-to-search-and-replace-text-in-a-file

with open('botometer/cap.txt', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('0.0,', '0.00')

filedata = filedata.replace('1.0,', '1.00')

# Write the file out again
with open('botometer/cap.txt', 'w') as file:
  file.write(filedata)
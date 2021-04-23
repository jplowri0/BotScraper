 #!/bin/bash

echo "Checking usernames against Botometer......."
echo "This may take a while ..... Fix yourself a coffee"

#REF https://stackoverflow.com/questions/13794873/how-to-export-all-print-to-a-txt-file-in-python
#This line runs the multiBotCheck then exports the output to a txt file. 
python3 inputCSVmultiBotCHeck.py > botometer/output.txt

echo "Formatting......"


#REF https://unix.stackexchange.com/questions/283407/can-sed-save-its-output-to-a-file
#This line removes the TweepError Not Authorized lines. 
sed -i 's/.*TweepError.*//ig' botometer/output.txt

#REF https://serverfault.com/questions/252921/how-to-remove-empty-blank-lines-from-a-file-in-unix-including-spaces
#This line removes any blank lines left behind from the above sed command. 
sed -i '/^$/d' botometer/output.txt

cp botometer/output.txt botometer/overall.txt
cp botometer/output.txt botometer/screenName.txt
cp botometer/output.txt botometer/cap.txt

#REF https://unix.stackexchange.com/questions/243207/how-can-i-delete-everything-until-a-pattern-and-everything-after-another-pattern
#REF https://stackoverflow.com/questions/27922910/how-to-extract-multiple-text-and-numbers-from-a-string-using-sed

#This gets the first overall extracted
overall=$(sed -i 's/^.*\(english.: ..astroturf.: ..., .fake_follower.: ..., .financial.: ..., .other.: ..., .overall.......\).*/\1/' botometer/overall.txt) 

#This now extracts the only overall
overall1=$(sed -i 's/^.*\(overall.......\).*$/\1/' botometer/overall.txt) 

#REF https://stackoverflow.com/questions/8356958/sed-just-trying-to-remove-a-substring
#this removes the text preceding the two digits.
overall2=$(sed -i 's/^overall.: //' botometer/overall.txt)

#Converting the text files to csv
cp botometer/overall.txt botometer/overall.csv

#This line will extract the screen name text with extras. 
name=$(sed -i 's/^.*\(screen_name.*$\).*/\1/' botometer/screenName.txt)

#this removes the screen_name text.
name1=$(sed -i 's/^screen_name.: .//' botometer/screenName.txt)

#this removes the remaining rubbish text.
name1=$(sed -i 's/.}}}$//' botometer/screenName.txt)

#Converting the text files to csv
cp botometer/screenName.txt botometer/screenName.csv

#This gets the first cap extracted
cap=$(sed -i 's/^.*\(cap.: ..english.: ....\).*/\1/' botometer/cap.txt) 

#This now extracts the only overall
cap1=$(sed -i 's/^.*\(....$\).*$/\1/' botometer/cap.txt) 

#Run the cap fix file. Overriding the 0.0, with 0.00
python3 capFix.py

#Converting the text files to csv
cp botometer/cap.txt botometer/cap.csv

#Executing the python script to combine the above csvs
python3 csvMerger.py

#REF https://stackoverflow.com/questions/28162358/append-a-header-for-csv-file
#This line apples the header to the idBots.csv file
sed -i 1i"score,username,cap" botometer/idBots.csv

#This script now combines the idBots.csv and the output from the cleaner.py script in /code/cleaner.py
python3 csvMerger3.py

#Cleaning the scores to above 4.8 threshold as 1 and below as 0. 
#python3 scoreCleaner.py


#Remove duplicates
python3 duplicateRemover.py


echo "Done!"

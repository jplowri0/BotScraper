#!/bin/bash


#export files

mv data/cleaning/resultsA.csv export/rawData.csv
mv analytics/*.csv export/

echo "Files have been exported"
echo "!!!!Dont forget to move files out of the export folder"
echo "before your next export!!!!"
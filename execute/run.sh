#!/bin/bash

#This script sequences all the code from the Analyse command. 


./botometer.sh

python3 applyML.py

python3 analytics.py







 #!/bin/bash

echo " $(tput setaf 6)_           _     ____                      "           
echo "| |__   ___ | |_  / ___|  ___ _ __ __ _ _ __   ___ _ __ "
echo "| '_ \ / _ \| __| \___ \ / __| '__/ _\` | '_ \ / _ \ '__\ "
echo "| |_) | (_) | |_   ___) | (__| | | (_| | |_) |  __/ | "  
echo "|_.__/ \___/ \__| |____/ \___|_|  \__,_| .__/ \___|_|"   
echo "                                       |_|  "            

echo "$(tput sgr 0)"
echo "This program uses several python libraries to scrape a term from twitter using Tweepy, "
echo "then uses the Machine Learning via the Botometer project to classify bot accounts."
echo ""
echo "You will be able to perform some analytics on your data scrape."
echo ""


echo "This project has been written by John Plowright 2021."
echo "Code References have been added as comments."
echo ""
chmod +x execute/twitterScraping2.py
chmod +x execute/run.sh
chmod +x execute/export.sh
chmod +x execute/purge.sh

cd execute

 for ((i=0; ;++i)); do #This for loop, loops infitely until the user enters option 8 and exits the program. REF https://stackoverflow.com/questions/31625794/infinite-for-loop-with-bashs
        echo "$(tput setaf 1) Choose an Option:$(tput sgr 0)" 
        echo "$(tput setaf 2)1. Please read instructions" 
        echo "2. Scrape Twitter"
        echo "3. Merge and Clean"
        echo "4. Classify Bot or Humans"
        echo "5. Export"
        echo "6. Clean"
        echo "7. Exit"
        read option;
        case $option in #The case options allows for user to make a choice. 
        1) cat execute/instructions.txt;;
        2) python3 twitterScraping2.py;;
        3) python3 mergeAndClean.py;;
        4) ./run.sh;;
        5) ./export.sh;;
        6) ./purge.sh;;
        7) echo "Goodbye"
            exit 0;; #user deciding to quit the program. 
        *) echo "Bad input" #user entering an invalid option - such as "11"
        esac
    done

echo "This project has been written by John Plowright 2021"
echo "Code References have been commented in"
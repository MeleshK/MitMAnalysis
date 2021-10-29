#!/bin/bash
printf "\n$1 copying to capture.txt"
cat $1 >> capture.txt
printf "\nRemoving '\000'"
tr < capture.txt -d '\000' > capturefixed.txt
printf "\nTaking backup"
cat capturefixed.txt >> backup.txt
printf "\nPerforming analysis"
python3 ./AnalysisMain.py
printf "\nAnalysis Complete"
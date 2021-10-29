#!/bin/bash
printf "$1 copying to capture.txt"
cat $1 >> capture.txt
printf "Removing '\000'"
tr < capture.txt -d '\000' > capturefixed.txt
printf "Taking backup"
cat capturefixed.txt >> backup.txt
printf "Performing analysis"
python3 ./AnalysisMain.py
printf "Analysis Complete"
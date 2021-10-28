#!/bin/bash

#Checks to see if mitmweb is already running
#If so, kills the processes
PROCESS=$(ps aux | grep mitmweb | tr -s " " | cut -d " " -f 2,11,12)
echo "$PROCESS" | while read -r line
do
	echo $line
	PSNAME=$(echo "$line" | cut -d " " -f 3)

    if [[ "$PSNAME" == *"/mitm"* ]]; then
        PSNUM=$(echo "$line" | cut -d " " -f 1)
        echo "Shutting down process $PSNUM $PSNAME"
		sudo kill -9 $PSNUM
    fi
done

echo "" > stream.txt
echo "" > capture.txt

#Starts mitmweb and outputs to stream.txt
mitmdump --anticomp --anticache --set block_global=false --set flow_detail=3 --mode transparent --ssl-insecure --verbose -s mitmdecode.py > stream.txt  2>/dev/null &

#Every 10  seconds, put stream into capture
#Then empty the contents to stream
while [ 0 -lt 1 ]
do
	sleep 10s
	cat stream.txt >> capture.txt
	tr < capture.txt -d '\000' > capturefixed.txt
	cat capturefixed.txt >> backup.txt
	echo "" > stream.txt # empty stream file
	python3 ./AnalysisMain.py
	echo "" > capture.txt # empty capture file
done

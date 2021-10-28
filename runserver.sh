#!/bin/bash

#Checks to see if mitmweb is already running
#If so, kills the processes
PROCESS=$(ps aux | grep mitmweb | tr -s " " | cut -d " " -f 2,11,12)
echo "$PROCESS" | while read -r i
do
    PSNAME=$(echo "$i" | cut -d " " -f 3)

    if [[ "$PSNAME" == *"/mitm"* ]]; then
        PSNUM=$(echo "$i" | cut -d " " -f 1)
        echo "Shutting down process $PSNUM $PSNAME"
		sudo kill -9 $PSNUM
    fi
done

echo "" > stream.txt
echo "" > capture.txt

#Starts mitmweb and outputs to stream.txt
 mitmweb --anticomp --anticache --set block_global=false --set flow_detail=3 --mode transparent --showhost --web-host 10.0.0.31 --web-port 9090 --ssl-insecure --verbose
#~/mitm/mitmdump --anticomp --anticache --set block_global=false --set flow_detail=3 --verbose --mode transparent --ssl-insecure -s mitmdecode.py > stream.txt  2>/dev/null &

#Every 10  seconds, put stream into capture
#Then empty the contents to stream
while [ 0 -lt 1 ]
do
	sleep 10s
	cat stream.txt >> capture.txt
	tr < capture.txt -d '\000' > capturefixed.txt
	cat capturefixed.txt >> backup.txt
	echo "" > stream.txt
	python3 ./AnalysisMain.py
	echo "" > capture.txt
done

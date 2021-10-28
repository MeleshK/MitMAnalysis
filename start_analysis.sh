#!/bin/bash

mitmweb --anticomp --anticache --ignore-hosts '^(?:(?!google).)*$' --set block_global=false --set flow_detail=3 --mode transparent --showhost --web-host 0.0.0.0 --web-port 9090 --no-web-open-browser --ssl-insecure --no-web-open-browser --verbose -s mitmdecode.py > stream.txt &

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
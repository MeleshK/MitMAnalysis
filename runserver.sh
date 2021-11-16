#!/bin/bash

#terminate mitmdump if already running.
try:
  kill "$(pgrep mitmdump)"

echo "" > stream.txt
echo "" > capture.txt
now=$(date +"%Y_%m_%d_%H_%M")

#Starts mitmdump and outputs to output.txt
mitmdump --anticomp --anticache --set block_global=false --set flow_detail=3 --mode transparent --showhost --save-stream-file "/project/mitmproxy_$now.cap" --set stream_large_bodies=5m --ssl-insecure --verbose -s mitmdecode.py &

#Every 10  seconds, put stream into capture
#Then empty the contents to stream
while [ 0 -lt 1 ]
do
	sleep 10s
	cat stream.txt >> capture.txt
	tr < capture.txt -d '\000' > capturefixed.txt
	cat capturefixed.txt >> "backup-$now.txt"
	echo "" > stream.txt
	python3 ./AnalysisMain.py
	echo "" > capture.txt
done

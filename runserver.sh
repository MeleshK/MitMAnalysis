#!/bin/bash
mitmweb --anticomp --anticache --ignore-hosts '^(?:(?!google).)*$' --set block_global=false --set flow_detail=3 --mode transparent --showhost --web-host 0.0.0.0 --web-port 9090 --save-stream-file ~/mitmproxy-`date +%s`-flow.cap --ssl-insecure --no-web-open-browser --ssl-insecure --no-web-open-browser --verbose -s mitmdecode.py &
#!/bin/bash
mitmweb --anticomp --anticache --listen-host 0.0.0.0 --mode transparent --showhost --webport 9999 --save-stream-file ~/mitmproxy-`date +%s`-flow.cap --ssl-insecure &
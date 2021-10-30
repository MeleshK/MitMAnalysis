#!/bin/bash
mitmweb -s shutdown.py
sleep 10s
sudo pkill mitmweb
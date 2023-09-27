#!/bin/bash

# Google IT Automation with Python - Bash Scripting, Advanced Command Interaction

for logfile in /var/log/*log; do
  echo "Processing: $logfile"
  cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done

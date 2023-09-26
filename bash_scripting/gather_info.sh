#!/bin/bash

# Google IT Automation with Python - Bash Scripting, Creating Bash Scripts

line="------------------------------------------------"
echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"

#!/bin/bash

# Google IT Automation with Python - Bash Scripting, While Loops in Bash Scripts

n=1
while [ $n -le 5 ]; do
    echo "Iteration number $n"
    ((n+=1))
done
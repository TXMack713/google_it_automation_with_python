#!/bin/bash

# Google IT Automation with Python - Bash Scripting, While Loops in Bash Scripts

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
  sleep $n
  ((n+=1))
  echo "Retry #$n"
done;

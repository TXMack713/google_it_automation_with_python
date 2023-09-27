#!/bin/bash

# Google IT Automation with Python - Bash Scripting, For Loops in Bash Scripts

for file in *.HTM; do
  name=$(basename "$file" .HTM)
  mv "$file" "$name.html"
done

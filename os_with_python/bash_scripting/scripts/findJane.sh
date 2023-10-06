#!/bin/bash

# Google IT Automation with Python - Bash Scripting, Qwiklabs Assessment

#> oldFiles.txt

# Find all files with the username "jane"

>oldFiles.txt

example=`grep " jane " ../data/list.txt | cut -d ' ' -f 3`
echo $example
# Get the names of all the files that match the username 'Jane'
files="`grep " jane " ../data/list.txt | cut -d ' ' -f 3`"

for line in $files; do
#  echo "Line"
  echo $line
#  echo "Line printed"
  for file in ../data/*; do
    if [[ "$file" == *"$line"* ]];
    then
      echo "True"
      echo "$file" >>oldFiles.txt
    fi
  done
done


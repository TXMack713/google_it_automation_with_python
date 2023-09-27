#!/bin/bash

# Google IT Automation with Python - Bash Scripting, Qwiklabs Assessment

#> oldFiles.txt

# Find all files with the username "jane"

> oldFiles.txt

# Get the names of all the files that
files="`grep " jane " ../data/list.txt | cut -d ' ' -f 1-3`"

if [[ $files == "jane" ]]
then
  "$files" >> oldFiles.txt
fi

for file in ../data/*; do
#  grep "/jane_" $file >> oldFiles.txt
 if [[ "$file" == *"jane_"* ]]
 then
   echo "$file" >> ../data/oldFiles.txt
  fi
done

# Search all lines of each file that contain the name " jane " and save the file names into a variable called files

#for line in *Files.txt; do
files=grep " jane_ " ../data/oldFiles.txt | cut -d "/" -f 3
echo $files



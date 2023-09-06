#Q1

def create_python_script(filename):
  import os
  comments = "# Start of a new Python program"
  with open(filename, "w")as file:
    file.write(comments)
    file.close()
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))

#Q2

import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    working_dir = os.getcwd()
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, "w") as file:
    pass

  # Return the list of files in the new directory
  os.chdir(working_dir)
  dir_list = []
  for name in os.listdir(directory):
    dir_list.append(name)

  return dir_list

print(new_directory("PythonPrograms", "script.py"))

#Q4

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open(filename, "w"):
    pass

  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  converted = str(datetime.datetime.fromtimestamp(timestamp)).split()
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  return ("{}".format(converted[0]))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd

#Q5

import os
def parent_directory():
  # Create a relative path to the parent
  # of the current working directory
  #os.getcwd()
  #print("test")
  path = os.getcwd()
  #print(path)
  #print("Absolute path: " + str(os.path.abspath(path)))
  path_arr = path.split("/")
  #print("Path array: " + str(path_arr))
  parent = path_arr[len(path_arr) - 2]
  #print("Parent: " + parent)
  relative_parent = os.path.join("../", parent)
  parent_arr = path_arr
  parent_arr.pop()
  print(parent_arr)

  # Return the absolute path of the parent directory
  return "/".join(parent_arr)

print(parent_directory())
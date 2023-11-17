#!/usr/bin/env python3
# Google IT Automation with Python
# Automating Real-World Tasks with Python
# Module 1 - Qwiklabs Assessment: Scale and convert images using PIL

import PIL
from PIL import Image
import os
import shutil


orig_path = os.getcwd()
print(orig_path)

path_array = orig_path.split("/")
path_array.pop()
path_array.pop()
root_path = "/".join(path_array)

if os.path.exists(orig_path+"/images"):
    os.chdir("images")

os.chdir(root_path)
print(os.getcwd())
new_dir = "opt"
opt_path = root_path + "/opt"

try:
    if os.path.exists(opt_path):
        os.chdir(new_dir)
    else:
        os.mkdir(new_dir)
        os.chdir(new_dir)
except:
    print("Directory already exists")
    os.chdir(new_dir)

new_folder = "icons"
icons_path = opt_path + "/icons"

try:
    if os.path.exists(icons_path):
        os.chdir(new_folder)
    else:
        os.mkdir(new_folder)
        os.chdir(new_folder)
except:
    print("Directory already exists")
    os.chdir(new_folder)

new_path = os.getcwd()
print("New path: " + new_path)
print(os.getcwd())

for root, directory, files in os.walk(orig_path):
    for file in files:
        full_file = os.path.join(root, file)
        print("Full file: " + full_file)
        if os.path.isfile(full_file):
            # new_file = new_path + "/" + file
            try:
                with Image.open(full_file) as im:
                    im.convert("RGB").rotate(90).resize((128, 128)).save(full_file, "JPEG")
                new_location = new_path + "/" + file
                shutil.move(full_file, new_location)
            except PIL.UnidentifiedImageError:
                pass


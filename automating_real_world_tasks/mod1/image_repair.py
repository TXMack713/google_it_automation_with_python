#!/usr/bin/env python3
import PIL
# Google IT Automation with Python
# Automating Real-World Tasks with Python
# Module 1 - Qwiklabs Assessment: Scale and convert images using PIL

from PIL import Image
import os
import shutil


os.chdir("images")
orig_path = os.getcwd()
print(orig_path)
os.chdir("..")
print(os.getcwd())
new_dir = "opt"
try:
    os.mkdir(new_dir)
    os.chdir(new_dir)
except:
    print("Directory already exists")
    os.chdir(new_dir)

new_folder = "icons"

try:
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
            new_file = new_path + "/" + file + ".jpeg"
            try:
                with Image.open(full_file) as im:
                    im.convert("RGB").rotate(90).resize((128, 128)).save(new_file, "JPEG")
                # new_location = new_path + "/" + file +
                # shutil.copy(full_file, new_location)
            except PIL.UnidentifiedImageError:
                pass


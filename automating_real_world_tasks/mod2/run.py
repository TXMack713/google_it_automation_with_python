#!/usr/bin/env python3
# Google IT Automation with Python
# Automating Real-World Tasks with Python
# Module 2 - Qwiklabs Assessment: Process Text Files with Python Dictionaries and Upload to Running Web Service

import os
import requests
import json

print(os.getcwd())
os.chdir("feedback")
review_path = os.getcwd()
print("Review path: " + review_path)

# Walk the review feedback directory
# Parse the feedback turn it into a python dictionary
# Serialize the data and post it to the database

review_list = []
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))
for root, directory, files in os.walk(review_path):
    for file in files:
        review_dict = {}
        title = ""
        username = ""
        date = ""
        feedback = ""
        full_file = os.path.join(root, file)

        if os.path.isfile(full_file) and full_file.endswith(".txt"):
            print("Full file: " + full_file)
            # new_file = new_path + "/" + file
            with open(full_file) as review:
                title = review.readline().strip()
                username = review.readline().strip()
                date = review.readline().strip()
                feedback_array = review.readlines()
                for x in feedback_array:
                    feedback += x + " "
                review_dict["title"] = title
                review_dict["username"] = username
                review_dict["date"] = date
                review_dict["feedback"] = feedback.strip()
                print("Review_dict:")
                print(review_dict)
                review_list.append(review_dict)
        else:
            continue

        print("\n")

print(review_list)

'''
#!/usr/bin/env python3

# Module 2 - Process Text Files with Python Dictionaries and Uploading to Running Web Services

import os
import requests
import json


file_list = os.listdir("/data/feedback")
print(file_list)

for file in file_list:
    full_file = "/data/feedback/" + file
    print("Full file path: " + full_file)
    review_dict = {}
    title = ""
    username = ""
    date = ""
    feedback = ""

    with open(full_file) as review:
        title = review.readline().strip()
        name = review.readline().strip()
        date = review.readline().strip()
        feedback_array = review.readlines()
        for x in feedback_array:
            feedback += x + " "
        review_dict["title"] = title
        review_dict["name"] = name
        review_dict["date"] = date
        review_dict["feedback"] = feedback.strip()
        print("Review_dict:")
        print(review_dict)
        
    response = requests.post("http://34.74.99.104/feedback/", data=review_dict)    
    if response.ok:    
        response.request.url    
        continue    
    else:    
        raise Exception("POST failed with status code {}".format(response.status_code))    
    # print(response)    
    # review_list.append(review_dict)      
'''

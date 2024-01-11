#!/usr/bin/env python3
# Google IT Automation with Python
# Automating Real-World Tasks with Python
# Module 3 - Mail Practice


from email.message import EmailMessage
import os.path
import mimetypes
import smtplib


message = EmailMessage()
print("Printing the message:")
print(message)

sender = "me@example.com"
recipient = "you@example.com"
message['From'] = sender
message['To'] = recipient
print("Printing the message:")
print(message)

message['Subject'] = "Greetings from {} to {}".format(sender, recipient)
print("Printing the message:")
print(message)

body = """Hey there!

I'm learning to send emails using Python!"""
message.set_content(body)
print("Printing the message:")
print(message)

# Adding an example image to learn about MIME types
print(os.getcwd())
os.chdir("../../../../..")
print(os.getcwd())
# os.chdir("Pictures/")
print(os.getcwd())
attachment_path = "Pictures/example.jpg"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)
# MIME type should be image/jpeg

mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
# should be image
print(mime_subtype)
# should be jpeg

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))

print(message)

# Using SMMTP to send email
# mail_server = smtplib.SMTP('localhost')
# mail_server = smtplib.SMTP_SSL('smtp.example.com')
import os

# this is a relative to file_manager.py
# so when we run this program from different directory its no
# longer relative to the directory that it currently is in
# email_txt = os.path.join("templates","email.txt")

# so make an absolute path to email.txt
# 1. get absolute path of the file that we are on
this_file_path = os.path.abspath(__file__) 
# -->/home/rajish/Python/CodingEntrepreneurs/Reference/files/file_manager.py

#  2. set base directory in root of the project
# will get top level directory name of this_file_path
BASE_DIR = os.path.dirname(this_file_path)
# /home/rajish/Python/CodingEntrepreneurs/Reference/files

ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)
# /home/rajish/Python/CodingEntrepreneurs/Reference

# with this you can run code from any directory and will not get FileNotFoundError.
email_txt = os.path.join(BASE_DIR, "templates/email.txt")

content = ""

with open(email_txt, 'r') as f:
    content = f.read()
    
print(content.format(name = "Rajish"))
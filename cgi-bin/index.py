#!/usr/bin/python3
print("Content-Type: text/html\n")

import cgi
import cgitb
import os

cgitb.enable()

file_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(file_dir)
with open(os.path.join(parent_dir, 'static.html'), 'r') as f:
    static_html = f.read()
formatted_html = static_html#.format(iso_list=iso_list)

print(formatted_html)

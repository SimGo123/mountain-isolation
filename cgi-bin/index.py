#!/usr/bin/python3

print("Content-Type: text/html\n")

import cgi
import cgitb

import sys
import os
try:
    import wiki2
except Exception as e:
    print("Content-Type: text/plain")
    print()
    print(f"Error importing wiki2: {e}")
    sys.exit(1)

cgitb.enable()  # Enable CGI error reporting

iso_list = []

form = cgi.FieldStorage()
input_text = form.getvalue("inputText")

if input_text:
    # iso_list = [{'name': 'Piz Morteratsch', 'height': 3751.0, 'coords': [46.4025, 9.90166667], 'isolation': 1.6, 'next_high': 'Piz Bernina'}, {'name': 'Piz Bernina', 'height': 4048.0, 'coords': [46.38222222, 9.90805556], 'isolation': 138.0, 'next_high': 'Finsteraarhorn'}, {'name': 'Finsteraarhorn', 'height': 4274.0, 'coords': [46.53722222, 8.12611111], 'isolation': 51.65, 'next_high': 'Nadelhorn'}, 
	# {'name': 'Nadelhorn', 'height': 4327.0, 'coords': [46.10888889, 7.86388889], 'isolation': 1.7, 'next_high': 'Dom [Berg]'}, {'name': 'Dom [Berg]', 'height': 4546.0, 'coords': [46.094, 7.85883333], 'isolation': 16.6, 'next_high': 'Nordend [Berg]'}, {'name': 'Nordend [Berg]', 'height': 4608.0, 'coords': [45.94166667, 7.87], 'isolation': 0.575, 'next_high': 'Grenzgipfel'}, {'name': 'Grenzgipfel', 'height': 4617.0, 'coords': [45.936719, 7.868561], 'isolation': 0.1, 'next_high': 'Dunantspitze'}, 
	# {'name': 'Dunantspitze', 'height': 4631.0, 'coords': [45.93694444, 7.86777778], 'isolation': 0.1, 'next_high': 'Dufourspitze'}, {'name': 'Dufourspitze', 'height': 4634.0, 'coords': [45.9369, 7.86675], 'isolation': 78.2, 'next_high': 'Mont Blanc de Courmayeur'}, {'name': 'Mont Blanc de Courmayeur', 'height': 4748.0, 'coords': [45.828695, 6.86843], 'isolation': 0.6, 'next_high': 'Mont Blanc'}, {'name': 'Mont Blanc', 'height': 4805.59, 'coords': [45.832544, 6.864325], 'isolation': 2812.0, 'next_high': 'Kjukjurtlju'}, {'name': 'Kjukjurtlju', 'height': 4978.0, 'coords': [43.34138889, 42.40611111], 'isolation': 2.7, 'next_high': 'Elbrus'}, {'name': 'Elbrus', 'height': 5642.0, 'coords': [43.35254, 42.437875], 'isolation': 2472.7, 'next_high': 'Pik Agasis'}, 
    # {'name': 'Pik Agasis', 'height': 5877.0, 'coords': [39.014128, 71.504167], 'isolation': 29.45, 'next_high': 'Pik Moskau'}, {'name': 'Pik Moskau', 'height': 6785.0, 'coords': [38.948517, 71.834732], 'isolation': 15.7, 'next_high': 'Pik Ismoil Somoni'}, {'name': 'Pik Ismoil Somoni', 'height': 7495.0, 'coords': [38.9426, 72.0151], 'isolation': 278.0, 'next_high': 'Kongur Jiubie'},
    # {'name': 'Kongur Jiubie', 'height': 7530.0, 'coords': [38.615796, 75.195643], 'isolation': 10.52, 'next_high': 'Kongur'}, {'name': 'Kongur', 'height': 7649.0, 'coords': [38.5933, 75.31269], 'isolation': 240.0, 'next_high': 'Batura Sar'}, {'name': 'Batura Sar', 'height': 7795.0, 'coords': [36.510329, 74.522602], 'isolation': 62.98, 'next_high': 'Distaghil Sar'}, {'name': 'Distaghil Sar', 'height': 7885.0, 'coords': [36.325702, 75.188224], 'isolation': 129.27, 'next_high': 'K2'}, {'name': 'K2', 'height': 8611.0, 'coords': [35.88333333, 76.51666667], 'isolation': 1315.77, 'next_high': 'Mount Everest'}, {'name': 'Mount Everest', 'height': 8848.0, 'coords': [27.98823, 86.92501]}]
    iso_list = wiki2.loop(input_text)

file_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(file_dir)
with open(os.path.join(parent_dir, 'static.html'), 'r') as f:
    static_html = f.read()
formatted_html = static_html.format(iso_list=iso_list)

print(formatted_html)

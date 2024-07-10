#!/usr/bin/python3

print("Content-Type: application/json\n")

import cgi
import cgitb
import requests
import json

cgitb.enable()

def search_wikipedia(query):
    url = "https://de.wikipedia.org/w/api.php"
    params = {
        "action": "opensearch",
        "format": "json",
        "search": query,
        "limit": 5
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        response.raise_for_status()

form = cgi.FieldStorage()
query = form.getvalue('query')

if query:
    results = search_wikipedia(query)
    print(json.dumps(results))
else:
    print(json.dumps({'error': 'Missing query parameter'}))

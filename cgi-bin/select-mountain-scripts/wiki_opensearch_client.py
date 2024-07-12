#!/usr/bin/python3

print("Content-Type: application/json\n")

import cgi
import cgitb
import requests
import json

cgitb.enable()

form = cgi.FieldStorage()
query = form.getvalue('query')

if not query:
    print(json.dumps({'error': 'Missing query parameter'}))
    exit(-1)

# Query to get top 5 search results for given query
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
else:
    response.raise_for_status()

print(json.dumps(data))

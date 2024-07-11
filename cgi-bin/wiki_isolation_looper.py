#!/usr/bin/python3

import cgi
import cgitb
import sys
import json
import wikipedia
from bs4 import BeautifulSoup
from bs4.element import NavigableString

cgitb.enable()

print("Content-Type: text/event-stream")
print()
sys.stdout.flush()

def send_error_msg(error_msg):
    print(f"event: errorx\ndata: {error_msg}")
    print()
    sys.stdout.flush()

def ignore_display_none(tag):
    # Function to filter out elements with display: none
    if tag.has_attr('style'):
        styles = tag['style'].split(';')
        for style in styles:
            if style.strip().startswith('display:none'):
                return True
    return False

def get_info_table_dict(html: str):
    # Parse the HTML table using BeautifulSoup
    html = str(html).replace('<br />',' ')
    soup = BeautifulSoup(html, 'html.parser')
    [tag.extract() for tag in soup.find_all(ignore_display_none)]

    table = soup.find('table', class_='infobox')

    if not table:
        send_error_msg("Page doesn't contain table")
        return {}

    # Extract column headers from the table
    headers = []
    header_row = table.find('tr')
    for header in header_row.find_all(['th', 'td']):
        headers.append(header.get_text().strip())

    # Extract data rows from the table
    data_rows = []
    rows = table.find_all('tr')[1:]  # Skip the header row
    i = 0
    for row in rows:
        data_row = []
        cells = row.find_all(['th', 'td'])
        j = 0
        for cell in cells:
            cell_content = []
            imgs = [desc for desc in cell.descendants if desc.name=='img']
            if any(imgs):
                if i == 0:
                    data_row.append('image')
                    cell_content.append(f"https:{imgs[0]['src']}")
            else:
                for child in cell.children:
                    if child.name == 'a' and j > 0 and child.has_attr('title'):
                        cell_content.append(f"[[{child['title']}]]")
                    elif child.name == 'img':
                        cell_content.append(f"img {child['src']}")
                    elif isinstance(child, NavigableString):
                        cell_content.append(str(child).replace('\n',''))
                    else:
                        cell_content.append(child.getText().replace('\n',''))
            data_row.append(''.join(cell_content))
            j += 1
        data_rows.append(data_row)
        i += 1

    data_dict = {}
    for row in data_rows:
        if len(row) == 2 and row[0] and row[0] != 'Koordinaten':
            data_dict[row[0]] = row[1]

    return data_dict


def height_to_meters(height_str: str):
    # Expect: '3751\xa0m\xa0ü.\xa0M.'
    splitted = height_str.split('\xa0')
    height_num = float(splitted[0].replace('.','').replace(',','.'))
    if splitted[1].startswith('m'):
        return height_num
    else:
        send_error_msg(f"Unexpected unit '{splitted[1]}' in str '{height_str}'")

def isolation_to_meters(isolation_str: str):
    # Expected: '62,98\xa0km →\xa0[[Distaghil Sar]]'
    splitted = isolation_str.split('\xa0')
    isolation_num = float(splitted[0].replace('.','').replace(',','.'))
    if splitted[1].startswith('km'):
        return isolation_num * 1000
    else:
        send_error_msg(f"Unexpected unit {splitted[1]} in str '{isolation_str}'")
    

# Loop till no other higher mountain can be found
# This either terminates at Mt. Everest (hopefully) or at an undocumented peak
def loop(mtn_name, prev=[]):
    # print(mtn_name + ', ')
    wikipedia.set_lang('de')
    try:
        page = wikipedia.WikipediaPage(mtn_name)
    except Exception as e:
        send_error_msg('Error fetching wiki page: ' + str(e))
        return prev
    info_dict = get_info_table_dict(page.html())

    try:
        dec_coords = page.coordinates
    except:
        wikipedia.set_lang('en')
        page_en = wikipedia.WikipediaPage(mtn_name)
        dec_coords = page_en.coordinates
    float_coords = [float(dec_coords[0]), float(dec_coords[1])]

    if 'Höhe' in info_dict:
        height = height_to_meters(info_dict['Höhe'])
    else:
        send_error_msg(f"'{mtn_name}' is probably not a page about a mountain")
        return prev
    if not all(k in info_dict for k in ['Dominanz']):
        prev.append([
            {'name':mtn_name, 'height':height, 'coords':float_coords}, 
            info_dict])
        return prev
    isolation_data = str(info_dict['Dominanz'])
    isolation_dist = isolation_to_meters(isolation_data)
    try:
        next_highest = isolation_data.split('[[')[1].split(']]')[0]
        prev.append([
            {'name':mtn_name, 'height':height, 'coords':float_coords, 'isolation_dist':isolation_dist, 'next_high':next_highest}, 
            info_dict])
        
        print(f"event: step\ndata: {json.dumps(prev)}")
        print()
        sys.stdout.flush()
    except Exception as e:
        send_error_msg(f"Can't parse '{isolation_data}' (probably no link)")
        prev.append([
            {'name':mtn_name, 'height':height, 'coords':float_coords, 'isolation_dist':isolation_dist}, 
            info_dict])
        return prev
    if '(Seite nicht vorhanden)' in next_highest:
        send_error_msg(f"Page doesn't exist: '{next_highest}'")
        return prev
    
    return loop(next_highest, prev)

form = cgi.FieldStorage()
mountain = form.getvalue('mountain')
iso_list = loop(mountain)

# iso_list = loop('Kongur')

# with open(os.path.join(parent_dir, 'iso_list_example.txt'), 'r') as f:
#     list_str = f.read()
#     iso_list = ast.literal_eval(list_str)

print(f"event: return\ndata: {json.dumps(iso_list)}")
print()
sys.stdout.flush()

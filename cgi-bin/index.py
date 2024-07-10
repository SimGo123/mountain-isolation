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

cgitb.enable()

iso_list = []

form = cgi.FieldStorage()
input_mountain = form.getvalue("mountain")

if input_mountain:
    # iso_list = [{'name': 'Piz Morteratsch', 'height': 3751.0, 'coords': [46.4025, 9.90166667], 'isolation': 1.6, 'next_high': 'Piz Bernina'}, {'name': 'Piz Bernina', 'height': 4048.0, 'coords': [46.38222222, 9.90805556], 'isolation': 138.0, 'next_high': 'Finsteraarhorn'}, {'name': 'Finsteraarhorn', 'height': 4274.0, 'coords': [46.53722222, 8.12611111], 'isolation': 51.65, 'next_high': 'Nadelhorn'}, 
	# {'name': 'Nadelhorn', 'height': 4327.0, 'coords': [46.10888889, 7.86388889], 'isolation': 1.7, 'next_high': 'Dom [Berg]'}, {'name': 'Dom [Berg]', 'height': 4546.0, 'coords': [46.094, 7.85883333], 'isolation': 16.6, 'next_high': 'Nordend [Berg]'}, {'name': 'Nordend [Berg]', 'height': 4608.0, 'coords': [45.94166667, 7.87], 'isolation': 0.575, 'next_high': 'Grenzgipfel'}, {'name': 'Grenzgipfel', 'height': 4617.0, 'coords': [45.936719, 7.868561], 'isolation': 0.1, 'next_high': 'Dunantspitze'}, 
	# {'name': 'Dunantspitze', 'height': 4631.0, 'coords': [45.93694444, 7.86777778], 'isolation': 0.1, 'next_high': 'Dufourspitze'}, {'name': 'Dufourspitze', 'height': 4634.0, 'coords': [45.9369, 7.86675], 'isolation': 78.2, 'next_high': 'Mont Blanc de Courmayeur'}, {'name': 'Mont Blanc de Courmayeur', 'height': 4748.0, 'coords': [45.828695, 6.86843], 'isolation': 0.6, 'next_high': 'Mont Blanc'}, {'name': 'Mont Blanc', 'height': 4805.59, 'coords': [45.832544, 6.864325], 'isolation': 2812.0, 'next_high': 'Kjukjurtlju'}, {'name': 'Kjukjurtlju', 'height': 4978.0, 'coords': [43.34138889, 42.40611111], 'isolation': 2.7, 'next_high': 'Elbrus'}, {'name': 'Elbrus', 'height': 5642.0, 'coords': [43.35254, 42.437875], 'isolation': 2472.7, 'next_high': 'Pik Agasis'}, 
    # {'name': 'Pik Agasis', 'height': 5877.0, 'coords': [39.014128, 71.504167], 'isolation': 29.45, 'next_high': 'Pik Moskau'}, {'name': 'Pik Moskau', 'height': 6785.0, 'coords': [38.948517, 71.834732], 'isolation': 15.7, 'next_high': 'Pik Ismoil Somoni'}, {'name': 'Pik Ismoil Somoni', 'height': 7495.0, 'coords': [38.9426, 72.0151], 'isolation': 278.0, 'next_high': 'Kongur Jiubie'},
    # {'name': 'Kongur Jiubie', 'height': 7530.0, 'coords': [38.615796, 75.195643], 'isolation': 10.52, 'next_high': 'Kongur'}, {'name': 'Kongur', 'height': 7649.0, 'coords': [38.5933, 75.31269], 'isolation': 240.0, 'next_high': 'Batura Sar'}, {'name': 'Batura Sar', 'height': 7795.0, 'coords': [36.510329, 74.522602], 'isolation': 62.98, 'next_high': 'Distaghil Sar'}, {'name': 'Distaghil Sar', 'height': 7885.0, 'coords': [36.325702, 75.188224], 'isolation': 129.27, 'next_high': 'K2'}, {'name': 'K2', 'height': 8611.0, 'coords': [35.88333333, 76.51666667], 'isolation': 1315.77, 'next_high': 'Mount Everest'}, {'name': 'Mount Everest', 'height': 8848.0, 'coords': [27.98823, 86.92501]}]
    
    iso_list = [[{'name': 'Piz Morteratsch', 'height': '3751\xa0m\xa0ü.\xa0M.', 'coords': [46.4025, 9.90166667], 'isolation': '1,6\xa0km →\xa0[[Piz Bernina]]', 'next_high': 'Piz Bernina'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/PizMorteratsch.jpg/300px-PizMorteratsch.jpg', 'Höhe': '3751\xa0m\xa0ü.\xa0M.', 'Lage': '[[Kanton Graubünden]], [[Schweiz]]', 'Gebirge': '[[Berninagruppe]] der [[Bernina-Alpen]] AVE 66', 'Dominanz': '1,6\xa0km →\xa0[[Piz Bernina]]', 'Schartenhöhe': '324\xa0m ↓\xa0Fuorcla Prievlusa', 'Erstbesteigung': '[[11. September]] [[1858]], C. Brügger, P. Gensler, Karl Emmermann und Angelo Klaingutti', 'Normalweg': 'Von Westen von der [[Tschiervahütte]] über Vadrettin da Tschierva und Nordrücken (WS)'}], [{'name': 'Piz Bernina', 'height': '4048\xa0m\xa0ü.\xa0M. [1]', 'coords': [46.38222222, 9.90805556], 'isolation': '138\xa0km →\xa0[[Finsteraarhorn]][2]', 'next_high': 'Finsteraarhorn'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Piz_Bernina_Aug_2008_close.jpg/300px-Piz_Bernina_Aug_2008_close.jpg', 'Höhe': '4048\xa0m\xa0ü.\xa0M. [1]', 'Lage': '[[Kanton Graubünden]], [[Schweiz]]', 'Gebirge': '[[Berninagruppe]]', 'Dominanz': '138\xa0km →\xa0[[Finsteraarhorn]][2]', 'Schartenhöhe': '2236\xa0m ↓\xa0[[Malojapass]][1]', 'Erstbesteigung': '13. September 1850 durch [[Johann Wilhelm Coaz]], Jon und Lorenz Ragut Tscharner', 'Normalweg': 'Spallagrat von [[Rifugio Marco e Rosa]] (II)'}], [{'name': 'Finsteraarhorn', 'height': '4274\xa0m\xa0ü.\xa0M.', 'coords': [46.53722222, 8.12611111], 'isolation': '51,65\xa0km →\xa0[[Nadelhorn]]', 'next_high': 'Nadelhorn'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Aerial_image_of_Finsteraarhorn_%28view_from_the_south%29.jpg/300px-Aerial_image_of_Finsteraarhorn_%28view_from_the_south%29.jpg', 'Höhe': '4274\xa0m\xa0ü.\xa0M.', 'Lage': 'Kantonsgrenze [[Kanton Bern]] und [[Kanton Wallis]], [[Schweiz]]', 'Gebirge': '[[Berner Alpen]]', 'Dominanz': '51,65\xa0km →\xa0[[Nadelhorn]]', 'Schartenhöhe': '2279\xa0m ↓\xa0Westl. [[Simplonpass]]', 'Typ': '[[Karling]]', 'Gestein': '[[Amphibolit]]', 'Erstbesteigung': '16. August 1812 durch Arnold Abbühl, Joseph Bortis und Alois Volken', 'Normalweg': 'über Südwestflanke und Nordwestgrat ZS-'}], [{'name': 'Nadelhorn', 'height': '4327\xa0m\xa0ü.\xa0M.', 'coords': [46.10888889, 7.86388889], 'isolation': '1,7\xa0km →\xa0[[Dom (Berg)]]', 'next_high': 'Dom (Berg)'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/NadelhornFromNE.JPG/300px-NadelhornFromNE.JPG', 'Höhe': '4327\xa0m\xa0ü.\xa0M.', 'Lage': '[[Kanton Wallis]], [[Schweiz]]', 'Gebirge': '[[Mischabel]], [[Walliser Alpen]]', 'Dominanz': '1,7\xa0km →\xa0[[Dom (Berg)]]', 'Schartenhöhe': '207\xa0m ↓\xa0Lenzjoch[1]', 'Erstbesteigung': '16. September 1858 durch [[Franz Andenmatten (Seite nicht vorhanden)]], Baptiste Epiney, Aloys Supersaxo, Joseph Zimmermann', 'Normalweg': 'Nordostgrat vom Windjoch (I, WS)'}], [{'name': 'Dom (Berg)', 'height': '4546\xa0m\xa0ü.\xa0M.', 'coords': [46.094, 7.85883333], 'isolation': '16,6\xa0km →\xa0[[Nordend (Berg)]]', 'next_high': 'Nordend (Berg)'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/DomFromN.jpg/300px-DomFromN.jpg', 'Höhe': '4546\xa0m\xa0ü.\xa0M.', 'Lage': '[[Kanton Wallis]], [[Schweiz]]', 'Gebirge': '[[Mischabel]], [[Walliser Alpen]]', 'Dominanz': '16,6\xa0km →\xa0[[Nordend (Berg)]]', 'Schartenhöhe': '1057\xa0m ↓\xa0Neues Weisstor[1]', 'Erstbesteigung': '11. September [[1858]] von J. Llewellyn Davies, [[Johann Zumtaugwald (Seite nicht vorhanden)]], Johann Kronig und Hieronymous Brantschen', 'Normalweg': 'Nordflanke (II), Gletschertour'}], [{'name': 'Nordend (Berg)', 'height': '4608\xa0m\xa0ü.\xa0M. [1]', 'coords': [45.94166667, 7.87], 'isolation': '0,575\xa0km →\xa0[[Grenzgipfel]]', 'next_high': 'Grenzgipfel'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Nordend_von_der_Dufourspitze.jpg/300px-Nordend_von_der_Dufourspitze.jpg', 'Höhe': '4608\xa0m\xa0ü.\xa0M. [1]', 'Lage': 'Grenze [[Schweiz]]/[[Italien]]', 'Gebirge': '[[Monte Rosa]], [[Walliser Alpen]]', 'Dominanz': '0,575\xa0km →\xa0[[Grenzgipfel]]', 'Schartenhöhe': '89\xa0m ↓\xa0Silbersattel[1]', 'Koordinaten, (CH)': '45°\xa056′\xa030″\xa0N, 7°\xa052′\xa012″\xa0O (633454\xa0/\xa087878)Koordinaten: 45°\xa056′\xa030″\xa0N, 7°\xa052′\xa012″\xa0O; CH1903:\xa0633454\xa0/\xa087878', 'Erstbesteigung': 'T.F. und Edward N.Buxton und J.J. Cowell mit Michel Payot am 26. August 1861[2]', 'Normalweg': 'vom Silbersattel über den Südgrat ([[UIAA]] II)', 'Besonderheiten': 'Höchster Punkt des [[Piemont]]'}], [{'name': 'Grenzgipfel', 'height': '4617\xa0m\xa0ü.\xa0M. [1]', 'coords': [45.936719, 7.868561], 'isolation': '0,1\xa0km →\xa0[[Dunantspitze]][2]', 'next_high': 'Dunantspitze'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/DufourspitzeFromNordendAndNames.jpg/300px-DufourspitzeFromNordendAndNames.jpg', 'Höhe': '4617\xa0m\xa0ü.\xa0M. [1]', 'Lage': 'Grenze [[Piemont]], [[Italien]] / [[Kanton Wallis]], [[Schweiz]]', 'Gebirge': '[[Monte Rosa]], [[Walliser Alpen]]', 'Dominanz': '0,1\xa0km →\xa0[[Dunantspitze]][2]', 'Schartenhöhe': '10\xa0m', 'Koordinaten, (CH)': '45°\xa056′\xa012″\xa0N, 7°\xa052′\xa07″\xa0O (633345\xa0/\xa087328)Koordinaten: 45°\xa056′\xa012″\xa0N, 7°\xa052′\xa07″\xa0O; CH1903:\xa0633345\xa0/\xa087328'}], [{'name': 'Dunantspitze', 'height': '4631\xa0m\xa0ü.\xa0M. [1]', 'coords': [45.93694444, 7.86777778], 'isolation': '0,1\xa0km →\xa0[[Dufourspitze]][2]', 'next_high': 'Dufourspitze'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/DufourspitzeFromNordendAndNames.jpg/300px-DufourspitzeFromNordendAndNames.jpg', 'Höhe': '4631\xa0m\xa0ü.\xa0M. [1]', 'Lage': '[[Kanton Wallis]], [[Schweiz]]', 'Gebirge': '[[Monte Rosa]], [[Walliser Alpen]]', 'Dominanz': '0,1\xa0km →\xa0[[Dufourspitze]][2]', 'Schartenhöhe': '15\xa0m', 'Erstbesteigung': '[[1854]] durch Christopher Smyth, James G. Smyth, Edmund Smyth', 'Normalweg': 'Westgrat vom „Sattel“ oder Südostgrat über den [[Grenzgipfel]]'}], [{'name': 'Dufourspitze', 'height': '4634\xa0m\xa0ü.\xa0M.', 'coords': [45.9369, 7.86675], 'isolation': '78,2\xa0km →\xa0[[Mont Blanc de Courmayeur]]', 'next_high': 'Mont Blanc de Courmayeur'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Dufourspitze_from_Nordend.jpg/300px-Dufourspitze_from_Nordend.jpg', 'Höhe': '4634\xa0m\xa0ü.\xa0M.', 'Lage': '[[Kanton Wallis]], [[Schweiz]]', 'Gebirge': '[[Monte Rosa]], [[Walliser Alpen]]', 'Dominanz': '78,2\xa0km →\xa0[[Mont Blanc de Courmayeur]]', 'Schartenhöhe': '2165\xa0m ↓\xa0[[Grosser St. Bernhard]]', 'Erstbesteigung': '1855 durch [[Charles Hudson (Bergsteiger)]], J. Smyth, C. Smyth, u.\xa0a.', 'Normalweg': 'anspruchsvolle Hochtour (vergletschert); Gesamtschwierigkeit AD- (AD = assez difficile, ziemlich schwierig)'}], [{'name': 'Mont Blanc de Courmayeur', 'height': '4748\xa0m\xa0s.l.m.', 'coords': [45.828695, 6.86843], 'isolation': '0,6\xa0km →\xa0[[Mont Blanc]]', 'next_high': 'Mont Blanc'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Mbcourmayeur0001.jpg/300px-Mbcourmayeur0001.jpg', 'Höhe': '4748\xa0m\xa0s.l.m.', 'Lage': '[[Italien]], [[Frankreich]]', 'Gebirge': '[[Savoyer Alpen]]', 'Dominanz': '0,6\xa0km →\xa0[[Mont Blanc]]', 'Schartenhöhe': '18\xa0m ↓\xa0[[Col Major (Seite nicht vorhanden)]]'}], [{'name': 'Mont Blanc', 'height': '4805,59\xa0m', 'coords': [45.832544, 6.864325], 'isolation': '2812\xa0km →\xa0[[Kjukjurtlju]]', 'next_high': 'Kjukjurtlju'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/MontBlancFromENE.jpg/300px-MontBlancFromENE.jpg', 'Höhe': '4805,59\xa0m', 'Lage': '[[Frankreich]] und [[Italien]]', 'Gebirge': '[[Mont-Blanc-Gruppe]]', 'Dominanz': '2812\xa0km →\xa0[[Kjukjurtlju]]', 'Schartenhöhe': '4692\xa0m ↓\xa0Beim [[Kubenasee]]', 'Gestein': '[[Granit]]', 'Erstbesteigung': '[[8. August]] [[1786]], [[Jacques Balmat]] und [[Michel-Gabriel Paccard]]', 'Normalweg': 'Hochtour von [[Refuge du Goûter]]', 'Besonderheiten': 'Höchster Berg der [[Alpen]]'}], [{'name': 'Kjukjurtlju', 'height': '4978\xa0m', 'coords': [43.34138889, 42.40611111], 'isolation': '2,7\xa0km →\xa0[[Elbrus]]-Südwestgipfel', 'next_high': 'Elbrus'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Kukurtlu.jpg/300px-Kukurtlu.jpg', 'Höhe': '4978\xa0m', 'Lage': '[[Karatschai-Tscherkessien]], [[Russland]]', 'Gebirge': '[[Kaukasus]]', 'Dominanz': '2,7\xa0km →\xa0[[Elbrus]]-Südwestgipfel', 'Erstbesteigung': 'Popow und Kameraden, 1932'}], [{'name': 'Elbrus', 'height': '5642\xa0m', 'coords': [43.35254, 42.437875], 'isolation': '2.472,7\xa0km →\xa0[[Pik Agasis]]', 'next_high': 'Pik Agasis'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/%D0%AD%D0%BB%D1%8C%D0%B1%D1%80%D1%83%D1%81_%D1%81_%D1%81%D0%B5%D0%B2%D0%B5%D1%80%D0%B0.jpg/300px-%D0%AD%D0%BB%D1%8C%D0%B1%D1%80%D1%83%D1%81_%D1%81_%D1%81%D0%B5%D0%B2%D0%B5%D1%80%D0%B0.jpg', 'Höhe': '5642\xa0m', 'Lage': '[[Kabardino-Balkarien]], [[Karatschai-Tscherkessien]] ([[Russland]])', 'Gebirge': '[[Großer Kaukasus]]', 'Dominanz': '2.472,7\xa0km →\xa0[[Pik Agasis]]', 'Schartenhöhe': '4741\xa0m ↓\xa0bei 26,56°\xa0N, 63,654°\xa0O in [[Pakistan]] (901\xa0m)', 'Typ': '[[Schichtvulkan]]', 'Letzte Eruption': '50 n. Chr. ± 50 Jahre', 'Erstbesteigung': '22. Juli 1829 Kilar Chatschirow (Ostgipfel), 26. Juli 1874 [[Frederick Gardiner (Bergsteiger) (Seite nicht vorhanden)]], [[Florence Crauford Grove]], [[Horace Walker]], [[Peter Knubel]] (Westgipfel)', 'Normalweg': 'Hochtour von [[Prijut 11 (Seite nicht vorhanden)]]', 'Besonderheiten': 'Höchster Berg Russlands und des Kaukasus, einer der [[Seven Summits]]'}], [{'name': 'Pik Agasis', 'height': '5877\xa0m', 'coords': [39.014128, 71.504167], 'isolation': '29,45\xa0km →\xa0[[Pik Moskau]]', 'next_high': 'Pik Moskau'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Photo-request.svg/40px-Photo-request.svg.png', 'Höhe': '5877\xa0m', 'Lage': '[[Tadschikistan]]', 'Gebirge': '[[Peter-I.-Kette]] ([[Pamir (Gebirge)]])', 'Dominanz': '29,45\xa0km →\xa0[[Pik Moskau]]', 'Schartenhöhe': '1597\xa0m ↓\xa0(4280\xa0m)'}], [{'name': 'Pik Moskau', 'height': '6785\xa0m', 'coords': [38.948517, 71.834732], 'isolation': '15,7\xa0km →\xa0[[Pik Ismoil Somoni]]', 'next_high': 'Pik Ismoil Somoni'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Pik_Moskva.jpg/300px-Pik_Moskva.jpg', 'Höhe': '6785\xa0m', 'Lage': '[[Nohija Tawildara (Seite nicht vorhanden)]] in [[Nohijahoi tobei dschumhurij]] ([[Tadschikistan]])', 'Gebirge': '[[Peter-I.-Kette]] ([[Pamir (Gebirge)]])', 'Dominanz': '15,7\xa0km →\xa0[[Pik Ismoil Somoni]]', 'Schartenhöhe': '1155\xa0m ↓\xa0(5630\xa0m)', 'Erstbesteigung': '1959 durch I. Bogatschow'}], [{'name': 'Pik Ismoil Somoni', 'height': '7495\xa0m', 'coords': [38.9426, 72.0151], 'isolation': '278\xa0km →\xa0[[Kongur Jiubie]] (Nebengipfel des [[Kongur]])', 'next_high': 'Kongur Jiubie'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Kommunismi_m%C3%A4etipp_85.jpg/300px-Kommunismi_m%C3%A4etipp_85.jpg', 'Höhe': '7495\xa0m', 'Lage': '[[Berg-Badachschan]], [[Tadschikistan]]', 'Gebirge': '[[Kette der Akademie der Wissenschaften]] ([[Pamir (Gebirge)]])', 'Dominanz': '278\xa0km →\xa0[[Kongur Jiubie]] (Nebengipfel des [[Kongur]])', 'Schartenhöhe': '3402\xa0m ↓\xa0(4093\xa0m)', 'Erstbesteigung': '3. September 1933 durch [[Jewgeni Michailowitsch Abalakow]]', 'Normalweg': 'Hochtour vergletschert'}], [{'name': 'Kongur Jiubie', 'height': '7530\xa0m', 'coords': [38.615796, 75.195643], 'isolation': '10,52\xa0km →\xa0[[Kongur]]', 'next_high': 'Kongur'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Karakul-kongur-d11.jpg/300px-Karakul-kongur-d11.jpg', 'Höhe': '7530\xa0m', 'Lage': '[[Xinjiang]] ([[Volksrepublik China]])', 'Gebirge': '[[Pamir (Gebirge)]]', 'Dominanz': '10,52\xa0km →\xa0[[Kongur]]', 'Schartenhöhe': '810\xa0m ↓\xa0Kongur-Sattel (6720\xa0m)', 'Erstbesteigung': '16. August 1956 durch eine sowjet.-chines. Expedition'}], [{'name': 'Kongur', 'height': '7649\xa0m', 'coords': [38.5933, 75.31269], 'isolation': '240\xa0km →\xa0[[Batura Sar]]', 'next_high': 'Batura Sar'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Kongur_south.jpg/300px-Kongur_south.jpg', 'Höhe': '7649\xa0m', 'Lage': '[[Xinjiang]], [[Volksrepublik China]]', 'Gebirge': '[[Pamir (Gebirge)]]', 'Dominanz': '240\xa0km →\xa0[[Batura Sar]]', 'Schartenhöhe': '3585\xa0m ↓\xa0(4064 m)', 'Erstbesteigung': '12. Juli 1981 durch [[Chris Bonington]], [[Al Rouse (Seite nicht vorhanden)]], [[Peter Boardman]], [[Joe Tasker]]'}], [{'name': 'Batura Sar', 'height': '7795\xa0m', 'coords': [36.510329, 74.522602], 'isolation': '62,98\xa0km →\xa0[[Distaghil Sar]]', 'next_high': 'Distaghil Sar'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Batura_valley_Passu.jpg/300px-Batura_valley_Passu.jpg', 'Höhe': '7795\xa0m', 'Lage': '[[Gilgit-Baltistan]], [[Pakistan]]', 'Gebirge': '[[Batura Muztagh]] ([[Karakorum (Gebirge)]])', 'Dominanz': '62,98\xa0km →\xa0[[Distaghil Sar]]', 'Schartenhöhe': '3118\xa0m ↓\xa0[[Mingteke-Pass]] (4677\xa0m)', 'Erstbesteigung': '30. Juni 1976 durch [[Hubert Bleicher]] und [[Herbert Oberhofer (Bergsteiger)]]', 'Normalweg': 'vergletscherte Hochtour'}], [{'name': 'Distaghil Sar', 'height': '7885\xa0m', 'coords': [36.325702, 75.188224], 'isolation': '129,27\xa0km →\xa0[[K2]]', 'next_high': 'K2'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Summit_view_from_Spantik_%287027m%29_to_north-east.png/300px-Summit_view_from_Spantik_%287027m%29_to_north-east.png', 'Höhe': '7885\xa0m', 'Lage': '[[Gilgit (Distrikt)]] in [[Gilgit-Baltistan]] ([[Pakistan]])', 'Gebirge': '[[Hispar Muztagh]] ([[Karakorum (Gebirge)]])', 'Dominanz': '129,27\xa0km →\xa0[[K2]]', 'Schartenhöhe': '2509\xa0m ↓\xa0[[Muztagh-Pass]] (5376\xa0m)', 'Erstbesteigung': '9. Juni 1960 durch Diether Marchart und Günther Stärker', 'Normalweg': 'vergletscherte Hochtour', 'Besonderheiten': 'Höchster Berg des [[Hispar Muztagh]]'}], [{'name': 'K2', 'height': '8611\xa0m', 'coords': [35.88333333, 76.51666667], 'isolation': '1.315,77\xa0km →\xa0[[Mount Everest]]', 'next_high': 'Mount Everest'}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/K2-big_b.jpg/300px-K2-big_b.jpg', 'Höhe': '8611\xa0m', 'Lage': '[[Gilgit-Baltistan]], [[Pakistan]], und [[Xinjiang]], [[Volksrepublik China]]', 'Gebirge': '[[Baltoro Muztagh]] ([[Karakorum (Gebirge)]])', 'Dominanz': '1.315,77\xa0km →\xa0[[Mount Everest]]', 'Schartenhöhe': '4020\xa0m ↓\xa0Lo Mustang', 'Erstbesteigung': '[[31. Juli]] [[1954]] durch [[Achille Compagnoni]], [[Lino Lacedelli]]', 'Normalweg': 'Abruzzi-Route', 'Besonderheiten': 'Zweithöchster Berg der Welt und höchster Berg [[Pakistan]]'}], [{'name': 'Mount Everest', 'height': '8848\xa0m', 'coords': [27.98823, 86.92501]}, {'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Everest_North_Face_toward_Base_Camp_Tibet_Luca_Galuzzi_2006.jpg/300px-Everest_North_Face_toward_Base_Camp_Tibet_Luca_Galuzzi_2006.jpg', 'Höhe': '8848\xa0m', 'Lage': '[[Solukhumbu]], [[Nepal]], und [[Autonomes Gebiet Tibet]], [[Volksrepublik China]]', 'Gebirge': '[[Mahalangur Himal]] ([[Himalaya]])', 'Gestein': '[[Kristallingestein]], [[Kalkstein]]', 'Alter des Gesteins': '[[Neoproterozoikum]]–[[Ordovizium]], [[Tertiär]]', 'Erstbesteigung': '29. Mai 1953 durch [[Edmund Hillary]] und [[Tenzing Norgay]]', 'Normalweg': 'Südroute'}]]
    # iso_list = wiki2.loop(input_mountain)

file_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(file_dir)
with open(os.path.join(parent_dir, 'static.html'), 'r') as f:
    static_html = f.read()
formatted_html = static_html.format(iso_list=iso_list)

print(formatted_html)

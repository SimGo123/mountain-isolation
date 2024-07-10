let prevPoint = null;
var osm = null;
var markerList = [];
var lineList = [];

function setupMap() {
    osm = L.map('osm').setView([47.8, 11.2], 3);
    // Für OSM: Erstelle Karte mit Urheberrecht und Tiles (Kacheln), aus denen die Karte zusammengesetzt ist
    const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contribiutors';
    const tileUrl = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
    const tiles = L.tileLayer(tileUrl, { attribution });
    tiles.addTo(osm);
}

function drawIsoList(iso_list) {
    let start = true;
    for (let i = 0; i < iso_list.length; i++) {
        let fixedParams = iso_list[i][0];
        let name = fixedParams['name'];
        let height = fixedParams['height'];
        let coords = fixedParams['coords'];
        // console.log(iso_list[i]);

        var marker = L.marker([coords[0], coords[1]]).addTo(osm);
        markerList.push(marker);
        // Popup-Text für den Marker
        infoboxComplete = iso_list[i][1];
        infoboxComplete['Koordinaten'] = `${coords[0].toFixed(5)},${coords[1].toFixed(5)}`;
        let markerTxt = `<h3>${name}</h3>`;
        for (const key in infoboxComplete) {
            if (infoboxComplete.hasOwnProperty(key)) {
                if (key == 'image') {
                    markerTxt += `<img src='${infoboxComplete[key]}' width='200px'><br />`
                } else {
                    markerTxt += `<b>${key}:</b> ${infoboxComplete[key]}<br />`;
                }
            }
        }
        // const txt = `
        // <h3>${name}</h3>
        // ${height} m<br />
        // <a href="https://de.wikipedia.org/wiki/${name}">Wiki</a><br />
        // Koordinaten: ${coords[0].toFixed(4)},${coords[1].toFixed(4)}`;
        marker.bindPopup(markerTxt);

        L.circle([coords[0], coords[1]], 1600).addTo(osm);

        let currPoint = new L.LatLng(coords[0], coords[1]);
        // Für eine Linie brauchen wir 2 Punkte - am Anfang darf also noch keine Linie gezeichnet werden
        if (start) {
            start = false;
        }
        else {
            var line = new L.Polyline([prevPoint, currPoint], {
                color: 'black',
                weight: 3,
                opacity: 0.5,
                smoothFactor: 1
            });
            line.arrowheads({
                size: '10px',
                fill: true,
                fillOpacity: 0.8
            });
            lineList.push(line);
            line.addTo(osm);
        }
        // Setze jetzigen Punkt als nachher vorheriger ;)
        prevPoint = currPoint;
    }
}

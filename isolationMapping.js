// Projekt am 09.07.2024 - 
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
        let name = iso_list[i]['name'];
        let height = iso_list[i]['height'];
        let coords = iso_list[i]['coords'];
        // console.log(iso_list[i]);

        var marker = L.marker([coords[0], coords[1]]).addTo(osm);
        markerList.push(marker);
        // Popup-Text für den Marker
        const txt = `
        <h3>${name}</h3>
        ${height} m<br />
        <a href="https://de.wikipedia.org/wiki/${name}">Wiki</a><br />
        Koordinaten: ${coords[0].toFixed(4)},${coords[1].toFixed(4)}`;
        marker.bindPopup(txt);

        let currPoint = new L.LatLng(coords[0], coords[1]);
        // Für eine Linie brauchen wir 2 Punkte - am Anfang darf also noch keine Linie gezeichnet werden
        if (start) {
            start = false;
        }
        else {
            // Zeichne Linie vom letzten zum jetzigen Punkt
            var line = new L.Polyline([prevPoint, currPoint], {
                color: 'black',
                weight: 3,
                opacity: 0.5,
                smoothFactor: 1
            });
            line.arrowheads({
                size: '10px',  // Arrowhead size
                fill: true,  // Fill arrowhead
                fillOpacity: 0.8  // Arrowhead opacity
            });
            lineList.push(line);
            line.addTo(osm);
        }
        // Setze jetzigen Punkt als nachher vorheriger ;)
        prevPoint = currPoint;
    }
}

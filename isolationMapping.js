let prevPoint = null;
var osm = null;
var markerList = [];
var lineList = [];
var circleList = [];

function setupMap() {
    osm = L.map('osm').setView([47.8, 11.2], 3);
    // Für OSM: Erstelle Karte mit Urheberrecht und Tiles (Kacheln), aus denen die Karte zusammengesetzt ist
    const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contribiutors';
    const tileUrl = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
    const tiles = L.tileLayer(tileUrl, { attribution });
    tiles.addTo(osm);
}

function cleanup() {
    markerList.forEach(function (marker) {
        osm.removeLayer(marker);
    });
    lineList.forEach(function (line) {
        osm.removeLayer(line);
    });
    circleList.forEach(function (circle) {
        osm.removeLayer(circle);
    });
    markerList = [];
    lineList = [];
    circleList = [];
}

function drawIsoList(iso_list) {
    cleanup();

    let start = true;
    const colors = ['red','blue','green','orange','violet', 'yellow']
    for (let i = 0; i < iso_list.length; i++) {
        let fixedParams = iso_list[i][0];
        let name = fixedParams['name'];
        let height = fixedParams['height'];
        let isolation_dist = 0;
        if (fixedParams.hasOwnProperty('isolation_dist')) {
            isolation_dist = fixedParams['isolation_dist'];
        }
        let coords = fixedParams['coords'];
        // console.log(iso_list[i]);

        let color_to_use = colors[i % colors.length];
        var showMarker = document.getElementById("cbShowMarker").checked;
        var showCircle = document.getElementById("cbShowCircle").checked;
        if (showMarker) {
            var colorIcon = new L.Icon({
                iconUrl: `https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-${color_to_use}.png`,
                shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
                iconSize: [25, 41],
                iconAnchor: [12, 41],
                popupAnchor: [1, -34],
                shadowSize: [41, 41]
            });
            var marker = L.marker([coords[0], coords[1]], {icon: colorIcon}).addTo(osm);
            markerList.push(marker);
            // Popup-Text für den Marker
            infoboxComplete = iso_list[i][1];
            infoboxComplete['Koordinaten'] = `${coords[0].toFixed(5)},${coords[1].toFixed(5)}`;
            let markerTxt = `<h3>${name} (<a href="https://de.wikipedia.org/wiki/${name}">Wiki</a>)</h3>`;
            for (const key in infoboxComplete) {
                if (infoboxComplete.hasOwnProperty(key)) {
                    if (key == 'image') {
                        markerTxt += `<img src='${infoboxComplete[key]}' width='200px'><br />`
                    } else {
                        markerTxt += `<b>${key}:</b> ${infoboxComplete[key]}<br />`;
                    }
                }
            }
            marker.bindPopup(markerTxt);
        }

        if (showCircle) {
            var circle = L.circle([coords[0], coords[1]], {
                radius: isolation_dist,
                color: color_to_use
            }).addTo(osm);
            circleList.push(circle);
        }

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

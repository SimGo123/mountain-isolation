var currPoint = null;
var prevPoint = null;
var markerList = [];
var lineList = [];
var circleList = [];

var osm = null;
var iso_list = [];
var heightGraph = null;
var demo = false;

document.addEventListener('DOMContentLoaded', function() {
    if (!demo) {
        setupMap();

        const mountainParam = 'mountain';
        const urlParams = new URLSearchParams(window.location.search);
        if (urlParams.has(mountainParam)) {
            let mountain = urlParams.get(mountainParam);
            startIsolationLoop(mountain);
        }
    }
});

// Starts the isolation loop
// Uses Server-Sent Events (SSE) protocol to get updates during loop execution
function startIsolationLoop(mountain) {
    document.getElementById('mountainLoader').style = 'visibility: visible;';

    const eventSource = new EventSource(`../cgi-bin/select-mountain-scripts/wiki_isolation_looper.py?mountain=${mountain}`);
    let isStart = true;

    eventSource.addEventListener('step', function(event) {
        iso_list = JSON.parse(event.data);
        if (isStart) {
            drawIsoList(true);
            isStart = false;
        } else {
            drawIsoList();
        }
    });

    eventSource.addEventListener('errorx', function(event) {
        document.getElementById('errorBox').style = 'visibility: visible;';
        document.getElementById('errorBox').innerHTML += `<strong>Error:</strong> ${event.data}<br />`
        console.log('errorx '+event.data);
    });

    eventSource.addEventListener('return', function(event) {
        iso_list = JSON.parse(event.data);
        drawIsoList();
        document.getElementById('mountainLoader').style = 'visibility: hidden;';
    });

    eventSource.onerror = function() {{
        eventSource.close();
    }};
}

function setupMap() {
    osm = L.map('osm',{noWrap:true}).setView([47.8, 11.2], 3);
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
    crossingDateline = false;
}

function drawIsoList(changeMapPos=false) {
    cleanup();
    let mountainListDiv = document.getElementById('mountainList');
    mountainListDiv.innerHTML = '';

    const colors = ['red','blue','green','orange','violet', 'yellow'];
    for (let i = 0; i < iso_list.length; i++) {
        let isStart = i==0;
        let fixedParams = iso_list[i][0];
        let name = fixedParams['name'];
        mountainListDiv.innerHTML += name + ' - ';
        let height = fixedParams['height'];
        let isolation_dist = 0;
        if (fixedParams.hasOwnProperty('isolation_dist')) {
            isolation_dist = fixedParams['isolation_dist'];
        }

        let coords = new L.LatLng(fixedParams['coords'][0], fixedParams['coords'][1]);
        currPoint = new L.LatLng(coords.lat, coords.lng);
        if (!isStart) {
            // If line between prevPoint and currrPoint crosses date line,
            // go across the [-180,180] longitude boundaries
            // This means drawing on a 'world' adjacent to the current one
            // All points after the dateline are drawn on the adjacent world,
            // as the condition below will be fulfilled
            // Warning: This only works when crossing the line just once
            if (Math.abs(prevPoint.lng - currPoint.lng) >= 180) {
                if (prevPoint.lng < 0) { // America -> Asia
                    currPoint.lng = -180 - (180 - currPoint.lng);
                } else { // Asia -> America
                    currPoint.lng = 180 + (180 + currPoint.lng);
                }
            }
        }

        if (changeMapPos) {
            osm.setView(coords, 7);
        }

        let colorToUse = colors[i % colors.length];
        var showMarker = document.getElementById("cbShowMarker").checked;
        var showCircle = document.getElementById("cbShowCircle").checked;
        if (showMarker) {
            drawMarker(iso_list[i], name, colorToUse, coords);
        }

        if (showCircle) {
            drawCircle(isolation_dist, colorToUse);
        }

        drawLine(isStart);
        // Set the current point to become the later previous one ;)
        prevPoint = currPoint;
    }
    drawHeightGraph(false);

    if (mountainListDiv.innerHTML.length >= 2) {
        mountainListDiv.innerHTML = mountainListDiv.innerHTML.substring(0, mountainListDiv.innerHTML.length-2);
    }
}

function drawMarker(curr_iso, name, colorToUse, coords) {
    var colorIcon = new L.Icon({
        iconUrl: `https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-${colorToUse}.png`,
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    });
    var marker = L.marker(currPoint, {icon: colorIcon}).addTo(osm);
    markerList.push(marker);
    // Popup text for the marker
    infoboxComplete = curr_iso[1];
    infoboxComplete['Koordinaten'] = `${coords.lat.toFixed(5)},${coords.lng.toFixed(5)}`;
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

function drawCircle(isolation_dist, colorToUse) {
    var circle = L.circle(currPoint, {
        radius: isolation_dist,
        color: colorToUse
    }).addTo(osm);
    circleList.push(circle);
}

function drawLine(isStart) {
    // For a line, >= 2 points are needed -> don't draw on start
    if (isStart) {
        isStart = false;
    }
    else {
        var line = new L.Polyline([prevPoint, currPoint], {
            color: 'black',
            weight: 3,
            opacity: 0.5,
            smoothFactor: 1
        });
        // line.arrowheads({
        //     size: '10px',
        //     fill: true,
        //     fillOpacity: 0.8
        // });
        lineList.push(line);
        line.addTo(osm);
    }
}

function drawHeightGraph(redraw) {
    let names = [];
    let heights = [];
    for (let i = 0; i < iso_list.length; i++) {
        let fixedParams = iso_list[i][0];
        let name = fixedParams['name'];
        let height = fixedParams['height'];
        names.push(name);
        heights.push(height);
    }
    if (!heightGraph || redraw) {
        heightGraph = new Highcharts.Chart({
            chart: {renderTo: 'heightGraph'},
            title: {text: 'Height Graph of Visited Mountains'},
            xAxis: {title: {text: 'Visited Mountains'}, /*categories:,*/ crosshair: true},
            yAxis: [
                {
                    title: {
                        text: 'Height (m)',
                        style: {
                            color: 'black'
                        }
                    },
                    labels: {
                        format: '{value}m',
                        style: {
                            color: 'black'
                        }
                    }
                }
            ],
            series: [
                {
                    name: 'Height', 
                    data: heights.map((height, index) => ({
                        y: height,
                        name: names[index]
                    })), 
                    type: 'spline',
                    tooltip: {
                        valueSuffix: ' m'
                    },
                    color: 'red'
                }
            ]
        });
    } else {
        heightGraph.series[0].setData(
            heights.map((height, index) => ({
                y: height,
                name: names[index]
            }))
        );
    }
}

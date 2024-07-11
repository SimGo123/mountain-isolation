function wikiSearchUpdate() {
    var searchTerm = document.getElementById('wikiInput').value.trim();
    if (!searchTerm) {
        clearResults();
        return;
    }
    
    fetch(`/cgi-bin/wiki_opensearch_client.py?query=${encodeURIComponent(searchTerm)}`)
        .then(response => response.json())
        .then(data => {
            if (searchTerm == document.getElementById('wikiInput').value.trim()) { // Check if still up to date
                displayResults(data, searchTerm);
            }
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            displayError('Error fetching data. Please try again later.');
        }
    );
}

function displayResults(data, searchTerm) {
    var searchResults = data[1]; // Array of search results
    var resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = ''; // Clear previous results
    
    if (searchResults.length === 0) {
        resultsContainer.innerHTML = '<p>No results found.</p>';
        return;
    }

    searchResults.forEach(result => {
        var resultItem = document.createElement('a');
        resultItem.classList.add('result-item');
        resultItem.innerHTML = result.replace(searchTerm, `<b>${searchTerm}</b>`);
        resultItem.addEventListener('click', function() {
            clearResults();
            document.getElementById('wikiInput').value = result;
            document.getElementById('wikiSearchForm').submit();
        });
        resultsContainer.appendChild(resultItem);
    });
}

function clearResults() {
    document.getElementById('results').innerHTML = '';
}

function displayError(message) {
    document.getElementById('results').innerHTML = `<p>${message}</p>`;
}

document.getElementById('plotForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const plotSummary = document.getElementById('plotSummary').value;

    // Update the URL if necessary
    fetch('http://127.0.0.1:5000/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ plot: plotSummary })
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';

        data.similarMovies.forEach(movie => {
            const movieDiv = document.createElement('div');
            movieDiv.classList.add('movie');
            movieDiv.innerHTML = `
                <h3>${movie}</h3>
            `;
            resultsDiv.appendChild(movieDiv);
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

import React, { useState } from 'react';
import './App.css';

function App() {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [error, setError] = useState('');

    const handleSearch = async () => {
        setError('');
        setResults([]);
        try {
            const response = await fetch(`/search?query=${encodeURIComponent(query)}`);
            if (!response.ok) throw new Error('Search failed');
            const data = await response.json();
            setResults(data.results || []);
        } catch (error) {
            setError('An error occurred while fetching the results.');
        }
    };

    const handleExport = async () => {
        setError('');
        try {
            const response = await fetch(`/search?query=${encodeURIComponent(query)}&export_csv=true`);
            if (!response.ok) throw new Error('Export failed');
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'results.csv';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        } catch (error) {
            setError('An error occurred while exporting the results.');
        }
    };

    return (
        <div className="search-container">
            <div className="search-box">
                <img src="/logo.png" alt="Springer Link Search" className="logo" />
                <h1 className="title">Springer Link Search</h1>
                <input
                    type="text"
                    className="search-input"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Search for scientific articles..."
                />
                <button className="search-button" onClick={handleSearch}>Search</button>
                {/*<button className="search-button" onClick={handleExport}>Export CSV</button>*/}
                {error && <div className="error">{error}</div>}
                <div className="results-container">
                    <ul className="results-list">
                        {results.map((result, index) => (
                            <li key={index} className="result-item">
                                <a href={result.url} target="_blank" rel="noopener noreferrer">
                                    <h2>{result.title}</h2>
                                </a>
                                <p>{result.abstract}</p>
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
        </div>
    );
}

export default App;

import React, { useState } from 'react';
import axios from 'axios';
import './SearchComponent.css';

function SearchComponent() {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSearch = async () => {
        setLoading(true);
        setError('');
        try {
            const response = await axios.get('http://127.0.0.1:5000/search', {
                params: {
                    query: query,
                    export_csv: false,
                },
            });
            setResults(response.data);
        } catch (error) {
            setError('Error fetching data');
            console.error('Error fetching data', error);
        }
        setLoading(false);
    };

    return (
        <div className="search-container">
            <div className="search-box">
                <img
                    src="https://th.bing.com/th/id/R.a50caa74723631eb6643d39000c4cc58?rik=5me383%2bP4Jszng&riu=http%3a%2f%2flibrary.karu.ac.ke%2fwp-content%2fuploads%2f2021%2f09%2fspringer_link.jpg&ehk=Ain81MNofPuNTuGEQbDwBov8F2B0ZC83As%2bwfv2M6mk%3d&risl=&pid=ImgRaw&r=0"
                    alt="Springer Link Logo"
                    className="logo"
                />
                <h1 className="title">Springer Link Search</h1>
                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Search for scientific articles..."
                    className="search-input"
                />
                <button onClick={handleSearch} disabled={loading} className="search-button">
                    {loading ? 'Searching...' : 'Search'}
                </button>
            </div>
            {error && <div className="error">{error}</div>}
            {results.length > 0 && (
                <div className="results-container">
                    <ul className="results-list">
                        {results.map((item, index) => (
                            <li key={index} className="result-item">
                                <strong>{item.title}</strong>
                                <p>{item.abstract}</p>
                            </li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}

export default SearchComponent;

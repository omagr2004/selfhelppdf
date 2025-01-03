import React, { useState } from 'react';
import axios from 'axios';

const WebScrape = () => {
    const [url, setUrl] = useState('');
    const [data, setData] = useState(null);
    const [error, setError] = useState('');

    const handleScrape = async () => {
        try {
            const response = await axios.post('/api/scrape', { url });
            setData(response.data);
            setError('');
        } catch (err) {
            setError('Error fetching data. Please check the URL and try again.');
            setData(null);
        }
    };

    return (
        <div>
            <h2>Web Scraping Tool</h2>
            <input
                type="text"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="Enter URL to scrape"
            />
            <button onClick={handleScrape}>Scrape</button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {data && (
                <div>
                    <h3>Fetched Data:</h3>
                    <pre>{JSON.stringify(data, null, 2)}</pre>
                </div>
            )}
        </div>
    );
};

export default WebScrape;
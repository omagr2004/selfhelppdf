import React from 'react';

const NlpResults = ({ results }) => {
    return (
        <div className="nlp-results">
            <h2>NLP Results</h2>
            {results && results.length > 0 ? (
                <ul>
                    {results.map((result, index) => (
                        <li key={index}>
                            <strong>Sentiment:</strong> {result.sentiment} <br />
                            <strong>Answer:</strong> {result.answer}
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No results available.</p>
            )}
        </div>
    );
};

export default NlpResults;
// src/components/Journal.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Journal() {
    const [entries, setEntries] = useState([]);
    const [newEntry, setNewEntry] = useState('');

    useEffect(() => {
        const fetchEntries = async () => {
            const response = await axios.get('/api/journal-entries/');
            setEntries(response.data);
        };
        fetchEntries();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/journal-entries/', { content: newEntry });
            setEntries([...entries, response.data]);
            setNewEntry('');
        } catch (error) {
            console.error('Failed to add journal entry', error);
        }
    };

    return (
        <div>
            <h2>Journal</h2>
            <ul>
                {entries.map((entry) => (
                    <li key={entry.id}>{entry.content}</li>
                ))}
            </ul>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={newEntry}
                    onChange={(e) => setNewEntry(e.target.value)}
                    placeholder="New journal entry"
                    required
                ></textarea>
                <button type="submit">Add Entry</button>
            </form>
        </div>
    );
}

export default Journal;

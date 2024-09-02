import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Journal() {
    const [journalEntries, setJournalEntries] = useState([]);

    useEffect(() => {
        const fetchJournalEntries = async () => {
            try {
                const response = await axios.get('/api/journal-entries/');
                setJournalEntries(response.data);
            } catch (error) {
                console.error('Error fetching journal entries:', error);
            }
        };

        fetchJournalEntries();
    }, []);

    return (
        <div>
            <h2>Journal Entries</h2>
            <ul>
                {journalEntries.map(entry => (
                    <li key={entry.id}>
                        <strong>{entry.student.username}</strong> - {entry.date}: {entry.content}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Journal;

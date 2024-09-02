// Dashboard.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '/workspaces/W.A.I.D.S/internship-journal/frontend/src/styles/Dashboard.css';

function Dashboard() {
    const [journalEntries, setJournalEntries] = useState([]);

    useEffect(() => {
        axios.get('/api/journal-entries/')
            .then(response => {
                setJournalEntries(response.data);
            })
            .catch(error => {
                console.error('Error fetching journal entries:', error);
            });
    }, []);

    return (
        <div className="dashboard">
            <h2>Journal Entries</h2>
            <table>
                <thead>
                    <tr>
                        <th>Student</th>
                        <th>Date</th>
                        <th>Content</th>
                        <th>Mentor Feedback</th>
                        <th>Supervisor Feedback</th>
                    </tr>
                </thead>
                <tbody>
                    {journalEntries.map(entry => (
                        <tr key={entry.id}>
                            <td>{entry.student}</td>
                            <td>{entry.date}</td>
                            <td>{entry.content}</td>
                            <td>{entry.mentor_feedback}</td>
                            <td>{entry.supervisor_feedback}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Dashboard;

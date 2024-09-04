// src/components/MentorList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function MentorList() {
    const [mentors, setMentors] = useState([]);

    useEffect(() => {
        const fetchMentors = async () => {
            const response = await axios.get('/api/mentors/');
            setMentors(response.data);
        };
        fetchMentors();
    }, []);

    return (
        <div>
            <h2>Mentors</h2>
            <ul>
                {mentors.map((mentor) => (
                    <li key={mentor.id}>
                        <Link to={`/mentors/${mentor.id}`}>{mentor.name}</Link>
                    </li>
                ))}
            </ul>
            <Link to="/mentors/create">Add Mentor</Link>
        </div>
    );
}

export default MentorList;

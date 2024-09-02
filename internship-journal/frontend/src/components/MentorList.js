// src/components/MentorList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const MentorList = () => {
    const [mentors, setMentors] = useState([]);

    useEffect(() => {
        axios.get('/api/mentors/')
            .then(response => {
                setMentors(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the mentors!', error);
            });
    }, []);

    return (
        <div>
            <h1>Mentors</h1>
            <ul>
                {mentors.map(mentor => (
                    <li key={mentor.id}>
                        <Link to={`/mentors/${mentor.id}`}>{mentor.name}</Link>
                    </li>
                ))}
            </ul>
            <Link to="/mentors/create">Add Mentor</Link>
        </div>
    );
};

export default MentorList;
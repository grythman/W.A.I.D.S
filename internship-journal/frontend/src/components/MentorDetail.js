// src/components/MentorDetail.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, Link } from 'react-router-dom';

const MentorDetail = () => {
    const { id } = useParams();
    const [mentor, setMentor] = useState(null);

    useEffect(() => {
        axios.get(`/api/mentors/${id}/`)
            .then(response => {
                setMentor(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the mentor!', error);
            });
    }, [id]);

    if (!mentor) return <div>Loading...</div>;

    return (
        <div>
            <h1>{mentor.name}</h1>
            <p>Email: {mentor.email}</p>
            <Link to={`/mentors/${mentor.id}/update`}>Edit</Link>
            <Link to={`/mentors/${mentor.id}/delete`}>Delete</Link>
        </div>
    );
};

export default MentorDetail;
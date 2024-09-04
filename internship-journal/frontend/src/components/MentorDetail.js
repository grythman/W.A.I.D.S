// src/components/MentorDetail.js
import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';

function MentorDetail() {
    const { id } = useParams();
    const [mentor, setMentor] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchMentor = async () => {
            const response = await axios.get(`/api/mentors/${id}/`);
            setMentor(response.data);
        };
        fetchMentor();
    }, [id]);

    const handleDelete = async () => {
        try {
            await axios.delete(`/api/mentors/${id}/`);
            navigate('/mentors');
        } catch (error) {
            console.error('Failed to delete mentor', error);
        }
    };

    if (!mentor) return <div>Loading...</div>;

    return (
        <div>
            <h2>{mentor.name}</h2>
            <p>{mentor.description}</p>
            <button onClick={() => navigate(`/mentors/${id}/update`)}>Edit</button>
            <button onClick={handleDelete}>Delete</button>
        </div>
    );
}

export default MentorDetail;

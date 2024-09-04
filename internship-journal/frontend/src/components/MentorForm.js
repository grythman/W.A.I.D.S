// src/components/MentorForm.js
import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import axios from 'axios';

function MentorForm() {
    const { id } = useParams();
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        if (id) {
            const fetchMentor = async () => {
                const response = await axios.get(`/api/mentors/${id}/`);
                setName(response.data.name);
                setDescription(response.data.description);
            };
            fetchMentor();
        }
    }, [id]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            if (id) {
                await axios.put(`/api/mentors/${id}/`, { name, description });
            } else {
                await axios.post('/api/mentors/create/', { name, description });
            }
            navigate('/mentors');
        } catch (error) {
            console.error('Failed to save mentor', error);
        }
    };

    return (
        <div>
            <h2>{id ? 'Update Mentor' : 'Create Mentor'}</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    placeholder="Name"
                    required
                />
                <textarea
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    placeholder="Description"
                    required
                ></textarea>
                <button type="submit">{id ? 'Update' : 'Create'}</button>
            </form>
        </div>
    );
}

export default MentorForm;

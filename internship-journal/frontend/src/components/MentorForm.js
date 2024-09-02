// src/components/MentorForm.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const MentorForm = () => {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const { id } = useParams();
    const navigate = useNavigate();

    useEffect(() => {
        if (id) {
            axios.get(`/api/mentors/${id}/`)
                .then(response => {
                    setName(response.data.name);
                    setEmail(response.data.email);
                })
                .catch(error => {
                    console.error('There was an error fetching the mentor!', error);
                });
        }
    }, [id]);

    const handleSubmit = (event) => {
        event.preventDefault();
        const mentorData = { name, email };

        if (id) {
            axios.put(`/api/mentors/${id}/`, mentorData)
                .then(() => {
                    navigate('/mentors');
                })
                .catch(error => {
                    console.error('There was an error updating the mentor!', error);
                });
        } else {
            axios.post('/api/mentors/', mentorData)
                .then(() => {
                    navigate('/mentors');
                })
                .catch(error => {
                    console.error('There was an error creating the mentor!', error);
                });
        }
    };

    return (
        <div>
            <h1>{id ? 'Edit Mentor' : 'Add Mentor'}</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Name:</label>
                    <input
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Email:</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">{id ? 'Update' : 'Create'}</button>
            </form>
        </div>
    );
};

export default MentorForm;
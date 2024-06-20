// src/components/PatientForm.js

import React, { useState, useEffect } from 'react';
import { useHistory, useParams } from 'react-router-dom';
import axios from 'axios';

const PatientForm = () => {
    const { id } = useParams();
    const history = useHistory();
    const [formData, setFormData] = useState({
        name: '',
        dob: '',
        gender: '',
        contact: '',
        address: '',
        email: ''
    });

    useEffect(() => {
        if (id) {
            axios.get(`/api/patients/${id}/`)
                .then(response => {
                    setFormData(response.data);
                })
                .catch(error => {
                    console.error('There was an error fetching the patient data!', error);
                });
        }
    }, [id]);

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (id) {
            // Update existing patient
            await axios.put(`/api/patients/${id}/`, formData);
        } else {
            // Create new patient
            await axios.post('/api/patients/', formData);
        }
        history.push('/patients');
    };

    return (
        <div>
            <h2>{id ? 'Edit Patient' : 'Add Patient'}</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Name:</label>
                    <input type="text" name="name" value={formData.name} onChange={handleChange} required />
                </div>
                <div>
                    <label>Date of Birth:</label>
                    <input type="date" name="dob" value={formData.dob} onChange={handleChange} required />
                </div>
                <div>
                    <label>Gender:</label>
                    <input type="text" name="gender" value={formData.gender} onChange={handleChange} required />
                </div>
                <div>
                    <label>Contact:</label>
                    <input type="text" name="contact" value={formData.contact} onChange={handleChange} required />
                </div>
                <div>
                    <label>Address:</label>
                    <input type="text" name="address" value={formData.address} onChange={handleChange} required />
                </div>
                <div>
                    <label>Email:</label>
                    <input type="email" name="email" value={formData.email} onChange={handleChange} required />
                </div>
                <button type="submit">{id ? 'Update Patient' : 'Add Patient'}</button>
            </form>
        </div>
    );
};

export default PatientForm;

import React, { useState } from 'react';
import { registerPatient } from './api';

const RegisterPatient = () => {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
        phone: '',
        address: '',
        medical_history: ''
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await registerPatient(formData);
            alert('Patient registered successfully');
        } catch (error) {
            console.error('Error registering patient', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="username" placeholder="Username" onChange={handleChange} />
            <input type="password" name="password" placeholder="Password" onChange={handleChange} />
            <input type="text" name="phone" placeholder="Phone" onChange={handleChange} />
            <input type="text" name="address" placeholder="Address" onChange={handleChange} />
            <textarea name="medical_history" placeholder="Medical History" onChange={handleChange}></textarea>
            <button type="submit">Register</button>
        </form>
    );
};

export default RegisterPatient;

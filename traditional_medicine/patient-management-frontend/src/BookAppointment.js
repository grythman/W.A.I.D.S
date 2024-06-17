import React, { useState } from 'react';
import { bookAppointment } from './api';

const BookAppointment = () => {
    const [formData, setFormData] = useState({
        patient_id: '',
        doctor_id: '',
        appointment_date: '',
        reason: ''
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
            await bookAppointment(formData);
            alert('Appointment booked successfully');
        } catch (error) {
            console.error('Error booking appointment', error);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="patient_id" placeholder="Patient ID" onChange={handleChange} />
            <input type="text" name="doctor_id" placeholder="Doctor ID" onChange={handleChange} />
            <input type="datetime-local" name="appointment_date" onChange={handleChange} />
            <textarea name="reason" placeholder="Reason" onChange={handleChange}></textarea>
            <button type="submit">Book Appointment</button>
        </form>
    );
};

export default BookAppointment;

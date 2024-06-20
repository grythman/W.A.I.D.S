import React, { useState, useEffect } from 'react';
import { getDoctors } from '../services/api';

const Doctors = () => {
    const [doctors, setDoctors] = useState([]);

    useEffect(() => {
        const fetchDoctors = async () => {
            const response = await getDoctors();
            setDoctors(response.data);
        };
        fetchDoctors();
    }, []);

    return (
        <div>
            <h2>Doctors</h2>
            <ul>
                {doctors.map(doctor => (
                    <li key={doctor.id}>{doctor.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default Doctors;
// src/components/Patients.js

import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

const Patients = () => {
    const [patients, setPatients] = useState([]);

    useEffect(() => {
        const fetchPatients = async () => {
            const response = await axios.get('/api/patients/');
            setPatients(response.data);
        };
        fetchPatients();
    }, []);

    return (
        <div>
            <h2>Patients</h2>
            <Link to="/patients/new">Add Patient</Link>
            <ul>
                {patients.map(patient => (
                    <li key={patient.id}>
                        {patient.name} - <Link to={`/patients/${patient.id}/edit`}>Edit</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Patients;

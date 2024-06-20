import React, { useState, useEffect } from 'react';
import { getPatients } from '../services/api';

const Patients = () => {
    const [patients, setPatients] = useState([]);

    useEffect(() => {
        const fetchPatients = async () => {
            const response = await getPatients();
            setPatients(response.data);
        };
        fetchPatients();
    }, []);

    return (
        <div>
            <h2>Patients</h2>
            <ul>
                {patients.map(patient => (
                    <li key={patient.id}>{patient.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default Patients;
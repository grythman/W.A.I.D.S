import React, { useState, useEffect } from 'react';
import { getMedicalHistories } from '../services/api';

const MedicalHistories = () => {
    const [medicalHistories, setMedicalHistories] = useState([]);

    useEffect(() => {
        const fetchMedicalHistories = async () => {
            const response = await getMedicalHistories();
            setMedicalHistories(response.data);
        };
        fetchMedicalHistories();
    }, []);

    return (
        <div>
            <h2>Medical Histories</h2>
            <ul>
                {medicalHistories.map(history => (
                    <li key={history.id}>{history.details}</li>
                ))}
            </ul>
        </div>
    );
};

export default MedicalHistories;
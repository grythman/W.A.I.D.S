import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TreatmentHistories = () => {
    const [histories, setHistories] = useState([]);

    useEffect(() => {
        axios.get('/api/treatment-histories/')
            .then(response => {
                setHistories(response.data);
            })
            .catch(error => {
                console.error("There was an error fetching the treatment histories!", error);
            });
    }, []);

    return (
        <div>
            <h2>Treatment Histories</h2>
            <ul>
                {histories.map(history => (
                    <li key={history.id}>
                        Treatment for {history.patient.name} by {history.doctor.name} on {history.date}: {history.treatment}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TreatmentHistories;

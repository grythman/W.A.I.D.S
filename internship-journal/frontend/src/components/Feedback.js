import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Feedback() {
    const [adviceList, setAdviceList] = useState([]);

    useEffect(() => {
        const fetchAdvice = async () => {
            try {
                const response = await axios.get('/api/advice/');
                setAdviceList(response.data);
            } catch (error) {
                console.error('Error fetching advice:', error);
            }
        };

        fetchAdvice();
    }, []);

    return (
        <div>
            <h2>Advice and Feedback</h2>
            <ul>
                {adviceList.map(advice => (
                    <li key={advice.id}>
                        <strong>{advice.supervisor.name}</strong> to <strong>{advice.student.username}</strong>: {advice.advice}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Feedback;

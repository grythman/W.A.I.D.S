import React, { useState, useEffect } from 'react';
import { getPayments } from '../services/api';

const Payments = () => {
    const [payments, setPayments] = useState([]);

    useEffect(() => {
        const fetchPayments = async () => {
            const response = await getPayments();
            setPayments(response.data);
        };
        fetchPayments();
    }, []);

    return (
        <div>
            <h2>Payments</h2>
            <ul>
                {payments.map(payment => (
                    <li key={payment.id}>
                        {payment.date} - ${payment.amount} - {payment.status}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Payments;
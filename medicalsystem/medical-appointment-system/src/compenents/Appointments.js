import React, { useState, useEffect } from 'react';
import { getAppointments } from '../services/api';

const Appointments = () => {
    const [appointments, setAppointments] = useState([]);

    useEffect(() => {
        const fetchAppointments = async () => {
            const response = await getAppointments();
            setAppointments(response.data);
        };
        fetchAppointments();
    }, []);

    return (
        <div>
            <h2>Appointments</h2>
            <ul>
                {appointments.map(appointment => (
                    <li key={appointment.id}>{appointment.date} - {appointment.time}</li>
                ))}
            </ul>
        </div>
    );
};

export default Appointments;
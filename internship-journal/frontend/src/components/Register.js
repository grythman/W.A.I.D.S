import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Register() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [internshipCompany, setInternshipCompany] = useState('');
    const [internshipStartDate, setInternshipStartDate] = useState('');
    const [internshipEndDate, setInternshipEndDate] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/register/', { username, password, internship_company: internshipCompany, internship_start_date: internshipStartDate, internship_end_date: internshipEndDate });
            if (response.status === 201) {
                navigate('/login');
            }
        } catch (error) {
            console.error('Error registering:', error);
        }
    };

    return (
        <div>
            <h2>Register</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
                </label>
                <label>
                    Password:
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                </label>
                <label>
                    Internship Company:
                    <input type="text" value={internshipCompany} onChange={(e) => setInternshipCompany(e.target.value)} />
                </label>
                <label>
                    Start Date:
                    <input type="date" value={internshipStartDate} onChange={(e) => setInternshipStartDate(e.target.value)} />
                </label>
                <label>
                    End Date:
                    <input type="date" value={internshipEndDate} onChange={(e) => setInternshipEndDate(e.target.value)} />
                </label>
                <button type="submit">Register</button>
            </form>
        </div>
    );
}

export default Register;

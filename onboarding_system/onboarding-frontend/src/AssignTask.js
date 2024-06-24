import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AssignTask = () => {
    const [description, setDescription] = useState('');
    const [employeeId, setEmployeeId] = useState('');
    const [employees, setEmployees] = useState([]);

    useEffect(() => {
        // Fetch the list of employees from the backend
        axios.get('/onboarding/employees/')
            .then(response => {
                setEmployees(response.data);
            })
            .catch(error => {
                console.error('Error fetching employees:', error);
            });
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('/onboarding/assign_task/', {
                description: description,
                employee_id: employeeId
            }, {
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });
            alert(response.data.message);
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to assign task');
        }
    };

    const getCookie = (name) => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    return (
        <div>
            <h2>Assign Task</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Description:</label>
                    <input
                        type="text"
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Employee:</label>
                    <select
                        value={employeeId}
                        onChange={(e) => setEmployeeId(e.target.value)}
                        required
                    >
                        <option value="">Select an employee</option>
                        {employees.map(employee => (
                            <option key={employee.id} value={employee.id}>
                                {employee.name}
                            </option>
                        ))}
                    </select>
                </div>
                <button type="submit">Assign Task</button>
            </form>
        </div>
    );
};

export default AssignTask;

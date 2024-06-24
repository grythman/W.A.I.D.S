import React, { useState, useEffect } from 'react';
import axios from 'axios';

const SetupITResources = () => {
    const [resourceType, setResourceType] = useState('');
    const [employeeId, setEmployeeId] = useState('');
    const [employees, setEmployees] = useState([]);

    useEffect(() => {
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
            const response = await axios.post('/onboarding/setup_it_resources/', {
                resource_type: resourceType,
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
            alert('Failed to set up IT resources');
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
            <h2>Setup IT Resources</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Resource Type:</label>
                    <input
                        type="text"
                        value={resourceType}
                        onChange={(e) => setResourceType(e.target.value)}
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
                <button type="submit">Setup IT Resources</button>
            </form>
        </div>
    );
};

export default SetupITResources;

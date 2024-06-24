import React, { useState } from 'react';
import axios from 'axios';

const CompleteModule = () => {
    const [moduleId, setModuleId] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post(`/onboarding/complete_module/${moduleId}/`, {}, {
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });
            alert(response.data.message);
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to complete module');
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
            <h2>Complete Module</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Module ID:</label>
                    <input
                        type="text"
                        value={moduleId}
                        onChange={(e) => setModuleId(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Complete Module</button>
            </form>
        </div>
    );
};

export default CompleteModule;

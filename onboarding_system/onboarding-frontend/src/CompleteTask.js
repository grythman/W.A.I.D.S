import React, { useState } from 'react';
import axios from 'axios';

const CompleteTask = () => {
    const [taskId, setTaskId] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post(`/onboarding/complete_task/${taskId}/`, {}, {
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });
            alert(response.data.message);
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to complete task');
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
            <h2>Complete Task</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Task ID:</label>
                    <input
                        type="text"
                        value={taskId}
                        onChange={(e) => setTaskId(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Complete Task</button>
            </form>
        </div>
    );
};

export default CompleteTask;

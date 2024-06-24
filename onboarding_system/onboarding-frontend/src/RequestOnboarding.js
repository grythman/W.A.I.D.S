import React, { useState } from 'react';
import axios from 'axios';

const RequestOnboarding = () => {
    const [position, setPosition] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('/onboarding/request_onboarding/', {
                position: position,
            }, {
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });
            alert(response.data.message);
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to request onboarding');
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
            <h2>Request Onboarding</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Position:</label>
                    <input
                        type="text"
                        value={position}
                        onChange={(e) => setPosition(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Submit</button>
            </form>
        </div>
    );
};

export default RequestOnboarding;

import React, { useState } from 'react';
import axios from 'axios';

const SendNotification = () => {
    const [message, setMessage] = useState('');
    const [recipient, setRecipient] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('/onboarding/send_notification/', {
                message: message,
                recipient: recipient
            }, {
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });
            alert(response.data.message);
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to send notification');
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
            <h2>Send Notification</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Message:</label>
                    <input
                        type="text"
                        value={message}
                        onChange={(e) => setMessage(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Recipient:</label>
                    <input
                        type="text"
                        value={recipient}
                        onChange={(e) => setRecipient(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Send Notification</button>
            </form>
        </div>
    );
};

export default SendNotification;

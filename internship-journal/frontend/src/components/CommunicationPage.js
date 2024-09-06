// CommunicationPage.js
import React, { useState } from 'react';

const CommunicationPage = () => {
    const [message, setMessage] = useState('');
    const [messages, setMessages] = useState([]);

    const handleMessageSend = () => {
        setMessages([...messages, { text: message, sender: 'You' }]);
        setMessage('');
    };

    return (
        <div className="communication-page">
            <h2>Messages</h2>
            <div className="chat-box">
                {messages.map((msg, index) => (
                    <div key={index} className="message">
                        <strong>{msg.sender}: </strong> {msg.text}
                    </div>
                ))}
            </div>

            <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Type your message"
            />
            <button onClick={handleMessageSend}>Send</button>
        </div>
    );
}

export default CommunicationPage;

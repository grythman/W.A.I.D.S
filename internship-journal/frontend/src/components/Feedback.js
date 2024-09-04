// src/components/Feedback.js
import React, { useState } from 'react';
import axios from 'axios';

function Feedback() {
    const [content, setContent] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await axios.post('/api/feedback/', { content });
            setContent('');
        } catch (error) {
            console.error('Failed to submit feedback', error);
        }
    };

    return (
        <div>
            <h2>Feedback</h2>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    placeholder="Your feedback"
                    required
                ></textarea>
                <button type="submit">Submit</button>
            </form>
        </div>
    );
}

export default Feedback;

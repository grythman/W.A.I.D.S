import React, { useState } from 'react';
import axios from 'axios';

const SubmitDocument = () => {
    const [documentId, setDocumentId] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post(`/onboarding/submit_document/${documentId}/`, {}, {
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });
            alert(response.data.message);
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to submit document');
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
            <h2>Submit Document</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Document ID:</label>
                    <input
                        type="text"
                        value={documentId}
                        onChange={(e) => setDocumentId(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Submit Document</button>
            </form>
        </div>
    );
};

export default SubmitDocument;

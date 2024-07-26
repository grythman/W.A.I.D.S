import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Journal() {
  const [entries, setEntries] = useState([]);
  const [content, setContent] = useState('');

  useEffect(() => {
    async function fetchEntries() {
      const response = await axios.get('/api/journal');
      setEntries(response.data.entries);
    }
    fetchEntries();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/api/journal', { content });
      if (response.data.success) {
        setEntries([...entries, response.data.entry]);
        setContent('');
      }
    } catch (error) {
      console.error('Journal entry failed', error);
    }
  };

  return (
    <div className="journal">
      <h2>Journal</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Content:</label>
          <textarea value={content} onChange={(e) => setContent(e.target.value)} required />
        </div>
        <button type="submit">Add Entry</button>
      </form>
      <ul>
        {entries.map((entry) => (
          <li key={entry.id}>
            <p>{entry.date}</p>
            <p>{entry.content}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Journal;

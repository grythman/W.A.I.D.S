import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Journal() {
  const [entries, setEntries] = useState([]);
  const [content, setContent] = useState('');

  useEffect(() => {
    const fetchEntries = async () => {
      const response = await axios.get('/api/journal');
      setEntries(response.data.entries);
    };
    fetchEntries();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post('/api/journal', { content });
    if (response.data.success) {
      setEntries([...entries, response.data.entry]);
      setContent('');
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
      <div>
        {entries.map(entry => (
          <div key={entry.id}>
            <p>{entry.date}: {entry.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Journal;

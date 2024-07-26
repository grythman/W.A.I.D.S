import React, { useState } from 'react';
import axios from 'axios';

function Feedback() {
  const [studentId, setStudentId] = useState('');
  const [evaluation, setEvaluation] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`/api/evaluate/${studentId}`, { evaluation });
      if (response.data.success) {
        setStudentId('');
        setEvaluation('');
      }
    } catch (error) {
      console.error('Evaluation failed', error);
    }
  };

  return (
    <div className="feedback">
      <h2>Evaluate Student</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Student ID:</label>
          <input type="text" value={studentId} onChange={(e) => setStudentId(e.target.value)} required />
        </div>
        <div>
          <label>Evaluation:</label>
          <textarea value={evaluation} onChange={(e) => setEvaluation(e.target.value)} required />
        </div>
        <button type="submit">Submit Evaluation</button>
      </form>
    </div>
  );
}

export default Feedback;

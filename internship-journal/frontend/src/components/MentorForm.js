import React, { useState } from 'react';
import { createMentor } from '../services/api';

const MentorForm = ({ setMentors }) => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newMentor = { name, email };
    const response = await createMentor(newMentor);
    setMentors((prev) => [...prev, response.data]);
    setName('');
    setEmail('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <button type="submit">Add Mentor</button>
    </form>
  );
};

export default MentorForm;

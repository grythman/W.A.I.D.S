import React, { useState, useEffect } from 'react';
import { fetchMentors } from '../services/api';
import MentorForm from './MentorForm';

const MentorList = () => {
  const [mentors, setMentors] = useState([]);

  useEffect(() => {
    const getMentors = async () => {
      const response = await fetchMentors();
      setMentors(response.data);
    };
    getMentors();
  }, []);

  return (
    <div>
      <MentorForm setMentors={setMentors} />
      <ul>
        {mentors.map((mentor) => (
          <li key={mentor.id}>{mentor.name} - {mentor.email}</li>
        ))}
      </ul>
    </div>
  );
};

export default MentorList;

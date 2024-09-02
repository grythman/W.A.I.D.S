import React, { useState, useEffect } from 'react';
import axiosInstance from '../utils/axiosInstance'; // Adjust the import path as necessary

const MentorList = () => {
  const [mentors, setMentors] = useState([]);

  useEffect(() => {
    axiosInstance.get('mentors/')
      .then(response => {``
        setMentors(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the mentors!', error);
      });
  }, []);

  return (
    <div>
      <h1>Mentors</h1>
      <ul>
        {mentors.map(mentor => (
          <li key={mentor.id}>{mentor.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default MentorList;
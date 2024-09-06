import React, { useEffect, useState } from 'react';
import axios from 'axios';

function FacultyList() {
  const [faculties, setFaculties] = useState([]);

  useEffect(() => {
    axios.get('/api/faculty/')
      .then(response => {
        setFaculties(response.data);
      })
      .catch(error => {
        console.error('Error fetching faculty data:', error);
      });
  }, []);

  return (
    <div>
      <h2>Faculty List</h2>
      <ul>
        {faculties.map(faculty => (
          <li key={faculty.id}>{faculty.user.username} - {faculty.department}</li>
        ))}
      </ul>
    </div>
  );
}

export default FacultyList;

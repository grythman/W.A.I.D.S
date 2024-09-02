import React, { useState, useEffect } from 'react';
import axiosInstance from '../utils/axiosInstance'; // Adjust the import path as necessary

const StudentList = () => {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    axiosInstance.get('students/')
      .then(response => {
        setStudents(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the students!', error);
      });
  }, []);

  return (
    <div>
      <h1>Students</h1>
      <ul>
        {students.map(student => (
          <li key={student.id}>{student.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default StudentList;
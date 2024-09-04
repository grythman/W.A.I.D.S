import React, { useState, useEffect } from 'react';
import { fetchStudents } from '../services/api';
import StudentForm from './StudentForm';

const StudentList = () => {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    const getStudents = async () => {
      const response = await fetchStudents();
      setStudents(response.data);
    };
    getStudents();
  }, []);

  return (
    <div>
      <StudentForm setStudents={setStudents} />
      <ul>
        {students.map((student) => (
          <li key={student.id}>{student.username} - {student.internship_company}</li>
        ))}
      </ul>
    </div>
  );
};

export default StudentList;

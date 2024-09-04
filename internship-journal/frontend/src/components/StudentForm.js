import React, { useState } from 'react';
import { createStudent } from '../services/api';

const StudentForm = ({ setStudents }) => {
  const [username, setUsername] = useState('');
  const [internshipCompany, setInternshipCompany] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const newStudent = { username, internship_company: internshipCompany };
    const response = await createStudent(newStudent);
    setStudents((prev) => [...prev, response.data]);
    setUsername('');
    setInternshipCompany('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="text"
        placeholder="Internship Company"
        value={internshipCompany}
        onChange={(e) => setInternshipCompany(e.target.value)}
      />
      <button type="submit">Add Student</button>
    </form>
  );
};

export default StudentForm;

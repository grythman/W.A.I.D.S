// src/components/StudentList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function StudentList() {
    const [students, setStudents] = useState([]);

    useEffect(() => {
        const fetchStudents = async () => {
            const response = await axios.get('/api/students/');
            setStudents(response.data);
        };
        fetchStudents();
    }, []);

    return (
        <div>
            <h2>Students</h2>
            <ul>
                {students.map((student) => (
                    <li key={student.id}>{student.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default StudentList;

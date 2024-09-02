import React, { useEffect, useState } from 'react';
import axios from 'axios';

function StudentList() {
    const [students, setStudents] = useState([]);

    useEffect(() => {
        const fetchStudents = async () => {
            try {
                const response = await axios.get('/api/students/');
                setStudents(response.data);
            } catch (error) {
                console.error('Error fetching students:', error);
            }
        };

        fetchStudents();
    }, []);

    return (
        <div>
            <h2>Students List</h2>
            <ul>
                {students.map(student => (
                    <li key={student.id}>{student.username} - {student.internship_company}</li>
                ))}
            </ul>
        </div>
    );
}

export default StudentList;

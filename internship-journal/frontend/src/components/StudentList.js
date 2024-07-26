import React, { useEffect, useState } from 'react';
import axios from 'axios';

const StudentList = () => {
    const [students, setStudents] = useState([]);

    useEffect(() => {
        axios.get('/api/students/')
            .then(response => {
                setStudents(response.data);
            })
            .catch(error => {
                console.error("There was an error fetching the students!", error);
            });
    }, []);

    return (
        <div>
            <h2>Student List</h2>
            <ul>
                {students.map(student => (
                    <li key={student.id}>{student.user.username}</li>
                ))}
            </ul>
        </div>
    );
}

export default StudentList;

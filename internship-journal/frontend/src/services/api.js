import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api', // Adjust based on your Django setup
});

export const fetchMentors = () => api.get('/mentors/');
export const createMentor = (data) => api.post('/mentors/', data);

export const fetchStudents = () => api.get('/students/');
export const createStudent = (data) => api.post('/students/', data);

export const fetchJournalEntries = () => api.get('/journal-entries/');
export const createJournalEntry = (data) => api.post('/journal-entries/', data);

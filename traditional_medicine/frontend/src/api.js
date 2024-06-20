// src/api.js
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

export const registerPatient = (patientData) => axios.post(`${API_BASE_URL}/register/`, patientData);
export const bookAppointment = (appointmentData) => axios.post(`${API_BASE_URL}/book_appointment/`, appointmentData);

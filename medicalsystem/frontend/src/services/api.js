import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

export const getPatients = async () => {
    return await axios.get(`${API_URL}patients/`);
};

export const getDoctors = async () => {
    return await axios.get(`${API_URL}doctors/`);
};

export const getAppointments = async () => {
    return await axios.get(`${API_URL}appointments/`);
};

export const getMedicalHistories = async () => {
    return await axios.get(`${API_URL}medicalhistories/`);
};

export const getPayments = async () => {
    return await axios.get(`${API_URL}payments/`);
};

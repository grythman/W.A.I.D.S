import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api/', // Adjust the baseURL to match your Django backend URL
});

export default axiosInstance;
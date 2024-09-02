import React, { useState } from 'react';
import axiosInstance from './axiosInstance';

const StudentRegister = () => {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
    // Add other fields as necessary
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axiosInstance.post('register/', formData)
      .then(response => {
        console.log('Registration successful', response.data);
      })
      .catch(error => {
        console.error('There was an error registering!', error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="username"
        value={formData.username}
        onChange={handleChange}
        placeholder="Username"
      />
      <input
        type="password"
        name="password"
        value={formData.password}
        onChange={handleChange}
        placeholder="Password"
      />
      <button type="submit">Register</button>
    </form>
  );
};

export default StudentRegister;
import React, { useState, useEffect } from 'react';
import { getDoctors, createAppointment } from '../../services/api';

const MakeAppointment = () => {
  const [doctors, setDoctors] = useState([]);
  const [formData, setFormData] = useState({
    doctor: '',
    date: ''
  });

  useEffect(() => {
    getDoctors().then(response => {
      setDoctors(response.data);
    });
  }, []);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    createAppointment(formData).then(response => {
      alert('Appointment created successfully!');
    }).catch(error => {
      alert('Error creating appointment!');
    });
  };

  return (
    <div>
      <h2>Make an Appointment</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Doctor:
          <select name="doctor" onChange={handleChange}>
            {doctors.map(doctor => (
              <option key={doctor.id} value={doctor.id}>
                {doctor.user.username} - {doctor.specialization}
              </option>
            ))}
          </select>
        </label>
        <label>
          Date:
          <input type="datetime-local" name="date" onChange={handleChange} />
        </label>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default MakeAppointment;
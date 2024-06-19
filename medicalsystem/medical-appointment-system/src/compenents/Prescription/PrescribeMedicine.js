import React, { useState, useEffect } from 'react';
import { getTreatmentHistories, createPrescription } from '../../services/api';

const PrescribeMedicine = () => {
  const [treatmentHistories, setTreatmentHistories] = useState([]);
  const [formData, setFormData] = useState({
    treatment: '',
    medicine: '',
    dosage: ''
  });

  useEffect(() => {
    getTreatmentHistories().then(response => {
      setTreatmentHistories(response.data);
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
    createPrescription(formData).then(response => {
      alert('Prescription created successfully!');
    }).catch(error => {
      alert('Error creating prescription!');
    });
  };

  return (
    <div>
      <h2>Prescribe Medicine</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Treatment:
          <select name="treatment" onChange={handleChange}>
            {treatmentHistories.map(treatment => (
              <option key={treatment.id} value={treatment.id}>
                {treatment.diagnosis}
              </option>
            ))}
          </select>
        </label>
        <label>
          Medicine:
          <input type="text" name="medicine" onChange={handleChange} />
        </label>
        <label>
          Dosage:
          <input type="text" name="dosage" onChange={handleChange} />
        </label>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default PrescribeMedicine;
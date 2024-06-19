import React, { useEffect, useState } from 'react';
import { getTreatmentHistories } from '../../services/api';

const ViewTreatmentHistory = () => {
  const [treatmentHistories, setTreatmentHistories] = useState([]);

  useEffect(() => {
    getTreatmentHistories().then(response => {
      setTreatmentHistories(response.data);
    });
  }, []);

  return (
    <div>
      <h2>Treatment History</h2>
      <ul>
        {treatmentHistories.map(history => (
          <li key={history.id}>
            {history.diagnosis} - {new Date(history.date).toLocaleString()} - {history.doctor.user.username}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ViewTreatmentHistory;
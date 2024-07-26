import React from 'react';
import { Link } from 'react-router-dom';

function Dashboard() {
  return (
    <div className="dashboard">
      <h2>Dashboard</h2>
      <div>
        <Link to="/journal">Journal</Link>
      </div>
      <div>
        <Link to="/feedback">Feedback</Link>
      </div>
    </div>
  );
}

export default Dashboard;

import React from 'react';
import { Link } from 'react-router-dom';
import Sidebar from './Sidebar';

function Dashboard() {
  return (
    <div className="dashboard">
      <Sidebar />
      <div className="dashboard-content">
        <h1>Welcome to the Internship Management System</h1>
        {/* Additional sections like faculty, students, internships, etc. */}
      </div>
    </div>
  );
}

export default Dashboard;

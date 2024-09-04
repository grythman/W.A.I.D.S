import React from 'react';
import './styles/HomePage.css';

const Home = () => {
  return (
    <div className="home-container">
      <h1>Welcome to the Internship Management System</h1>
      <p>
        This system allows mentors and students to track their internship progress
        and manage journal entries. You can view and add mentors, students, and
        journal entries using the navigation above.
      </p>
    </div>
  );
};

export default Home;

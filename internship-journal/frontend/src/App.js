import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './components/HomePage';
import LoginPage from './components/LoginPage';
import Register from './components/Register';
import Dashboard from './components/Dashboard';
import Journal from './components/Journal';
import Feedback from './components/Feedback';
import StudentList from './components/StudentList';
import './styles/App.css';

const App = () => {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/journal" element={<Journal />} />
        <Route path="/feedback" element={<Feedback />} />
        <Route path="/students" element={<StudentList />} />
      </Routes>
    </Router>
  );
};

export default App;

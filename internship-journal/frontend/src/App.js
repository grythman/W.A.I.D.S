// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './components/HomePage';
import LoginPage from './components/LoginPage';
import Register from './components/Register';
import Dashboard from './components/Dashboard';
import Feedback from './components/Feedback';
import Journal from './components/Journal';
import StudentList from './components/StudentList';

function App() {
    return (
        <Router>
            <div className="App">
                <Navbar />
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/register" element={<Register />} />
                    <Route path="/dashboard" element={<Dashboard />} />
                    <Route path="/feedback" element={<Feedback />} />
                    <Route path="/journal" element={<Journal />} />
                    <Route path="/students" element={<StudentList />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;

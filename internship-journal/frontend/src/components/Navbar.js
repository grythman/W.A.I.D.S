// Navbar.js
import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav className="navbar">
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/login">Login</Link></li>
                <li><Link to="/register">Register</Link></li>
                <li><Link to="/dashboard">Dashboard</Link></li>
                <li><Link to="/feedback">Feedback</Link></li>
                <li><Link to="/journal">Journal</Link></li>
                <li><Link to="/students">Students</Link></li>
            </ul>
        </nav>
    );
}

export default Navbar;

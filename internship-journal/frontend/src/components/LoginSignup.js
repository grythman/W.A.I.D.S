// LoginSignup.js
import React, { useState } from 'react';

const LoginSignup = () => {
    const [role, setRole] = useState('Student');

    const handleRoleChange = (event) => {
        setRole(event.target.value);
    };

    return (
        <div className="login-signup">
            <h2>Login / Signup</h2>
            <form>
                <label htmlFor="role">Role:</label>
                <select id="role" value={role} onChange={handleRoleChange}>
                    <option value="Student">Student</option>
                    <option value="Mentor">Mentor</option>
                    <option value="Teacher">Teacher</option>
                    <option value="Admin">Admin</option>
                </select>

                <label>Email:</label>
                <input type="email" required />

                <label>Password:</label>
                <input type="password" required />

                <button type="submit">Submit</button>
            </form>
        </div>
    );
}

export default LoginSignup;

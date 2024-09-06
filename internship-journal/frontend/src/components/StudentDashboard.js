// StudentDashboard.js
import React from 'react';

const StudentDashboard = () => {
    return (
        <div className="student-dashboard">
            <h2>Student Dashboard</h2>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#submit-report">Submit Internship Report</a></li>
                    <li><a href="#evaluations">View Evaluations</a></li>
                    <li><a href="#messages">Messages</a></li>
                </ul>
            </nav>

            <section className="main-content">
                <h3>Internship Progress</h3>
                <progress value="70" max="100">70%</progress>

                <h3>Submit Report</h3>
                <form>
                    <input type="file" accept=".pdf" />
                    <button type="submit">Upload Report</button>
                </form>

                <h3>Evaluation Status</h3>
                <p>Your report is under review by the mentor.</p>
            </section>
        </div>
    );
}

export default StudentDashboard;

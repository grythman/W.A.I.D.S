import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from './components/HomePage';
import MentorList from './components/MentorList';
import StudentList from './components/StudentList';
import JournalEntryList from './components/JournalEntryList';
import './styles/App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>Internship Management System</h1>
          <nav>
            <Link to="/">Home</Link>
            <Link to="/mentors">Mentors</Link>
            <Link to="/students">Students</Link>
            <Link to="/journal-entries">Journal Entries</Link>
          </nav>
        </header>
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/mentors" element={<MentorList />} />
            <Route path="/students" element={<StudentList />} />
            <Route path="/journal-entries" element={<JournalEntryList />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;

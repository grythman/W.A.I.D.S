// App.js
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar";
import HomePage from "./components/HomePage";
import LoginPage from "./components/LoginPage";
import Register from "./components/Register";
import Dashboard from "./components/Dashboard";
import Feedback from "./components/Feedback";
import Journal from "./components/Journal";
import StudentList from "./components/StudentList";
import MentorList from "./components/MentorList";
import MentorDetail from "./components/MentorDetail";
import MentorForm from "./components/MentorForm";

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
          <Route path="/mentors" element={<MentorList />} />
          <Route path="/mentors/create" element={<MentorForm />} />
          <Route path="/mentors/:id" element={<MentorDetail />} />
          <Route path="/mentors/:id/update" element={<MentorForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
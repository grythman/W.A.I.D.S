// src/App.js

import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import Patients from './components/Patients';
import PatientForm from './components/PatientForm';
import Doctors from './components/Doctors';
import Appointments from './components/Appointments';
import MedicalHistories from './components/MedicalHistories';
import Payments from './components/Payments';
import './style.css';  // Importing the CSS file

const App = () => {
    return (
        <Router>
            <div>
                <nav>
                    <ul>
                        <li><Link to="/patients">Patients</Link></li>
                        <li><Link to="/doctors">Doctors</Link></li>
                        <li><Link to="/appointments">Appointments</Link></li>
                        <li><Link to="/medicalhistories">Medical Histories</Link></li>
                        <li><Link to="/payments">Payments</Link></li>
                    </ul>
                </nav>
                <Switch>
                    <Route path="/patients" exact component={Patients} />
                    <Route path="/patients/new" component={PatientForm} />
                    <Route path="/patients/:id/edit" component={PatientForm} />
                    <Route path="/doctors" component={Doctors} />
                    <Route path="/appointments" component={Appointments} />
                    <Route path="/medicalhistories" component={MedicalHistories} />
                    <Route path="/payments" component={Payments} />
                </Switch>
            </div>
        </Router>
    );
};

export default App;

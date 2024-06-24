import React from 'react';
import './App.css';
import RequestOnboarding from './RequestOnboarding';
import AssignTask from './AssignTask';
import CompleteTask from './CompleteTask';
import SubmitDocument from './SubmitDocument';
import CompleteModule from './CompleteModule';
import SetupITResources from './SetupITResources';
import SendNotification from './SendNotification';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <h1>Automated Employee Onboarding System</h1>
                <RequestOnboarding />
                <AssignTask />
                <CompleteTask />
                <SubmitDocument />
                <CompleteModule />
                <SetupITResources />
                <SendNotification />
            </header>
        </div>
    );
}

export default App;

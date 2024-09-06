// src/App.js
import React from 'react';
import Header from './components/Header';
import MainBanner from './components/MainBanner';
import Features from './components/Features';
import Testimonials from './components/Testimonials';
import Statistics from './components/Statistics';
import Footer from './components/Footer';
import './styles/App.css';

function App() {
    return (
        <div className="App">
            <Header />
            <MainBanner />
            <Features />
            <Testimonials />
            <Statistics />
            <Footer />
        </div>
    );
}

export default App;

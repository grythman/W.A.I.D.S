// Header.js
import React from 'react';

const Header = () => {
    return (
        <header>
            <div className="logo">IMS Logo</div>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#contact">Contact</a></li>
                    <li><a href="#login">Login/Signup</a></li>
                </ul>
            </nav>
            <div className="language-switcher">
                <button>EN</button>
                <button>MN</button>
            </div>
        </header>
    );
}

export default Header;

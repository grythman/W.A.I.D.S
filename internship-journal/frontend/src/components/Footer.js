// src/components/Footer.js
import React from 'react';

const Footer = () => {
    return (
        <footer>
            <ul>
                <li><a href="#privacy-policy">Privacy Policy</a></li>
                <li><a href="#terms-of-use">Terms of Use</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <div className="social-icons">
                <a href="https://facebook.com">Facebook</a>
                <a href="https://twitter.com">Twitter</a>
            </div>
        </footer>
    );
}

export default Footer;

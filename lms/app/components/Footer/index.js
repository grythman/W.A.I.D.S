/**
*
* Footer
*
*/

import React from 'react';
import PropTypes from 'prop-types';

import './style.css';
import './styleM.css';

const Footer = () => {
  return (
    <div className="footerComponent">
      <span></span>
      <span className="footerCopyright">LMS - Copyright 2024 | All Rights Reserved</span>
      <span></span>
    </div>
  );
};

Footer.propTypes = {
  someProp: PropTypes.string,
  anotherProp: PropTypes.number,
};

export default Footer;
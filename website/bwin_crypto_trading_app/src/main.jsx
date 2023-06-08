import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import Routes from './components/Routes';
import './index.css';

const rootElement = document.getElementById('root');

ReactDOM.render(
  <Router>
    <React.StrictMode>
      <Routes />
    </React.StrictMode>
  </Router>,
  rootElement
);

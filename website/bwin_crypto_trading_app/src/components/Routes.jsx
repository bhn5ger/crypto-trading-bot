import React from 'react';
import { Route, Switch } from 'react-router-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import App from '../App';
import LoginForm from './Login';

const Routes = () => {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={App} />
        <Route exact path="/login" component={LoginForm} />
      </Switch>
    </Router>
  );
};

export default Routes;

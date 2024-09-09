// lms/app/containers/App/index.js
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import { Switch, Route, Redirect } from 'react-router-dom';
import { withRouter } from 'react-router';

import Home from 'containers/Home';
import Browse from 'containers/Browse';
import Detail from 'containers/Detail';
import Lessons from 'containers/Lessons';
import Dashboard from 'containers/Dashboard';
import Single from 'containers/Single';
import New from 'containers/New';
import SignIn from 'containers/SignIn';
import SignUp from 'containers/SignUp';
import Enroll from 'containers/Enroll';
import About from 'containers/About';
import NotFound from 'containers/NotFound';

import Snackbar from 'material-ui/Snackbar';
import Dialog from 'material-ui/Dialog';
import { Tabs, Tab } from 'material-ui/Tabs';
import TextField from 'material-ui/TextField';
import FlatButton from 'material-ui/FlatButton';

import './style.css';
import './styleM.css';

class App extends Component {
  constructor() {
    super();
    this.state = {
      token: localStorage.getItem('token') || "",
      user: JSON.parse(localStorage.getItem('user')) || {},
      snack: false,
      msg: "",
      email: "",
      username: "",
      password: "",
      authOpen: false,
      activeTab: 0,
    };
  }

  static propTypes = { children: PropTypes.node };
  static childContextTypes = { muiTheme: PropTypes.object };

  getChildContext() {
    var theme = getMuiTheme();
    theme.textField.focusColor = "#6fc13e";
    theme.inkBar.backgroundColor = "#38ae47";
    theme.tabs.backgroundColor = "#6fc13e";
    return { muiTheme: theme };
  }

  handleRequestClose = () => {
    this.setState({ snack: false, msg: "" });
  };

  showSnack = (msg) => {
    this.setState({ snack: true, msg: msg });
  };

  handleUsername = (event) => {
    this.setState({ username: event.target.value });
  };

  handleEmail = (event) => {
    this.setState({ email: event.target.value });
  };

  handlePassword = (event) => {
    this.setState({ password: event.target.value });
  };

  handleAuth = () => {
    this.setState({ authOpen: !this.state.authOpen });
  };

  signIn = () => {
    const { username, password } = this.state;

    fetch('http://localhost:8000/signIn/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    })
      .then(response => response.json())
      .then(json => {
        if (json.error) {
          this.showSnack(json.error);
        } else if (json.access) {
          localStorage.setItem('token', json.access);
          this.setState({ token: json.access });
          return fetch('http://localhost:8000/getUser/', {
            method: 'GET',
            headers: {
              Authorization: `Bearer ${json.access}`,
            },
          });
        }
        throw new Error('Unexpected response');
      })
      .then(response => response.json())
      .then(json => {
        localStorage.setItem('user', JSON.stringify(json.user));
        this.setState({ user: json.user });
        this.showSnack(`Welcome ${json.user.username}`);
        this.handleAuth();
      })
      .catch(error => this.showSnack(error.message));
  };

  signUp = () => {
    const { email, username, password } = this.state;

    fetch('http://localhost:8000/signUp/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, username, password }),
    })
      .then(response => response.json())
      .then(json => {
        if (json.error) {
          this.showSnack(json.error);
        } else if (json.success) {
          this.signIn();
        }
      })
      .catch(error => this.showSnack(error.message));
  };

  signOut = (redirect = false) => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    this.showSnack("Good-bye!");
    this.setState({
      token: "",
      user: {},
    }, () => {
      if (redirect) {
        setTimeout(() => this.props.history.push('/'), 2000);
      }
    });
  };

  render() {
    return (
      <div>
        <MuiThemeProvider>
          <Switch>
            <Route exact path='/' render={() => <Home app={this} />} />
            <Route path='/browse' render={() => <Browse app={this} />} />
            <Route path='/course/:id' render={(props) => <Detail {...props} app={this} />} />
            <Route path='/lesson/:id/:lid' render={(props) => <Lessons {...props} app={this} />} />
            <Route path='/lesson/:id' render={(props) => <Lessons {...props} app={this} />} />
            <Route path='/dashboard' render={(props) => <Dashboard {...props} app={this} />} />
            <Route path='/detail/:id' render={(props) => <Single {...props} app={this} />} />
            <Route path='/update/:id' render={(props) => <New {...props} app={this} />} />
            <Route path='/enroll/:id' render={(props) => <Enroll {...props} app={this} />} />
            <Route path='/about' render={() => <About app={this} />} />
            <Route path='/signUp' render={() => <SignUp app={this} />} />
            <Route path='/signIn' render={() => <SignIn app={this} />} />
            <Route path='*' render={() => <NotFound />} />
          </Switch>
        </MuiThemeProvider>

        <Dialog onRequestClose={this.handleAuth} open={this.state.authOpen} bodyStyle={{ padding: "0" }}>
          <Tabs value={this.state.activeTab} onChange={(value) => this.setState({ activeTab: value })}>
            <Tab label="Sign In">
              <div className="lmsAuthBlock">
                <div className="lmsAuthHeader">Sign In to LMS</div>
                <TextField floatingLabelText="Username" fullWidth={true} onChange={this.handleUsername} value={this.state.username} />
                <TextField floatingLabelText="Password" fullWidth={true} onChange={this.handlePassword} value={this.state.password} type="password" />
                <FlatButton style={{ marginTop: '15px', color: "#FFFFFF", background: "#6fc13e", width: "100%" }} onClick={this.signIn}>Sign In</FlatButton>
              </div>
            </Tab>
            <Tab label="Sign Up">
              <div className="lmsAuthBlock">
                <div className="lmsAuthHeader">Sign Up to LMS</div>
                <TextField floatingLabelText="Full Name" fullWidth={true} onChange={this.handleUsername} value={this.state.username} />
                <TextField floatingLabelText="E-Mail" fullWidth={true} onChange={this.handleEmail} value={this.state.email} />
                <TextField floatingLabelText="Password" fullWidth={true} onChange={this.handlePassword} value={this.state.password} type="password" />
                <FlatButton style={{ marginTop: '15px', color: "#FFFFFF", background: "#6fc13e", width: "100%" }} onClick={this.signUp}>Sign Up</FlatButton>
              </div>
            </Tab>
          </Tabs>
        </Dialog>
        <Snackbar
          open={this.state.snack}
          message={this.state.msg}
          autoHideDuration={3000}
          onRequestClose={this.handleRequestClose}
        />
      </div>
    );
  }
}

export default withRouter(App);

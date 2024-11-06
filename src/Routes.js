import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'; // Fix import statement
import LoginPage from './pages/LoginPage';
import HomePage from './pages/HomePage';
import SignupPage from './pages/SignupPage';
import NotFound from './pages/NotFound'

export const Routes = () => {
    return (
        <Router>
            <Switch>
                <Route exact path="/">  {/* Add "exact" here */}
                    <LoginPage/>
                </Route>
                <Route path="/home">
                    <HomePage/>
                </Route>
                <Route path="/signin">
                    <SignupPage/>
                </Route>
                <Route path="*" component={NotFound} /> {/* This is your 404 route */}
            </Switch>
        </Router>
    );
};

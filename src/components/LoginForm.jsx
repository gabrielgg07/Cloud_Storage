import React, { useState } from 'react';
import './LoginForm.css';

const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();

    const response = await fetch('  https://11c0-50-231-135-50.ngrok-free.app/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();
    if (response.ok) {
      alert(data.message);
    } else {
      alert(data.error);
    }
  };

  return (
    <div className="Login">
      <div className="Header">
        <h1 id="Header-text">Welcome</h1>
        <div className="Header-subtext">
          <h3>Sign In</h3>
        </div>
      </div>
      <div className="form-container">
        <form onSubmit={handleSubmit}>
          <div className="input-container">
            <input
              type="email"
              id="email"
              className="input-box"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <input
              type="password"
              id="password"
              className="input-box"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
            <button type="submit" className="action-button">
              Log In
            </button>
            <p>
              Don't have an account? <a href="/signin">Sign Up</a>
            </p>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginForm;

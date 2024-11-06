import React from 'react';
import LoginForm from '../components/LoginForm';
import '../App.css'

function LoginPage() {
  return (
    <div>
    <div className='circle'></div>
    <div className='App'>
      <div className='circle1'></div>
      <div className='circle2'></div>
      <div className='circle3'></div> 
      <LoginForm/>
    </div>
  </div>
  )
}

export default LoginPage;

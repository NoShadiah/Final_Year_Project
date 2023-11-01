import React, { useState, useEffect } from "react";
// import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { BrowserRouter as Router } from "react-router-dom";
import {Route, Navigate, Routes} from "react-router-dom";
// import "./App.css";
import { Dashboard } from "./dashboard";
import { Login } from "./components/login_signup/login";
import {SignUp} from "./components/login_signup/signup"
import { Navbar } from "./Layout/layout";
import { Forgotpassword } from "./components/login_signup/forgotpassword";


export default function App(){
  const [loggedIn, setLoggedIn] = useState(false);
  const [userType, setUserType] = useState('');
  const userTypeFromStorage = localStorage.getItem('user_type');
  

  
  
  return (<>
        <Router>
          {/* <Navbar/> */}
            <Routes>
                
                      <Route index element={<Login/>}/>
                      <Route path="/dashboard" element={<Dashboard/>} />
                      <Route path="/login" element={<Login/>} /> 
                      <Route path="/signup" element={<SignUp/>} /> 
                      <Route path="/passwordreset" element={<Forgotpassword/>}/> 
            </Routes>
        </Router>
    </>
  )
};


//   {/* // const handleLogout = () => { */}
//   {/* //   // Clear user type from local storage */}
//   {/* //   localStorage.removeItem('userType');


  

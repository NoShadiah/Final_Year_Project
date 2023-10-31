import React from "react";
import { useNavigate } from "react-router-dom";

import "./styling.css";

export function Forgotpassword(){
    const navigate = useNavigate();

    return(
        <section className="section">
        <div class="form-box">
            <div class="form-value">
                <form onSubmit={()=>{navigate("/login")}}>
                    <h2>Reset password</h2>
                    <p> Enter your account email and you will<br></br> receive a password reset link</p>
                    <div class="inputbox">
                        {/* <!-- from fontawesome i will get the icons for the input labels --> */}
                        <label for="email">Email: </label>
                        <i class="fas fa-envelope"></i>
                        <input type="email" required name="email"/>
                        
                    </div>
                    <button id="button">Send link</button>
                    <div classname="register">
                        <p><a href="/login">Back to login</a></p>
                    </div>

                </form>
            </div>
        </div>
    </section>
    )
}
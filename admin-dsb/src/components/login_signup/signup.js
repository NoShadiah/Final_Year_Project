import {useEffect, useState} from "react";
import { useNavigate } from "react-router-dom";
import "./styling.css"
// import APIService from "./posting";
// Number 1
export function SignUp(){
    const navigate = useNavigate();
    const [firstname, setFirstName]=useState("");
    const [lastname, setLastName]=useState("");
    const [email, setEmail]=useState("");
    const [contact, setContact]=useState("");
    const [usertype, setUserType]=useState("Client");
    const [address, setAddress]=useState("");
    const [gender, setGender]=useState("F");
    const [password, setPassword]=useState("");
    const[success, setSuccess] = useState("");
    const ChangeFirstName=(e)=>{
             setFirstName(e.target.value)
            
             console.log(firstname)

    }
    const ChangeLastName=(e)=>{
        setLastName(e.target.value)
       
        console.log(lastname)

}
    const ChangeEmail=(e)=>{
        
       setEmail(e.target.value)
        console.log(email)
    }
    const ChangeContact=(e)=>{
        
        setContact(e.target.value)
        console.log(contact)
    }
    const ChangeAddress=(e)=>{
        
        setAddress(e.target.value)
        console.log(address)
    }
    const ChangeGender=(e)=>{
        
        setGender(e.target.value)
        console.log(gender)
    }
    const ChangePassword=(e)=>{
        
        setPassword(e.target.value)
        console.log(password)
    }
    

    function InsertUser(){
       const data = {
        firstname,
        lastname,
        email,
        contact,
        address,
        password,
        user_type:usertype,
        gender
    }
    

        fetch("http://localhost:5000/api/v1/users/register", {
        method: "POST", // or 'PUT'
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
        })
        .then((response) => response.json())
        .then((data) => {
            console.log("Success:", data);
        })
        .catch((error) => {
            console.error("Error:", error);
        });
    }
        
  
      const handleSubmit=()=>{ 
        InsertUser()
        navigate("/verify")
      }
    
    return(

    <div id="mysection">
    <div class="form-box">
        
        <div class="form-value">
            
            <form onSubmit={handleSubmit()} >
                <h2>Sign Up</h2>
                <div id="signupform">
                    <div class="inputbox">
                        {/* <!-- from fontawesome i will get the icons for the input labels --> */}
                        <label for="name">First name: </label>
                        <i class="fas fa-person"></i>
                        <input type="text" required name="name"/>
                        
                    </div>
                    <div class="inputbox">
                        {/* <!-- from fontawesome i will get the icons for the input labels --> */}
                        <label for="name">Last name: </label>
                        <i class="fas fa-person"></i>
                        <input type="text" required name="name"/>
                        
                    </div>
                    <div class="inputbox">
                        {/* <!-- from fontawesome i will get the icons for the input labels --> */}
                        <label for="email">Email: </label>
                        <i class="fas fa-envelope"></i>
                        <input type="email" required name="email"/>
                        
                    </div>
                    <div class="inputbox">
                        {/* <!-- from fontawesome i will get the icons for the input labels --> */}
                        <label for="usertype">User Type: </label>
                        <i class="fas fa-person"></i>
                        <input type="text" required name="usertype"/>
                        
                    </div>
                    <div class="inputbox">
                        {/* <!-- from fontawesome i will get the icons for the input labels --> */}
                        <label for="address">Address: </label>
                        <i class="fas fa-person"></i>
                        <input type="text" required name="address"/>
                        
                    </div>
                    <div class="inputbox">
                        {/* <!-- from fontawesome i will get the icons for the input labels --> */}
                        <label for="gender">Gender: </label>
                        <i class="fas fa-person"></i>
                        <input type="text" required name="gender"/>
                        
                    </div>
                    <div class="inputbox">
                        {/* <!-- from fontawesome i will get the icons for the input labels --> */}
                        <label for="profile">Profile photo: </label>
                        <i class="fas fa-person"></i>
                        <input type="file" required name="profile"/>
                        
                    </div>
                    <div class="inputbox">
                        {/* <!-- from fontawesome i will get the icons for the input labels --> */}
                        <label for="password">Password:</label>
                        <i class="fas fa-lock"></i>
                        <input type="password" required name="password"/>
                        
                    </div>
                    <div class="inputbox">
                        {/* <!-- from fontawesome i will get the icons for the input labels --> */}
                        <label for="password">Confirm Password:</label>
                        <i class="fas fa-lock"></i>
                        <input type="password" required name="password"/>
                        
                    </div>
                
                </div>
                
                
                 {/* <div class="forget">
                   
                        <label for="">
                            <input type="checkbox">Remeber Me 
                        </label> 
            
                
                </div>  */}
                <button id="button">Submit</button>
                <div class="register">
                    <p>Already have an account? <a href="/login">Log In</a></p>
                </div>
            </form>
        </div>
    </div>
</div>
    )
}
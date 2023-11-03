import {useState, use} from "react";
import { useNavigate } from "react-router-dom";
import "./styling.css";
// Step number 1
export function Login(){
    const navigate = useNavigate();
    const [password, setPassword]=useState("");
    const [email, setEmail]=useState("");
    const [code, setCode]=useState("");
    const [user_type, setUserType]=useState("");
    const [isAdmin, setIsAdmin]= useState(false);
    
    const Change=(e)=>{
             setPassword(e.target.value)
            
             console.log(password)

    }
    const ChangeEmail=(e)=>{
        
       setEmail(e.target.value)
        console.log(email)
    }

    const ChangeCode=(e)=>{
        
        setCode(e.target.value)
         console.log(code)
     }
    
    function UserLogin(){
        // const [isloggedIn, setIsLoggedIn] = useState(false)
        const details = {
            method:'POST',
            headers:{
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                email,
                password,
                code
            })
        }
        fetch('http://127.0.0.1:5000/api/v1/auth/login', details)
        .then(response => response.json())
        .then((data)=>{
            console.log(data); 
            if (data.access_token){
                // setIsLoggedIn(true);
                // alert(data.message);
                // setUserType(data.user_type);
                if (data.user_type === "Student" || data.user_type === "student"){
                    navigate("/studenthome")
                }else if (data.user_type === "Company" || data.user_type === "company") {
                    navigate("/companyhome")
                } else if (data.user_type === "Super Admin" || data.user_type === "Assistant Admin"){
                    navigate("/dashboard")
                };
                localStorage.setItem('access_token', JSON(data.access_token));
                localStorage.setItem('refresh_token', JSON(data.refresh_token));
                localStorage.setItem('user_type', JSON(data.user_type));
                
                
            }
            else{
                
                    alert(data.message);
                

            }
            

    })
        .catch(error =>(
            console.error("There is a problem with the data", error)
        ))
    }
   
    const handleSubmit = (event) =>{
        event.preventDefault();
        
        
        UserLogin()
        setEmail("");
        setPassword("");
        setCode("");
        // console.log("Your password is",password+"!?23%4"+email+"!&")
    }
    return(
    <section className="section">
        <div class="form-box">
            <div class="form-value">
                <form onSubmit={handleSubmit}>
                    <h2>Login</h2>
                    <div class="inputbox">
                        {/* from fontawesome i will get the icons for the input labels  */}
                        <label for="email">Email: </label>
                        <i class="fas fa-envelope"></i>
                        <input 
                            type='email'
                            value={email}
                            onChange={ChangeEmail}
                            required name="email"/>
                        
                    </div>
                    <div class="inputbox">
                        {/*  from fontawesome i will get the icons for the input labels */}
                        <label for="password">Password:</label>
                        <i class="fas fa-lock"></i>
                        <input 
                                type='password'
                                value={password}
                                onChange={Change} 
                                required name="password"/>
                        
                    </div>
                    <div class="inputbox">
                        {/*  from fontawesome i will get the icons for the input labels */}
                        <label for="code">Company code:</label>
                        <i class="fas fa-lock"></i>
                        <input 
                                type='text'
                                value={code}
                                onChange={ChangeCode} 
                                name="code"/>
                        
                    </div>
                    <div class="forget">
                       
                            <label for="">
                                <input type="checkbox"/>Remeber Me 
                            </label> 
                        <a href="/passwordreset">Forgot Password</a>
                    
                    </div>
                    <button id="button">login</button>
                    <div class="register">
                        <p>Don't have an account? <a href="/signup">Sign Up</a></p>
                    </div>
                </form>
            </div>
        </div>
    </section>

    )
}
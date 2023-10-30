import {useState} from "react";
import "./styling.css";
// Step number 1
export function Login(){
    const [password, setPassword]=useState("");
    const [email, setEmail]=useState("");
    
    const Change=(e)=>{
             setPassword(e.target.value)
            
             console.log(password)

    }
    const ChangeEmail=(e)=>{
        
       setEmail(e.target.value)
        console.log(email)
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
                password
            })
        }
        fetch('http://127.0.0.1:5000/api/v1/users/token', details)
        .then(response => response.json())
        .then((data)=>{
            console.log(data); 
            if (data.access_token){
                // setIsLoggedIn(true);
                localStorage.setItem('access_token', JSON.stringify(data.access_token));
                localStorage.setItem('refresh_token', JSON.stringify(data.refresh_token));
                localStorage.setItem('user_type', JSON.stringify(data.user_type));
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
        // console.log("Your password is",password+"!?23%4"+email+"!&")
    }
    return(
    //     <div id='form1'>
    //     <h1>Please Login to go further.</h1>
    //     <form onSubmit={handleSubmit}>
    //         <div>
    //             <label>Enter email: </label>
    //             <input 
    //             type='email'
    //             value={email}
    //             onChange={ChangeEmail}/>
    //         </div>
    //         <div>
    //             <label>Enter your password: </label>
    //             <input 
    //             type='password'
    //             value={password}
    //             onChange={Change}
    //             />
    //         </div>
            
    //         <div>
    //             <button >LogIn</button>
    //         </div>
    //     </form>

    // </div>

    <section className="section">
        <div class="form-box">
            <div class="form-value">
                <form action="" onsubmit="">
                    <h2>Login</h2>
                    <div class="inputbox">
                        {/* from fontawesome i will get the icons for the input labels  */}
                        <label for="email">Email: </label>
                        <i class="fas fa-envelope"></i>
                        <input type="email" required name="email"/>
                        
                    </div>
                    <div class="inputbox">
                        {/*  from fontawesome i will get the icons for the input labels */}
                        <label for="password">Password:</label>
                        <i class="fas fa-lock"></i>
                        <input type="password" required name="password"/>
                        
                    </div>
                    <div class="forget">
                       
                            <label for="">
                                <input type="checkbox"/>Remeber Me 
                            </label> 
                        <a href="forgotpassword.html">Forgot Password</a>
                    
                    </div>
                    <button><a href="../Dashboard/landing.html">log In</a></button>
                    <div class="register">
                        <p>Don't have an account? <a href="/frontend/authentication/signup.html">Sign Up</a></p>
                    </div>
                </form>
            </div>
        </div>
    </section>

    )
}
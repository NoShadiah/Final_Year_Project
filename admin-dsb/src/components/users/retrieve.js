import {useState, useEffect} from "react";
import "./viewall.css";
import {myusers} from "./data.js";

export function AllUsers() {
    

    // Fecth users
    const[users, setUsers] = useState([])
    useEffect(()=>{
        
        
        
        const fetchUsers = () => {
            const token = localStorage.getItem('access_token');
            
            fetch('http://localhost:5000/api/v1/users/all', {
              headers: { 
                'Content-Type': 'application/json'
                ,'Authorization': `Bearer Token ${token}`
              }
            })
            .then(response => {
              if (!response.ok) {
                throw new Error(response.statusText);
              }
              return response.json();
            })
            .then(data => {
              setUsers(data);
              localStorage.setItem('myUsers', JSON.stringify(data));
            })
            .catch(error => console.error(error));
          }
          
          fetchUsers();
    }, [])
    console.log("users state:",users)
    // console.log("storageUsers", JSON.parse(localStorage.getItem("myUsers")))
    return (
            <div id='viewalltable'>
                
                <div className='mylist'>
                   <table>
                         <tr className="head">
                            <th id="U_Id">User Id</th>
                            <th>Full Name</th>
                            <th>Email</th>
                            <th>User Type</th>
                            <th id="actions">Actions</th>
                            
                        </tr>
                        <hr></hr>
                        {
            myusers?.map(user =>(
                                <tr className="data">
                                    <td>{user["U_Id"]}</td>
                                    <td>{user["F_name"]} {user["L_name"]}</td>
                                    <td>{user["email"]}</td>
                                    <td>{user["user_type"]}</td>
                                    <td> <div id="buttons"><button>View</button> <button>Delete</button></div></td>
                                    
                                </tr>))
                        }
                                
                                </table>
                    </div>
                </div>
        )
}
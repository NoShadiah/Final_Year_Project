import React, { useState } from "react";
import ReactDOM from "react-dom/client";
import "./App.css"

import { Users } from "./components/users/retrieve";
import { UserRegister } from "./components/users/register";

import { Categories } from "./components/categories/retrieve";
import { Registercategory } from "./components/categories/register";
import { Gallery } from "./components/gallery/retrieve";
import { RegisterGalleryItem } from "./components/gallery/register";
import { RegisterFoodItem } from "./components/food_items/register";
import { FoodItems } from "./components/food_items/retrieve";
import { RegisterMenuItem } from "./components/menu/register";
import { SearchProduct } from "./components/menu/search";
import { MenuItems } from "./components/menu/retrieve";
import { Orders } from "./components/orders/retrieve";


import "./dstyling.css"
import "./styling.css"



export const Dashboard = () => {
    const [active, setActive] = useState("");
    
    
        
        return(
            
             
            // <div id="dashboard">
            //     <div>
            //     <div className="dropdown">
            //         <p className="dropbtn">Users</p>
            //         <div className="dropdown-content">
            //             <button className="btn" onClick={()=>setActive("register user")}>Register</button> <br></br>
            //             <button className="btn" onClick={()=>setActive("all users")}>View all</button> <br></br>
            //             <button className="btn" onClick={()=>setActive("update users")}>Update</button> <br></br>
            //             <button className="btn" onClick={()=>setActive("delete user")}>Delete</button> 
            //         </div>
            //     </div><br></br>
            //     <div className="dropdown">
            //         <p className="dropbtn">Food categories</p>
            //         <div className="dropdown-content">
            //             <button className="btn" onClick={()=>setActive("register food category")}>Register</button> <br></br>
            //             <button className="btn" onClick={()=>setActive("all Food categories")}>View all</button> <br></br>
            //             <button className="btn" onClick={()=>setActive("update Food categories")}>Update</button> <br></br>
            //             <button className="btn" onClick={()=>setActive("delete category")}>Delete</button> 
            //         </div>
            //     </div><br></br></div>
                
                
                
                
                
            
            
            
            <main>
        <section id="sidebar">
            <div class="profile">
                <div class="admin">
                    <img src="https://img.freepik.com/free-photo/group-afro-americans-working-together_1303-8983.jpg?size=626&ext=jpg&ga=GA1.2.538938599.1670853663&semt=ais" alt="" srcset=""/>
                   <div class="details">
                    <h3>Promise K</h3>
                    {/* <h5>Super Admin</h5> */}
                   </div>
                </div> 
                <span>X</span>
            </div>
            <div class="menu-items">
                <div class="dashboard">
                    Dashboard

                </div>

                <p id="p">All users</p>
                <div class="dropdown">
                    
                    <p className="dropbtn">Users</p>
                    <div className="dropdown-content">
                        <button className="btn" onClick={()=>setActive("register users item")}>Register</button> <br></br>
                        <button className="btn" onClick={()=>setActive("all users")}>View all</button> <br></br>
                        {/* // <button className="btn" onClick={()=>setActive("Search item")}>Search item</button> <br></br>
                        // <button className="btn" onClick={()=>setActive("update users")}>Update</button> <br></br>
                        // <button className="btn" onClick={()=>setActive("delete users item")}>Delete</button>  */}
                </div>
                </div>
                <div class="fields">
                    Fields of study
                </div>
                <div class="Students">
                    Students
                </div>
                <div class="Companies">
                    Companies
                </div>

                <p id="p">Connecting</p>
                <div class="internships">
                    Internships
                </div>
                <div class="matches">
                    Internship matches
                </div>
                <div class="applications">
                    Applications
                </div>
                <div class="testimonials">
                    Testimonials
                </div>

                <p id="p">Interviews</p>
                <div class="qn-categories">
                    Question categories
                </div>
                <div class="questions">
                    Questions
                </div>

                <p id="p">From users</p>
                <div class="messages">
                    Messages
                </div>
                <div class="faqs">
                    FAQs
                </div>
                <div class="reviews">
                    Reviews
                </div>

                <p id="p">Advanced</p>
                <div class="settings">
                    Settings
                </div>
                <div class="aprofile">
                    Profile
                </div>
                <div class="userroles">
                    User Roles
                </div>
                <p>Advanced</p>
                <div class="settings">
                    Settings
                </div>
                <div class="aprofile">
                    Profile
                </div>
                <div class="userroles">
                    User Roles
                </div>

                
                
            </div>     


        </section>
        <section id="mainpage">
            <nav id="navbar">
                <div class="logo">
                    <img src="https://img.freepik.com/free-photo/group-afro-americans-working-together_1303-8983.jpg?size=626&ext=jpg&ga=GA1.2.538938599.1670853663&semt=ais" alt="" srcset=""/>
                    <h5 class="menu">Menu</h5>
                </div>
                <div class="buttons">
                    <img src="https://img.freepik.com/free-photo/group-afro-americans-working-together_1303-8983.jpg?size=626&ext=jpg&ga=GA1.2.538938599.1670853663&semt=ais" alt="" srcset=""/>
                    <div class="button">
                        <button>Site</button>
                        <button>Logout</button>

                    </div>                
                </div>
                
            </nav>
           <div class="content " id="content_section">
            
                 
                     <div>
                        {/* for registering  */}
                         {active ==="register user" && <UserRegister/>}
                         {active ==="register food category" && <Registercategory/>}
                         {active ==="register food item" && <RegisterFoodItem/>}
                         {active ==="register menu item" && <RegisterMenuItem/>}
                         {active ==="Search item" && <SearchProduct/>}
                         {active ==="register gallery item" && <RegisterGalleryItem/>}
                         {active ==="Add settings" && <UserRegister/>}
                     
                        {/* for reading */}
                         {active === "all users" && <Users/> }
                         {active === "all Food categories" && <Categories/> }
                         {active === "all Food items" && <FoodItems/> }
                         {active === "all Menu" && <MenuItems/> }
                         {active === "all orders" && <Orders/> }
                         {active === "all gallery items" && <Gallery/> }
                         {active === "all settings" && <Users/> }
                     </div>
                 </div>

             
           
        </section>
    </main>

        );
    

    
}

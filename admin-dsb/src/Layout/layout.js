import './navbar.css';
import {Outlet, Link} from "react-router-dom";
export const Navbar=()=>{
    return(
        <>
            <div id='nav'>
                <Link to='/' id='item'>Home</Link>
                <Link to='/signup'id='item'>Signup</Link>
                <Link to='/dashboard'id='item'>Dashboard</Link>
                <Link to='/login' id='item'>Login</Link>
                <Link to='/site' id='item'>Site</Link>

                <Link to='/passwordreset' id='item'>#</Link>
                <button class="search button" type="button" aria-label="Search Button"> 
                <svg viewBox="0 0 24 24" fill="currentColor" width="24" height="24"> 
                    <path d="M18.031 16.617l4.283 4.282-1.415 1.415-4.282-4.283A8.96 8.96 0 0 1 11 20c-4.968 0-9-4.032-9-9s4.032-9 9-9 9 4.032 9 9a8.96 8.96 0 0 1-1.969 5.617zm-2.006-.742A6.977 6.977 0 0 0 18 11c0-3.868-3.133-7-7-7-3.868 0-7 3.132-7 7 0 3.867 3.132 7 7 7a6.977 6.977 0 0 0 4.875-1.975l.15-.15z"/> 
                </svg>     
</button>
            </div>
            <Outlet/>
        </>
    )
};
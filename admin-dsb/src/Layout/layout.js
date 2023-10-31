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
                <Link to='/site' id='item'>Skills Connect</Link>

                <Link to='/passwordreset' id='item'>#</Link>
            </div>
            <Outlet/>
        </>
    )
};
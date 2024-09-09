import { NavLink } from "react-router-dom"

function Header({ session }) {
    return (
        <header className="header">
            <NavLink to="/" className="button" style={{float: 'left'}}>Sellit</NavLink>
            {session !== null ? <NavLink to="/account" className="button" style={{float: 'right'}}>Account</NavLink> : <NavLink to="/login" className="button" style={{float: 'right'}}>Login</NavLink>}
            <NavLink to="/newlisting" className="button" style={{float: 'right'}}>New</NavLink>
            <NavLink to="/search" className="button" style={{float: 'right'}}>Search</NavLink>
        </header>
    )
}

export default Header;
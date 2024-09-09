import React, { useEffect, useState } from "react";
import { Routes, Route } from "react-router-dom";
import Header from "./Header.js"
import HomePage from "./HomePage.js"
import LoginPage from "./LoginPage.js"
import SignUpPage from "./SignUpPage.js"
import Account from "./Account.js"
import UserPage from "./UserPage.js"
import ListingPage from "./ListingPage.js"
import SearchPage from "./SearchPage.js"
import NewListing from "./ListingPage.js"

function App() {
  const [session, setSession] = useState([])

  useEffect(() => {
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((user) => setSession(user))
      }
    })
  }, [])

  return (
    <>
      <main>
        <Header session={ session }/>
          <Routes>
            <Route path="/" element={ <HomePage /> }/>
            <Route path="/login" element={ <LoginPage /> }/>
            <Route path='/signup' element={ <SignUpPage /> }/>
            <Route path='/account' element={ <Account /> }/>
            <Route path='/user/:id' element={ <UserPage /> }/>
            <Route path='/listing/:id' element={ <ListingPage /> }/>
            <Route path='/search' element={ <SearchPage /> }/>
            <Route path='/newlisting' element={ <NewListing /> }/>
          </Routes>
      </main>
    </>
  );
}

export default App;

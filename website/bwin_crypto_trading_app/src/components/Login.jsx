import React, {useEffect, useState} from "react";
import { gapi } from "gapi-script";
import "./loginform.css"
import styles from "../style";

const LoginForm = () => {

    useEffect(() => {
        function start() {
            gapi.client.init({
                clientId: "79474543031-tmjo35916ufn421ej3u1i2ljao2apr4s.apps.googleusercontent.com",
                scope: ""
            })
        }
        gapi.load('client: auth2', start)
    })

    const [popupStyle, showPopup] = useState("hide")

    const popup = () => {
        showPopup("login-popup")
        setTimeout(() => showPopup("hide"), 3000)
    }

    return (
        <div className="container">
          <div className="cover">

            <h1 className="flex-1 font-poppins font-semibold ss:text-[36px] text-[26px] text-white">
            View the financial dashboard tracking b<span className="text-gradient">Win's</span> performance
            </h1>

            <input type="text" placeholder="username" />
            <input type="password" placeholder="password" />
    
            <div className="login-btn" onClick={popup}>
                Login
            </div>
    
            <div className={popupStyle}>
              <h3>Login Failed</h3>
              <p>Username or password incorrect</p>
            </div>
          </div>
        </div>
      )
}

export default LoginForm
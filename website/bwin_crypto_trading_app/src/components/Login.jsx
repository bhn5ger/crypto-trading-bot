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
            <h1 className={`py-3 px-4 font-poppins font-normal text-[32px] text-white outline-none text-center ${styles}`}>
              Investor Login
            </h1>
            <h1 className={`py-3 px-4 font-poppins font-normal text-[16px] text-white outline-none text-center ${styles}`}>
              View bWin's financial dashboard <br></br> and track its performance
            </h1>

            <input type="text" placeholder="Username" />
            <input type="password" placeholder="Password" />
    
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
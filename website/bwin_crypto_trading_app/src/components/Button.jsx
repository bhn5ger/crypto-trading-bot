import React from "react";

const Button = ({ styles }) => (
  <button type="button" className={`py-3 px-4 font-poppins font-normal cursor-pointer text-[16px] text-primary bg-blue-gradient rounded-[10px] outline-none ${styles}`}>
    Investor Login
  </button>
);

export default Button;
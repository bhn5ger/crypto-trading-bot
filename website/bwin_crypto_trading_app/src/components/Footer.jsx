import styles from "../style";
import { bwin_logo } from "../assets";

const Footer = () => (
  <section className={`${styles.flexCenter} ${styles.paddingY} flex-col`}>
    <div className={`${styles.flexStart} md:flex-row flex-col mb-8 w-full`}>
      
      <div className="flex-[1] flex flex-col justify-start mr-10">
        <img
          src={bwin_logo}
          alt="bwin_logo"
          className="w-[170px] h-[72.14px] object-contain self-start"
        />
        <p className={`${styles.paragraph} mt-4 max-w-[312px]`}>
          Winning in winters.
        </p>
      </div> 

    </div>

    <div className="w-full flex justify-between items-center md:flex-row flex-col pt-6 border-t-[1px] border-t-[#3F3E45]">
      <p className="font-poppins font-normal text-center text-[18px] leading-[27px] text-white">
        Copyright Ⓒ 2023 Brian Nguyen. All Rights Reserved.
      </p>

    </div>
  </section>
);

export default Footer;
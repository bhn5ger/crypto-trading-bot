import { gridtrading } from "../assets";
import styles, { layout } from "../style";

const Billing = () => (
  <section id="product" className={layout.sectionReverse}>
    <div className={layout.sectionImgReverse}>
      <img src={gridtrading} alt="gridtrading" className="w-[100%] h-[100%] relative z-[5]" />

      {/* gradient start */}
      <div className="absolute z-[3] -left-1/2 top-0 w-[50%] h-[50%] rounded-full white__gradient" />
      <div className="absolute z-[0] w-[50%] h-[50%] -left-1/2 bottom-0 rounded-full pink__gradient" />
      {/* gradient end */}
    </div>

    <div className={layout.sectionInfo}>
      <h2 className={styles.heading2}>
        Betting on volatility
      </h2>
      <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
        Using the grid trading strategy, bWin identifies opportunities to exploit
        fluctuations around a calculated fixed price.
      </p>

    </div>
  </section>
);

export default Billing;
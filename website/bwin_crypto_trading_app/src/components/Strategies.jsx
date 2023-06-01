import { strategies } from "../assets";
import styles, { layout } from "../style";

const Strategies = () => (
  <section id="strategies" className={layout.sectionReverse}>
    <div className={layout.sectionImgReverse}>
    <div style={{ marginRight: '280px' }}>
      <img src={strategies} alt="strategies" className="w-[170%] h-[100%] relative z-[5] max-w-[1200px] max-h-[1200px]"/>
    </div>

      {/* gradient start */}
      <div className="absolute z-[3] -left-1/2 top-0 w-[50%] h-[50%] rounded-full white__gradient" />
      <div className="absolute z-[0] w-[50%] h-[50%] -left-1/2 bottom-0 rounded-full pink__gradient" />
      {/* gradient end */}
    </div>

    <div className={layout.sectionInfo}>
      <h2 className={styles.heading2}>
        Apply various trading strategies
      </h2>
      <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
        In addition to new trading strategies, use popular trading strategies 
        including grid trading, arbitrage, and fibonacci retracement that bet on volatility, 
        leverage differences in exchange rates, and calculate levels using the golden ratio.
      </p>

    </div>
  </section>


);

export default Strategies;
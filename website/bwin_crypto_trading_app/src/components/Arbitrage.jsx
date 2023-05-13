import { arbitrage } from "../assets";
import styles, { layout } from "../style";

const Arbitrage = () => (
  <section className={layout.section}>
    <div className={layout.sectionInfo}>
      <h2 className={styles.heading2}>
        Leveraging differences in exchange rates
      </h2>
      <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
        bWin takes advantage of differences in exchange rates for pairs of coins within a single exchange
        via triangle arbitrage, in addition to differences in exchange rates for pairs of coins between hundreds of exchanges.
      </p>
    </div>

    <div className={layout.sectionImg}>
      <img src={arbitrage} alt="arbitrage" className="w-[89%] h-[100%]" />
    </div>
  </section>  
);

export default Arbitrage;
import { fibonacci } from "../assets";
import styles, { layout } from "../style";

const Fibonacci = () => (
  <section className={layout.sectionReverse}>
    <div className={layout.sectionImgReverse}>
      <img src={fibonacci} alt="fibonacci" className="w-[95%] h-[100%] relative z-[5]" />

      {/* gradient start */}
      <div className="absolute z-[3] -left-1/2 top-0 w-[50%] h-[50%] rounded-full white__gradient" />
      <div className="absolute z-[0] w-[50%] h-[50%] -left-1/2 bottom-0 rounded-full pink__gradient" />
      {/* gradient end */}
    </div>

    <div className={layout.sectionInfo}>
      <h2 className={styles.heading2}>
        Calculating levels with the golden ratio
      </h2>
      <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
        Place entry orders, determine stop-loss levels, or set price targets with Fibonacci retracement levels.
      </p>

    </div>
  </section>
);

export default Fibonacci;
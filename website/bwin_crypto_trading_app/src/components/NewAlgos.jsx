import { novelalgo } from "../assets";
import styles, { layout } from "../style";

const NewAlgos = () => (
  <section className={layout.section}>
    <div className={layout.sectionInfo}>
      <h2 className={styles.heading2}>
        Using new techniques
      </h2>
      <p className={`${styles.paragraph} max-w-[470px] mt-5`}>
        On top of popular trading strategies, make use of newly developed
        algorithms.
      </p>
    </div>

    <div className={layout.sectionImg}>
      <img src={novelalgo} alt="novelalgo" className="w-[100%] h-[100%]" />
    </div>
  </section>  
);

export default NewAlgos;
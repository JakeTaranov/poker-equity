import styles from "./Card.dimmed.module.css";

export default function CardDimmed(props) {
  const { suit, value } = props;
  return (
    <div className={styles.card}>
      <div className={styles.topLeft}>
        <div className={`${styles.value} ${styles[suit]}`}>{value}</div>
        <div className={`${styles.suit} ${styles[suit]}`} />
      </div>
      <div className={`${styles.centerSuitContainer}`}>
        <div className={`${styles.centerSuit} ${styles[suit]}`} />
      </div>
      <div className={styles.bottomRight}>
        <div className={`${styles.value} ${styles[suit]}`}>{value}</div>
        <div className={`${styles.suit} ${styles[suit]}`} />
      </div>
    </div>
  );
}

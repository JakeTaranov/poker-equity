import styles from "./Card.module.css";

export default function Card(props) {
    const { suit, value, isDimmed } = props;
    return (
        <div className={styles.card} style={{opacity: isDimmed ? 0.3 : 1}}>
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

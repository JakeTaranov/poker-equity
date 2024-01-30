import { motion } from "framer-motion";
import useSound from "use-sound";
import styles from "./Card.module.css";
import { useState } from "react";
import { CardProps } from "../../types/card";
import Card from "./Card";

export default function CardBack(props) {
    const { suit, value } = props;
    const [isFlipped, setIsFlipped] = useState(false);
    const [isAnimating, setIsAnimating] = useState(false);
    const [playCardFlipSound] = useSound("/sounds/flipCard.mp3", { volume: 0.8 });

    const handleFlip = () => {
        if (!isAnimating) {
            setIsFlipped(!isFlipped);
            setIsAnimating(true);
            // playCardFlipSound()
        }
    };

    return (
        <div className={styles.flipCardContainer} onClick={handleFlip}>
            <div className={styles.flipCard}>
                <motion.div
                    className={styles.flipCardInner}
                    initial={false}
                    animate={{ rotateY: isFlipped ? 180 : 360 }}
                    transition={{ duration: 0.6, animationDirection: "normal" }}
                    onAnimationComplete={() => setIsAnimating(false)}
                >
                    <div className={`${styles.cardback} ${styles.flipCardFront}`}>
                        <span>Blind Mans Bluff</span>
                    </div>
                    <div className={styles.flipCardBack}
                    >
                        <Card suit={suit} value={value} />
                    </div>
                </motion.div>
            </div>
        </div>
    );
}
import { useState, useEffect } from "react";
import "./App.css";
import Card from "./components/Card/Card";
import Graphs from "./components/Graphs/Graphs";
import { cards } from "./components/Card/cardList";
import { genereateOdds } from "./api";
import GridLoader from "react-spinners/GridLoader";

function App() {
  // Hand Cards
  const [h1Card1, setH1Card1] = useState({
    value: "",
    suit: "",
    rank: 0,
  });
  const [h1Card2, setH1Card2] = useState({
    value: "",
    suit: "",
    rank: 0,
  });
  const [h2Card1, setH2Card1] = useState({
    value: "",
    suit: "",
    rank: 0,
  });
  const [h2Card2, setH2Card2] = useState({
    value: "",
    suit: "",
    rank: 0,
  });
  // Board Cards
  const [b1Card, setB1Card] = useState({
    value: "",
    suit: "",
    rank: 0,
  });
  const [b2Card, setB2Card] = useState({
    value: "",
    suit: "",
    rank: 0,
  });
  const [b3Card, setB3Card] = useState({
    value: "",
    suit: "",
    rank: 0,
  });
  const [b4Card, setB4Card] = useState({
    value: "",
    suit: "",
    rank: 0,
  });
  const [b5Card, setB5Card] = useState({
    value: "",
    suit: "",
    rank: 0,
  });
  const [board, setBoard] = useState([]);
  const [selectedCard, setSelectedCard] = useState({
    value: "",
    suit: "",
    rank: 0,
  });
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(false);
  const [selectedCardsList, setSelectedCardsList] = useState([]);

  // Whenever h1 or h2 changes, we update the selected cards to dimm them
  useEffect(() => {
    // Update the list of cards selected
    const tempSelectedCardsList = [
      h1Card1,
      h1Card2,
      h2Card1,
      h2Card2,
      b1Card,
      b2Card,
      b3Card,
      b4Card,
      b5Card,
    ];
    const tempBoardList = [b1Card, b2Card, b3Card, b4Card, b5Card];
    setSelectedCardsList(tempSelectedCardsList);
    setBoard(tempBoardList);
  }, [
    h1Card1,
    h1Card2,
    h2Card1,
    h2Card2,
    b1Card,
    b2Card,
    b3Card,
    b4Card,
    b5Card,
  ]);

  const updateSelectedCard = (cardIndex) => {
    console.log(
      "You selected the " +
        cards[cardIndex].value +
        " of " +
        cards[cardIndex].suit
    );
    setSelectedCard({
      value: cards[cardIndex].value,
      suit: cards[cardIndex].suit,
      rank: cards[cardIndex].rank,
    });
  };

  const checkIfSelectedCardInBoardOrHand = (selected) => {
    if (
      JSON.stringify(selectedCard) === JSON.stringify(h1Card1) ||
      JSON.stringify(selectedCard) === JSON.stringify(h1Card2) ||
      JSON.stringify(selectedCard) === JSON.stringify(h2Card1) ||
      JSON.stringify(selectedCard) === JSON.stringify(h2Card2) ||
      JSON.stringify(selectedCard) === JSON.stringify(b1Card) ||
      JSON.stringify(selectedCard) === JSON.stringify(b2Card) ||
      JSON.stringify(selectedCard) === JSON.stringify(b3Card) ||
      JSON.stringify(selectedCard) === JSON.stringify(b4Card) ||
      JSON.stringify(selectedCard) === JSON.stringify(b5Card)
    ) {
      return true;
    }
    return false;
  };

  const updateCurrentSelectedPlayerCard = (selected) => {
    // Check to see if the card is already selected
    if (checkIfSelectedCardInBoardOrHand(selected)) {
      return;
    }

    if (selected == "h1c1") {
      setH1Card1({
        value: selectedCard.value,
        suit: selectedCard.suit,
        rank: selectedCard.rank,
      });
    } else if (selected == "h1c2") {
      setH1Card2({
        value: selectedCard.value,
        suit: selectedCard.suit,
        rank: selectedCard.rank,
      });
    } else if (selected == "h2c1") {
      setH2Card1({
        value: selectedCard.value,
        suit: selectedCard.suit,
        rank: selectedCard.rank,
      });
    } else if (selected == "h2c2") {
      setH2Card2({
        value: selectedCard.value,
        suit: selectedCard.suit,
        rank: selectedCard.rank,
      });
    } else if (selected == "b1") {
      setB1Card({
        value: selectedCard.value,
        suit: selectedCard.suit,
        rank: selectedCard.rank,
      });
    } else if (selected == "b2") {
      setB2Card({
        value: selectedCard.value,
        suit: selectedCard.suit,
        rank: selectedCard.rank,
      });
    } else if (selected == "b3") {
      setB3Card({
        value: selectedCard.value,
        suit: selectedCard.suit,
        rank: selectedCard.rank,
      });
    } else if (selected == "b4") {
      setB4Card({
        value: selectedCard.value,
        suit: selectedCard.suit,
        rank: selectedCard.rank,
      });
    } else if (selected == "b5") {
      setB5Card({
        value: selectedCard.value,
        suit: selectedCard.suit,
        rank: selectedCard.rank,
      });
    }
  };

  const clearAllCards = () => {
    const blank = {
        value: "",
        suit: "",
        rank: 0,
    }
    setH1Card1(blank);
    setH1Card2(blank);
    setH2Card1(blank);
    setH2Card2(blank);
    setB1Card(blank);
    setB2Card(blank);
    setB3Card(blank);
    setB4Card(blank);
    setB5Card(blank);
    setStats(null)

    // Will automatically clear selectedCardList and board from use effect
  }

  const hasValidPlayerCards = (bothHandCards) => {
    const hasEmptyHand = bothHandCards.some(
      (card) => card.value === "" && card.suit === "" && card.rank === 0
    );

    return hasEmptyHand;
  };

  const genereateOddsFromApi = async () => {
    // Ensure that the user has two cards selected for each hand
    if (hasValidPlayerCards([h1Card1, h1Card2, h2Card1, h2Card2])) {
      alert("You must select two cards per hand");
      return;
    }

    setLoading(true);
    var simulation_data = await genereateOdds(
      [h1Card1, h1Card2],
      [h2Card1, h2Card2],
      board
    );
    simulation_data = JSON.parse(simulation_data);
    setStats(simulation_data);
    setLoading(false);
  };

  const check_card_in_selected = (cardIndex) => {
    const obj_to_check = {
      value: cards[cardIndex].value,
      suit: cards[cardIndex].suit,
      rank: cards[cardIndex].rank,
    };

    const isInSelected = selectedCardsList.some(
      (card) =>
        card.value === obj_to_check.value &&
        card.suit === obj_to_check.suit &&
        card.rank === obj_to_check.rank
    );

    return isInSelected;
  };

  return (
    <>
      <div>
        <h1> Poker Simulator </h1>
        <div className="entireDisplayGrid">
          <div className="allCardsDisplayContainer">
            <div className="allCardsDisplay">
              {cards.map((card, index) => (
                <div>
                  <button
                    className="cardSelectButton"
                    onClick={() => updateSelectedCard(index)}
                  ></button>

                  <Card
                    suit={card.suit}
                    value={card.value}
                    isDimmed={check_card_in_selected(index)}
                  ></Card>
                </div>
              ))}
            </div>
          </div>

          <div className="playersHandContainer">
            <div>
              <p>Hand 1</p>
              <div className="playersHand">
                <button
                  className="cardSelectButton"
                  onClick={() => updateCurrentSelectedPlayerCard("h1c1")}
                ></button>
                <button
                  className="cardSelectButton"
                  onClick={() => updateCurrentSelectedPlayerCard("h1c2")}
                ></button>
                <Card suit={h1Card1.suit} value={h1Card1.value}></Card>
                <Card suit={h1Card2.suit} value={h1Card2.value}></Card>
              </div>
            </div>

            <div>
              <p> Board </p>
              <div className="boardCards">
                <button
                  className="cardSelectButton"
                  onClick={() => updateCurrentSelectedPlayerCard("b1")}
                ></button>
                <button
                  className="cardSelectButton"
                  onClick={() => updateCurrentSelectedPlayerCard("b2")}
                ></button>
                <button
                  className="cardSelectButton"
                  onClick={() => updateCurrentSelectedPlayerCard("b3")}
                ></button>
                <button
                  className="cardSelectButton"
                  onClick={() => updateCurrentSelectedPlayerCard("b4")}
                ></button>
                <button
                  className="cardSelectButton"
                  onClick={() => updateCurrentSelectedPlayerCard("b5")}
                ></button>
                <Card suit={b1Card.suit} value={b1Card.value}></Card>
                <Card suit={b2Card.suit} value={b2Card.value}></Card>
                <Card suit={b3Card.suit} value={b3Card.value}></Card>
                <Card suit={b4Card.suit} value={b4Card.value}></Card>
                <Card suit={b5Card.suit} value={b5Card.value}></Card>
              </div>
            </div>

            <div>
              <p>Hand 2</p>
              <div className="playersHand">
                <button
                  className="cardSelectButton"
                  onClick={() => updateCurrentSelectedPlayerCard("h2c1")}
                ></button>
                <button
                  className="cardSelectButton"
                  onClick={() => updateCurrentSelectedPlayerCard("h2c2")}
                ></button>
                <Card suit={h2Card1.suit} value={h2Card1.value}></Card>
                <Card suit={h2Card2.suit} value={h2Card2.value}></Card>
              </div>
            </div>
          </div>
        </div>

        <button className="generalButton" onClick={() => genereateOddsFromApi()}>GENERATE ODDS</button>
        <button className="generalButton" onClick={() => clearAllCards()}>CLEAR</button>

        <div className="loadingIcon">
          {loading && (
            <GridLoader color={"#0C855B"} loading={loading} size={25} />
          )}
        </div>
        <div>{stats && !loading && <Graphs stats={stats}></Graphs>}</div>
      </div>
    </>
  );
}

export default App;

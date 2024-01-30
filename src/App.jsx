import { useState, useEffect } from "react";
import "./App.css";
import Card from "./components/Card/Card";
import CardDimmed from "./components/Card/CardDimmed";

import { cards } from "./components/Card/cardList";
import { genereateOdds } from "./api";
import { Chart as ChartJS } from "chart.js/auto";
import { Bar, Pie } from "react-chartjs-2";
import GridLoader from "react-spinners/GridLoader";

function App() {
  const [h1Card1, setH1Card1] = useState({
    value: null,
    suit: null,
    rank: null,
  });
  const [h1Card2, setH1Card2] = useState({
    value: null,
    suit: null,
    rank: null,
    rank: null,
  });
  const [h2Card1, setH2Card1] = useState({
    value: null,
    suit: null,
    rank: null,
  });
  const [h2Card2, setH2Card2] = useState({
    value: null,
    suit: null,
    rank: null,
  });
  const [selectedCard, setSelectedCard] = useState({
    value: null,
    suit: null,
    rank: null,
  });
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(false);
  const [selectedCardsList, setSelectedCardsList] = useState([]);

  const alpha = 0.7;

  const pie_chart_colors = [
    `rgb(189, 195, 199, ${alpha})`,
    `rgb(127, 140, 141, ${alpha})`,
    `rgb(46, 64, 83, ${alpha})`,
    `rgb(211, 84, 0, ${alpha})`,
    `rgb(241, 196, 15, ${alpha})`,
    `rgb(46, 204, 113, ${alpha})`,
    `rgb(72, 201, 176, ${alpha})`,
    `rgb(52, 152, 219, ${alpha})`,
    `rgb(175, 122, 197, ${alpha})`,
    `rgb(236, 112, 99, ${alpha})`,
  ];

  const bar_colors = ["#008000", "#0000FF", "#FF0000"];
  
  // Whenever h1 or h2 changes, we update the selected cards to dimm them
  useEffect(() => {
    // Update the list of cards selected
    const tempSelectedCardsList = [h1Card1, h1Card2, h2Card1, h2Card2];
    setSelectedCardsList(tempSelectedCardsList);
    console.log(selectedCardsList);
  }, [h1Card1, h1Card2, h2Card1, h2Card2]);

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

  const updateCurrentSelectedPlayerCard = (selected) => {
    // Check to see if the card is already selected

    if (
      JSON.stringify(selectedCard) === JSON.stringify(h1Card1) ||
      JSON.stringify(selectedCard) === JSON.stringify(h1Card2) ||
      JSON.stringify(selectedCard) === JSON.stringify(h2Card1) ||
      JSON.stringify(selectedCard) === JSON.stringify(h2Card2)
    ) {
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
    } else {
      setH2Card2({
        value: selectedCard.value,
        suit: selectedCard.suit,
        rank: selectedCard.rank,
      });
    }
  };

  const genereateOddsFromApi = async () => {
    setLoading(true);
    var simulation_data = await genereateOdds(
      h1Card1,
      h1Card2,
      h2Card1,
      h2Card2
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
        <div className="entireDisplayGrid">
          <div className="allCardsDisplayContainer">
            <div className="allCardsDisplay">
              {cards.map((card, index) => (
                <div>
                  <button
                    className="cardSelectButton"
                    onClick={() => updateSelectedCard(index)}
                  ></button>

                  {check_card_in_selected(index) ? (
                    <CardDimmed
                      suit={card.suit}
                      value={card.value}
                    ></CardDimmed>
                  ) : (
                    <Card suit={card.suit} value={card.value}></Card>
                  )}
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

        <button onClick={() => genereateOddsFromApi()}>GENERATE ODDS</button>
        <div className="loadingIcon">
          {loading && (
            <GridLoader color={"#023020"} loading={loading} size={25} />
          )}
        </div>
        <div>
          {stats && !loading && (
            <>
              <div className="barContainer">
                <Bar
                  options={{
                    plugins: {
                      title: {
                        display: true,
                        text: "Win / Split Percentages",
                        color: "#FFFFFF",
                      },
                      legend: {
                        display: false,
                      },
                    },
                  }}
                  data={{
                    labels: ["Split", "Hand 1", "Hand 2"],
                    datasets: [
                      {
                        label: ["Wins / Splits"],
                        data: [
                          parseFloat(stats["split_percentage"]).toFixed(2),
                          parseFloat(stats["hand_1_win_percentage"]).toFixed(2),
                          parseFloat(stats["hand_2_win_percentage"]).toFixed(2),
                        ],
                        borderRadius: 30,
                        backgroundColor: bar_colors,
                      },
                    ],
                  }}
                />
              </div>
              <div className="pieContainerGrid">
                <div className="pieContainerHand1">
                  <Pie
                    options={{
                      plugins: {
                        title: {
                          display: true,
                          text: "Hand 1 Wins",
                          color: "#FFFFFF",
                        },
                      },
                    }}
                    data={{
                      labels: [
                        "Royal Flush",
                        "Straight Flush",
                        "Four of a Kind",
                        "Full House",
                        "Flush",
                        "Straight",
                        "Three of A Kind",
                        "Two Pair",
                        "Pair",
                        "High Card",
                      ],
                      datasets: [
                        {
                          label: "Hand 1",
                          data: [
                            parseFloat(
                              stats["hand_1_win_percentage_types"][
                                "royal_flush"
                              ]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_1_win_percentage_types"][
                                "straight_flush"
                              ]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_1_win_percentage_types"][
                                "four_of_a_kind"
                              ]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_1_win_percentage_types"]["full_house"]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_1_win_percentage_types"]["flush"]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_1_win_percentage_types"]["straight"]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_1_win_percentage_types"][
                                "three_of_a_kind"
                              ]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_1_win_percentage_types"]["two_pair"]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_1_win_percentage_types"]["pair"]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_1_win_percentage_types"]["high"]
                            ).toFixed(2),
                          ],
                          borderRadius: 5,
                          backgroundColor: pie_chart_colors,
                        },
                      ],
                    }}
                  />
                </div>

                <div className="pieContainerHand2">
                  <Pie
                    options={{
                      plugins: {
                        title: {
                          display: true,
                          text: "Hand 2 Wins",
                          color: "#FFFFFF",
                        },
                      },
                    }}
                    data={{
                      labels: [
                        "Royal Flush",
                        "Straight Flush",
                        "Four of a Kind",
                        "Full House",
                        "Flush",
                        "Straight",
                        "Three of A Kind",
                        "Two Pair",
                        "Pair",
                        "High Card",
                      ],
                      datasets: [
                        {
                          label: "Hand 2",
                          data: [
                            parseFloat(
                              stats["hand_2_win_percentage_types"][
                                "royal_flush"
                              ]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_2_win_percentage_types"][
                                "straight_flush"
                              ]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_2_win_percentage_types"][
                                "four_of_a_kind"
                              ]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_2_win_percentage_types"]["full_house"]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_2_win_percentage_types"]["flush"]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_2_win_percentage_types"]["straight"]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_2_win_percentage_types"][
                                "three_of_a_kind"
                              ]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_2_win_percentage_types"]["two_pair"]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_2_win_percentage_types"]["pair"]
                            ).toFixed(2),
                            parseFloat(
                              stats["hand_2_win_percentage_types"]["high"]
                            ).toFixed(2),
                          ],
                          borderRadius: 5,
                          backgroundColor: pie_chart_colors,
                        },
                      ],
                    }}
                  />
                </div>
              </div>
            </>
          )}
        </div>
      </div>
    </>
  );
}

export default App;

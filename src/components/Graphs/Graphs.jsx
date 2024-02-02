// import styles from "./Graphs.module.css";
import "./graphs.css";
import { Chart as ChartJS } from "chart.js/auto";
import { Bar, Pie } from "react-chartjs-2";

export default function Graphs(props) {
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

  const stats = props["stats"];

  return (
    <div>
      <div className="chartsContainer">
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
                labels: {
                  fontColor: "#FFFFFF",
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
                        stats["hand_1_win_percentage_types"]["royal_flush"]
                      ).toFixed(2),
                      parseFloat(
                        stats["hand_1_win_percentage_types"]["straight_flush"]
                      ).toFixed(2),
                      parseFloat(
                        stats["hand_1_win_percentage_types"]["four_of_a_kind"]
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
                        stats["hand_1_win_percentage_types"]["three_of_a_kind"]
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
                        stats["hand_2_win_percentage_types"]["royal_flush"]
                      ).toFixed(2),
                      parseFloat(
                        stats["hand_2_win_percentage_types"]["straight_flush"]
                      ).toFixed(2),
                      parseFloat(
                        stats["hand_2_win_percentage_types"]["four_of_a_kind"]
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
                        stats["hand_2_win_percentage_types"]["three_of_a_kind"]
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
      </div>
    </div>
  );
}

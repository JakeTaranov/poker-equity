# Texas Holdem Odds Calculator via Monte Carlo Simulation

## Overview
The application is designed to predict the outcomes of poker hands using a Monte Carlo Simulation, a statistical method known for its accuracy in predicting complex outcomes. With this tool, users can input specific cards for each player and, optionally, community cards (flop, turn, and river) to simulate various poker scenarios.

The simulation runs 100,000 iterations, providing statistically signifigant results for the context of predicting the probabilities of different hands winning under given conditions.

## Technologies Used
<ul>
  <li> React + Javscript </li>
    <ul>
      <li> The front end application, which allows for user input </li>
    </ul>
  <li> Python </li>
    <ul>
      <li> Responsible for the server side actions, along with running the simulation </li>
    </ul>
  <li> FastAPI </li>
    <ul>
      <li> Allowing for requests between the front end and server </li>
    </ul>
  <li >MongoDB </li>
    <ul>
      <li> Caching previously ran simulations to reduce response times </li>
    </ul>
</ul>


https://github.com/JakeTaranov/poker-equity/assets/48743548/52454253-7e9f-495a-a871-db6a9f43963f


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from Simulator import Simulator
import pprint
import json

class HandItem(BaseModel):
    rank: int
    value: str
    suit: str

class HandRequest(BaseModel):
    hand_1: List[HandItem]
    hand_2: List[HandItem]



app = FastAPI()

origins = [
    "http://localhost:5173/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with the actual origin of your front-end app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def format_player_cards(cards):
    formatted_cards = []
    for card in cards:
        formatted_cards.append((card.rank, card.suit))

    return formatted_cards
@app.get("/")
async def root():
    return {"message": "TEST FROM FAST API"} 


@app.post("/evaluate_hands")
def evalute_hands(hands: HandRequest):
    hand_1_formatted = format_player_cards(hands.hand_1)
    hand_2_formatted = format_player_cards(hands.hand_2)
    
    n = 100000
    print(hand_1_formatted, hand_2_formatted)
    simulator = Simulator(n, hand_1_formatted, hand_2_formatted, False)
    simulator_data = simulator.simulate()
    
    pprint.pprint(simulator_data)
    print("Hand 1 wins:", simulator_data["wins_splits"][1]/n * 100)
    print("Hand 2 wins:", simulator_data["wins_splits"][2]/n * 100)
    print("Splits:", simulator_data["wins_splits"][3]/n * 100)
   # response_data = {"message": "Received hands %s %s" % (hands.hand_1[0].value, hands.hand_2)}
    return {"data": json.dumps(simulator_data)}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from pydantic import BaseModel
from pymongo.mongo_client import MongoClient
from Simulator import Simulator
import certifi
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

ca = certifi.where()

uri = "mongodb+srv://taranovjake99:qhLl1FyUHzr9gpJr@poker-equity.4dx6cky.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=ca)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
    
simulation_data = {
        "wins_splits": {},
        "hand_1_win_types": {
            "royal_flush": 0,
            "straight_flush": 0,
            "full_house": 0,
            "flush": 0,
            "straight": 0,
            "three_of_a_kind": 0,
            "two_pair": 0,
            "pair": 0,
            "high": 0,
            },
        "hand_2_win_types": {
            "royal_flush": 0,
            "straight_flush": 0,
            "full_house": 0,
            "flush": 0,
            "straight": 0,
            "three_of_a_kind": 0,
            "two_pair": 0,
            "pair": 0,
            "high": 0,
            },
        "split_types": {
            "royal_flush": 0,
            "straight_flush": 0,
            "full_house": 0,
            "flush": 0,
            "straight": 0,
            "three_of_a_kind": 0,
            "two_pair": 0,
            "pair": 0,
            "high": 0,
            },
        "hand_1_win_percentage_types": {},
        "hand_2_win_percentage_types": {},
        "split_percentage_types": {},
}

simulation_stats_validator = {
    "bsonType": "object",
    "required": ["hand_1_win_percentage", "hand_2_win_percentage", "split_percentage", "hand_1_win_percentage_types", "hand_2_win_percentage_types", "split_percentage_types"],
    "properties" : {
        "hand_1_win_percentage" : {
            "bsonType": "float",
            "description": "must be a float and is required"
        },
        "hand_2_win_percentage" : {
            "bsonType": "float",
            "description": "must be a float and is required"
        },
        "split_percentage" : {
            "bsonType": "float",
            "description": "must be a float and is required"
        },
        "hand_1_win_percentage_types" : {
            "bsonType": "object",
            "required": ["royal_flush", "straight_flush", "full_house", "flush", "straight", "three_of_a_kind", "two_pair", "pair", "high"],
            "properties" : {
                "royal_flush" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "straight_flush" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "full_house" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "flush" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "straight" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "three_of_a_kind" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "two_pair" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "pair" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "high" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                }
            }  
        },
        
        "hand_2_win_percentage_types" : {
            "bsonType": "object",
            "required": ["royal_flush", "straight_flush", "full_house", "flush", "straight", "three_of_a_kind", "two_pair", "pair", "high"],
            "properties" : {
                "royal_flush" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "straight_flush" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "full_house" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "flush" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "straight" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "three_of_a_kind" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "two_pair" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "pair" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "high" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                }
            }
        }, 
        "split_percentage_types" : {
            "bsonType": "object",
            "required": ["royal_flush", "straight_flush", "full_house", "flush", "straight", "three_of_a_kind", "two_pair", "pair", "high"],
            "properties" : {
                "royal_flush" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "straight_flush" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "full_house" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "flush" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "straight" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "three_of_a_kind" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "two_pair" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "pair" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                },
                "high" : {
                    "bsonType": "float",
                    "description": "must be a float and is required"
                }
            }
            
        }
    }
}
    





    
    
    
    
    
origins = [
    "http://localhost:5173/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Replace with the actual origin of your front-end app
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


# @app.post("/evaluate_hands")
# def evalute_hands(hands: HandRequest):
#     hand_1_formatted = format_player_cards(hands.hand_1)
#     hand_2_formatted = format_player_cards(hands.hand_2)
    
#     n = 100000
#     print(hand_1_formatted, hand_2_formatted)
#     simulator = Simulator(n, hand_1_formatted, hand_2_formatted, False)
#     simulator_data = simulator.simulate()
    
#     pprint.pprint(simulator_data)
#     print("Hand 1 wins:", simulator_data["wins_splits"][1]/n * 100)
#     print("Hand 2 wins:", simulator_data["wins_splits"][2]/n * 100)
#     print("Splits:", simulator_data["wins_splits"][3]/n * 100)
#    # response_data = {"message": "Received hands %s %s" % (hands.hand_1[0].value, hands.hand_2)}
#     return {"data": json.dumps(simulator_data)}
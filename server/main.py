from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from pydantic import BaseModel
from pymongo.mongo_client import MongoClient
from Simulator import Simulator
import certifi
import pprint
import json
from bson import ObjectId

    
class CardItem(BaseModel):
    rank: int 
    value: str
    suit: str

class HandRequest(BaseModel):
    hand_1: List[CardItem]
    hand_2: List[CardItem]
    board: List[CardItem]


app = FastAPI()

ca = certifi.where()

#db_password = os.environ["MONGO_DB_PE_PASS"]
#print("DB pass", db_password)
uri = f"mongodb+srv://taranovjake99:qhLl1FyUHzr9gpJr@poker-equity.4dx6cky.mongodb.net/?retryWrites=true&w=majority&authSource=admin"
# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=ca)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    

dbs = client.list_database_names()
db = client["test"]
collection = db["sim_stats_test"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with the actual origin of your front-end app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def format_player_and_board_cards(cards):
    formatted_cards = []
    for card in cards:
        formatted_cards.append((card.rank, card.suit))

    return formatted_cards


@app.get("/")
async def root():
    return {"message": "TEST FROM FAST API"} 

        
def create_id(hands_and_board):
    hands_string = ""
    suit_str = ""
    for hand in hands_and_board:
        for card in hand:
            # if empty suit we assing 'e'
            if card.suit == "":
                suit_str = 'e'
            else:
                suit_str = card.suit[0]
            hands_string += ''.join(sorted(str(suit_str) + card.value))
            
    return hands_string


def check_if_already_exists_in_database(id):
    does_exist = collection.find_one({"_id": id})
    return does_exist
    
    
def insert_in_database(simulation_data):
    try:
        collection.insert_one(simulation_data)
        print("Inserted ", id, "into database")
    except Exception as e:
        print("ERROR INSERTING INTO DATABASE",e) 
    
def clear_database():
    collection.delete_many({})


# returns the board if it is not empty, otherwise returns None
def check_board_is_empty(board):
    for card in board:
        if card != (0, ""):
            return board

    return None
    

@app.post("/evaluate_hands")
def evalute_hands(hands: HandRequest):
    hand_1_formatted = format_player_and_board_cards(hands.hand_1)
    hand_2_formatted = format_player_and_board_cards(hands.hand_2)
    print(hands.board)
    board_formatted = format_player_and_board_cards(hands.board)
  #  print(hand_1_formatted)
    
    # clear_database()
    # return
    
    # check to see if we have already computed the hand, if so we can return it immediatley 
    # NOTE: FIX ID SO IT WORKS WITH FLOPS +
    
    id = create_id([hands.hand_1, hands.hand_2, hands.board])
    
    
    is_in_database = check_if_already_exists_in_database(id)
    
    if is_in_database:
        print("data found in db")
       # pprint.pprint(is_in_database)
        pprint.pprint(is_in_database)
        return {"data": json.dumps(is_in_database)}
    print("data not found in db")    
    
    n = 100000
   # print(hand_1_formatted, hand_2_formatted)
    
    # None if empty
    board = check_board_is_empty(board_formatted)
    
    simulator = Simulator(n, hand_1_formatted, hand_2_formatted, False, board=board)
    simulator_data = simulator.simulate()
    
    # if we are here then the data does not already exists in the database so we want to insert it
    # specify the id
    simulator_data["_id"] = id
    insert_in_database(simulator_data)
    
    pprint.pprint(simulator_data)
    print("Hand 1 wins:", simulator_data["wins_splits"]["1"]/n * 100)
    print("Hand 2 wins:", simulator_data["wins_splits"]["2"]/n * 100)
    print("Splits:", simulator_data["wins_splits"]["3"]/n * 100)
   # response_data = {"message": "Received hands %s %s" % (hands.hand_1[0].value, hands.hand_2)}
    return {"data": json.dumps(simulator_data)}















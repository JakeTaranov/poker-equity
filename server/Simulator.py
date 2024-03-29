from HandChecker import HandChecker
from cards import cards as deck
import random
import pprint
import random
import os

# simualte hand_1 and hand_2 on the respected board 
class Simulator:
    def __init__(self, iterations, hand_1, hand_2, debug, board=None):
        self.iterations = iterations
        self.hand_1 = hand_1
        self.hand_2 = hand_2
        self.debug = debug
        self.board = board
        
    
    @staticmethod 
    def create_board_of_five(deck, hand_1, hand_2):
        # creating random indexs to pull from deck
        
        random_idxs = random.sample(range(52), 51)
        board = []
        added = 0
        for idx in random_idxs:
            
            cur_card = ((deck[idx]["rank"], deck[idx]["suit"]))
            if cur_card == hand_1[0] or cur_card == hand_1[1] or cur_card == hand_2[0] or cur_card == hand_2[1]:
                continue
            
            elif added == 5:
                break
            
            board.append(cur_card)
            added += 1
            
        return board
    
    @staticmethod 
    def create_board_of_n(deck, hand_1, hand_2, existing_board):
        
        cards_to_make = existing_board.count((0, ""))
        
        random_idxs = random.sample(range(52), 51)

        added = 0
        
        rest_of_board = []
        
        for idx in random_idxs:
            
            cur_card = ((deck[idx]["rank"], deck[idx]["suit"]))
            # make sure we are not using the same card twice
            if cur_card == hand_1[0] or cur_card == hand_1[1] or cur_card == hand_2[0] or cur_card == hand_2[1] or cur_card == existing_board[0] or cur_card == existing_board[1] or cur_card == existing_board[2] or cur_card == existing_board[3] or cur_card == existing_board[4]:
                continue
            
            elif added == cards_to_make:
                break
            
            rest_of_board.append(cur_card)
            added += 1
        

        existing_board = existing_board + rest_of_board

        # removing the (0, "") entires
        for _ in range(cards_to_make): 
            existing_board.remove((0, ""))
            
     #   print("BOARD MADE", existing_board)
        return existing_board
        
            
        
    @staticmethod
    def create_board(deck, hand_1, hand_2, existing_board=None):
            
        if not existing_board:
            return Simulator.create_board_of_five(deck, hand_1, hand_2)
            # We want to make a board of 5
        else:
            return Simulator.create_board_of_n(deck, hand_1, hand_2, existing_board)
            # we want to make a board to fill up the reamining card spots left on the board
            

        
    
    
    @staticmethod
    def check_generic_winner(hand_1_strength, hand_2_strength):
        # check if hand 1 wins
        if hand_1_strength > hand_2_strength:
            return 1
        # check if hand 2 wins
        elif hand_2_strength > hand_1_strength:
            return 2
        # check if there is a draw
        elif hand_1_strength == hand_2_strength and hand_1_strength != 0 and hand_2_strength != 0: 
            return 3
        # no hand was made
        else:
            return 0
        
        
    @staticmethod
    def check_two_pair_winner(hand_1_strength, hand_2_strength, hand_1, hand_2, board):
        
        # checking the basic cases here, if one hand has a two pair and the other doesnt 
        
        # If no two pair is found in either hand
        if not hand_1_strength and not hand_2_strength:
            return 0
        # check if hand 1 wins
        elif not hand_2_strength and hand_1_strength:
            return 1
        # check if hand 1 wins 
        elif not hand_1_strength and hand_2_strength:
            return 2
        
        # if both the hands have two pair we check to see which has the higher pair
        
        # if hand 1 has the higher pair
        if hand_1_strength[0] > hand_2_strength[0]:
            return 1
        # if hand 2 has the higher pair
        elif hand_2_strength[0] > hand_1_strength[0]:
            return 2        
        else:
            # if both the top pairs are equal we check the second pair
            if hand_1_strength[1] > hand_2_strength[1]:
                return 1
            elif hand_2_strength[1] > hand_1_strength[1]:
                return 2
            else:
                # If both the top pair and second pair are equal we find the highest card on the board and the players hand
                hand_1_max_kicker = max([rank for rank, _ in hand_1])
                hand_2_max_kicker = max([rank for rank, _ in hand_2])
                
                # We must find the value of the last card in the board
                board_rank_count = {}
                for rank, _ in board:
                    board_rank_count[rank] = board_rank_count.get(rank, 0) + 1
             #   print(board_rank_count)
             
                unique_in_board = max([rank for rank, count in board_rank_count.items() if count == 1])
                
                # If the remaning card in the board is higher than the max in hand 1 and hand 2, then it is a split
                if unique_in_board > hand_1_max_kicker and unique_in_board > hand_2_max_kicker:
                    return 3
                elif hand_1_max_kicker > hand_2_max_kicker:
                    return 1
                elif hand_2_max_kicker > hand_1_max_kicker:
                    # if we are here hand two must have the highest kicker
                    return 2
                else:
                    # if the both player card kickers are higher than what is on the board and they are equal its a tie
                    return 3
                        
    @staticmethod
    def check_pair_winner(hand_1_strength, hand_2_strength, hand_1, hand_2, board):
        if not hand_1_strength and not hand_2_strength:
            return 0
        elif not hand_2_strength and hand_1_strength:
            return 1
        elif not hand_1_strength and hand_2_strength:
            return 2
        
        if hand_1_strength > hand_2_strength:
            return 1   
        elif hand_2_strength > hand_1_strength:
            return 2
        else:
            # if pairs are equal we check the highest reamining 3 cards in the hands and board
            
            
            # we know here hand_1_strength = hand_2_strength so we can use either 
            hand_1_ranks = [rank for rank, _ in hand_1 if rank != hand_1_strength]
            hand_2_ranks = [rank for rank, _ in hand_2 if rank != hand_1_strength]
            
            # # We must find the values of the 3 remaiing cards on the board
            board_rank_count = {}
            for rank, _ in board:
                board_rank_count[rank] = board_rank_count.get(rank, 0) + 1
            unique_in_board = [rank for rank, count in board_rank_count.items() if count == 1 and rank != hand_1_strength]
            
            top_hand_1 = sorted(hand_1_ranks+unique_in_board, reverse=True)[:3]
            top_hand_2 = sorted(hand_2_ranks+unique_in_board, reverse=True)[:3]            
            return Simulator.check_high_card_winner(top_hand_1, top_hand_2)
            
            
    @staticmethod 
    def check_high_card_winner(hand_1_strength, hand_2_strength):
        for h1, h2, in zip(hand_1_strength, hand_2_strength):
            if h1 > h2:
                return 1
            elif h2 > h1:
                return 2
            else:
                continue
        return 3
    
            
    
    @staticmethod
    def log(winner, hand_1, hand_2, board, how):
        
        string_winner = ""
        if winner == 1:
            string_winner = "Hand 1"
        elif winner == 2:
            string_winner = "Hand 2"
        else:
            string_winner = "Split"
            
        print("\n Winner:", string_winner, "\n With:", how ,"\n Hand 1:", hand_1, "\n Hand 2:", hand_2, "\n Board:", board, '\n')        
    
    
    # Returns the winner of the hand
    # 1 = hand_1
    # 2 = hand_2
    # 3 = tie
            
    def simulate_hand(self, board):
            hand_1_check = HandChecker(self.hand_1, board)
            hand_2_check = HandChecker(self.hand_2, board)
            
            
                          
            hand_1_royal_flush = hand_1_check.royal_flush()
            hand_2_royal_flush = hand_2_check.royal_flush()
            winner = self.check_generic_winner(hand_1_royal_flush, hand_2_royal_flush)
            if winner:
                # write logs
                if self.debug:
                    self.log(winner, self.hand_1, self.hand_2, board, "Royal Flush")
                return str(winner), "royal_flush"
            
            

            hand_1_straight_flush = hand_1_check.straight_flush()
            hand_2_straight_flush = hand_2_check.straight_flush()
            winner = self.check_generic_winner(hand_1_straight_flush, hand_2_straight_flush)
            if winner:
                # write logs
                if self.debug:
                    self.log(winner, self.hand_1, self.hand_2, board, "Straight Flush")
                return str(winner), "straight_flush"
            
            
            
            hand_1_four_of_a_kind = hand_1_check.four_of_a_kind()
            hand_2_four_of_a_kind = hand_2_check.four_of_a_kind()
            winner = self.check_generic_winner(hand_1_four_of_a_kind, hand_2_four_of_a_kind)
            if winner:
                # write logs
                if self.debug:
                    self.log(winner, self.hand_1, self.hand_2, board, "Four of a Kind")
                return str(winner), "four_of_a_kind"
            
            
            
            hand_1_full_house = hand_1_check.full_house()
            hand_2_full_house = hand_2_check.full_house()
            winner = self.check_generic_winner(hand_1_full_house, hand_2_full_house)
            if winner:
                # write logs
                if self.debug:
                    self.log(winner, self.hand_1, self.hand_2, board, "Full House")
                return str(winner), "full_house"
            
            
            
            hand_1_flush = hand_1_check.flush()
            hand_2_flush = hand_2_check.flush()
            winner = self.check_generic_winner(hand_1_flush, hand_2_flush)
            if winner:
                # write logs
                if self.debug:
                    self.log(winner, self.hand_1, self.hand_2, board, "Flush")
                return str(winner), "flush"
            
            
            
            hand_1_straight = hand_1_check.straight()
            hand_2_straight = hand_2_check.straight()
            winner = self.check_generic_winner(hand_1_straight, hand_2_straight)
            if winner:
                # write logs
                if self.debug:
                    self.log(winner, self.hand_1, self.hand_2, board, "Straight")
                return str(winner), "straight"
            
            
            
            hand_1_three_of_a_kind = hand_1_check.three_of_a_kind()
            hand_2_three_of_a_kind = hand_2_check.three_of_a_kind()
            winner = self.check_generic_winner(hand_1_three_of_a_kind, hand_2_three_of_a_kind)
            if winner:
                # write logs
                if self.debug:
                    self.log(winner, self.hand_1, self.hand_2, board, "Three of a Kind")
                return str(winner), "three_of_a_kind"
            
            
            
            hand_1_two_pair = hand_1_check.two_pair()
            hand_2_two_pair = hand_2_check.two_pair()
            winner = self.check_two_pair_winner(hand_1_two_pair, hand_2_two_pair, self.hand_1, self.hand_2, board)
            if winner:
                # write logs
                if self.debug:
                    self.log(winner, self.hand_1, self.hand_2, board, "Two Pair")
                return str(winner), "two_pair" 
            
                   
            
            hand_1_pair= hand_1_check.pair()
            hand_2_pair = hand_2_check.pair()  
            winner = self.check_pair_winner(hand_1_pair, hand_2_pair, self.hand_1, self.hand_2, board)
            if winner:
                # write logs
                if self.debug:
                    self.log(winner, self.hand_1, self.hand_2, board, "Pair")
                return str(winner), "pair"
            
              
            
            hand_1_high_card = hand_1_check.high_card()         
            hand_2_high_card = hand_2_check.high_card() 
            winner = self.check_generic_winner(hand_1_high_card, hand_2_high_card)
            
            if winner:
                # write logs
                if self.debug:
                    self.log(winner, self.hand_1, self.hand_2, board, "High Card")
                return str(winner), "high"
            
    @staticmethod
    def create_percentages(simulation_data, n):        
        simulation_data["hand_1_win_percentage"] = simulation_data["wins_splits"]["1"] / n * 100
        simulation_data["hand_2_win_percentage"] = simulation_data["wins_splits"]["2"] / n * 100
        simulation_data["split_percentage"] = simulation_data["wins_splits"]["3"] / n * 100        
        
        for win_type, wins in simulation_data["hand_1_win_types"].items():
            simulation_data["hand_1_win_percentage_types"][win_type] = wins / n * 100
        
        for win_type, wins in simulation_data["hand_2_win_types"].items():
            simulation_data["hand_2_win_percentage_types"][win_type] = wins / n * 100
        
        for win_type, wins in simulation_data["split_types"].items():
            simulation_data["split_percentage_types"][win_type] = wins / n * 100
        
        
            
        return simulation_data

        
                
    def simulate(self):    
        
        simulation_data = {
            "wins_splits": {
                "1": 0,
                "2": 0,
                "3": 0
                },
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

        for i in range(self.iterations):
            #random.seed(os.urandom(16))
            #shuffle the deck
            random.shuffle(deck)
            # if we pass in out own board, for when there is a flop etc. Create the remaining cards for the board if the user passed one in
            if self.board:
                #print("HERE")
                board = self.create_board(deck, self.hand_1, self.hand_2, self.board)

            else:
                #create the 5 card playing board without the board passed by user
                board = self.create_board(deck, self.hand_1, self.hand_2)
            
            winner, how = self.simulate_hand(board)
                    
            simulation_data["wins_splits"][winner] = simulation_data["wins_splits"].get(winner, 0) + 1
            
            if winner == "1":
                simulation_data["hand_1_win_types"][how] = simulation_data["hand_1_win_types"].get(how, 0) + 1    
            elif winner == "2":
                simulation_data["hand_2_win_types"][how] = simulation_data["hand_2_win_types"].get(how, 0) + 1 
            else:
                simulation_data["split_types"][how] = simulation_data["split_types"].get(how, 0) + 1 

        return self.create_percentages(simulation_data, self.iterations)
            
            
            
            
            
            
            
            
            
def fast_test():
    # h1c1 = { "suit": "club", "value": "Q", "rank": 6, "isPlayable": True }
    # h1c2 = { "suit": "spade", "value": "Q", "rank": 5, "isPlayable": True }
    # h1 = [(h1c1["rank"], h1c1["suit"]), (h1c2["rank"], h1c2["suit"])]


    # h2c1 = { "suit": "heart", "value": "Q", "rank": 12, "isPlayable": True }
    # h2c2 = { "suit": "spade", "value": "Q", "rank": 13, "isPlayable": True }
    # h2 = [(h2c1["rank"], h2c1["suit"]), (h2c2["rank"], h2c2["suit"])]

    # board_raw = [
    #     { "suit": "spade", "value": "Q", "rank": 11, "isPlayable": True },
    #     { "suit": "club", "value": "Q", "rank": 10, "isPlayable": True },
    #     { "suit": "diamond", "value": "Q", "rank": 11, "isPlayable": True },
    #     { "suit": "diamond", "value": "Q", "rank": 10, "isPlayable": True },
    #     { "suit": "heart", "value": "Q", "rank": 9, "isPlayable": True },
    # ]

    # board = [(11, "heart"), (10, "spade"), (9, "spade"), (0, ""), (0, "")]
    
    
    h1 = [(11, 'diamond'), (5, 'club')]
    h2 = [(10, 'club'), (5, 'club')]
    board = [(5, 'spade'), (7, 'club'), (8, 'spade'), (12, 'club'), (12, 'diamond')]



    n = 1
    s = Simulator(n, h1, h2, False, board=board)
    data = s.simulate()


    pprint.pprint(data)

    print("Hand 1 wins:", data["wins_splits"]["1"]/n * 100)
    print("Hand 2 wins:", data["wins_splits"]["2"]/n * 100)
    print("Splits:", data["wins_splits"]["3"]/n * 100)


#fast_test()

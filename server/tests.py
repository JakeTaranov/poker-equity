import unittest
from Simulator import Simulator
from HandChecker import HandChecker

class TestHandChecker(unittest.TestCase):
    
    
    def test_royal_flush_draw(self):
        # royal flush on the board
        board = [(10, "diamond"), (11, 'diamond'), (12, 'diamond'), (13, 'diamond'), (14, 'diamond')]
        hand_1 = [(12, "club"),(13, "club")]
        hand_2 = [(12, "heart"),(13, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.royal_flush()
        hand_2_res = hand_2_checker.royal_flush()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)        
        self.assertEqual(res, 3)
        
    def test_royal_flush_winner(self):
        # hand 1 wins by royal flush
        board = [(10, "club"), (11, 'club'), (2, 'spade'), (3, 'diamond'), (14, 'club')]
        hand_1 = [(12, "club"),(13, "club")]
        hand_2 = [(12, "heart"),(13, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.royal_flush()
        hand_2_res = hand_2_checker.royal_flush()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)        
        self.assertEqual(res, 1)
        
    def test_straight_flush_draw(self):
        # straight glush on the board
        board = [(2, "spade"), (3, 'spade'), (4, 'spade'), (5, 'spade'), (6, 'spade')]
        hand_1 = [(12, "club"),(13, "club")]
        hand_2 = [(6, "heart"),(2, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.straight_flush()
        hand_2_res = hand_2_checker.straight_flush()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 3)      
        
    def test_straight_flush_winner(self):
        # hand 1 should win
        board = [(2, "spade"), (3, 'spade'), (4, 'spade'), (11, 'club'), (6, 'club')]
        hand_1 = [(5, "spade"),(6, "spade")]
        hand_2 = [(6, "heart"),(2, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.straight_flush()
        hand_2_res = hand_2_checker.straight_flush()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1)    
        
    def test_four_of_a_kind_win_from_kicker(self):
        # hand 1 should win from kicker
        # four of a kind on the board, 13 kicker wins
        board = [(2, "club"), (2, 'heart'), (2, 'spade'), (2, 'diamond'), (6, 'spade')]
        hand_1 = [(12, "club"),(13, "club")]
        hand_2 = [(6, "heart"),(2, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.four_of_a_kind()
        hand_2_res = hand_2_checker.four_of_a_kind()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1)      
        
        
    def test_four_of_a_kind_winner(self):
        # hand 1 should win
        # three 2's on the board with the 4th in their hand
        board = [(2, "spade"), (2, 'spade'), (2, 'spade'), (11, 'club'), (6, 'club')]
        hand_1 = [(5, "spade"),(2, "spade")]
        hand_2 = [(6, "heart"),(3, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.four_of_a_kind()
        hand_2_res = hand_2_checker.four_of_a_kind()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1)    
        
        
    def test_four_of_a_kind_draw(self):
        # draw
        # four of a kind on the board with the highest remaining card on the board
        board = [(2, "spade"), (2, 'spade'), (2, 'spade'), (2, 'club'), (6, 'club')]
        hand_1 = [(3, "spade"),(5, "spade")]
        hand_2 = [(1, "heart"),(5, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.four_of_a_kind()
        hand_2_res = hand_2_checker.four_of_a_kind()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 3)           
        
    def test_full_house_winner(self):
        # hand 1 should win
        # three 2's on the board with 2 5's
        board = [(2, "spade"), (2, 'spade'), (2, 'spade'), (5, 'club'), (6, 'club')]
        hand_1 = [(3, "spade"),(5, "spade")]
        hand_2 = [(10, "heart"),(3, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.full_house()
        hand_2_res = hand_2_checker.full_house()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1)    
        
        
    def test_full_house_draw(self):
        # draw
        # full house on board
        board = [(2, "spade"), (2, 'spade'), (2, 'spade'), (5, 'club'), (5, 'club')]
        hand_1 = [(13, "spade"),(14, "spade")]
        hand_2 = [(12, "heart"),(11, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.full_house()
        hand_2_res = hand_2_checker.full_house()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 3)     
        
        
    def test_full_house_higher_pair(self):
        # three on the board, both players have pair in hand
        # hand 1 should win with the higher pair
        board = [(2, "spade"), (2, 'spade'), (2, 'spade'), (6, 'club'), (5, 'club')]
        hand_1 = [(13, "spade"),(13, "spade")]
        hand_2 = [(12, "heart"),(12, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.full_house()
        hand_2_res = hand_2_checker.full_house()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1)     
        
    def test_flush_draw(self):
        # flush on the board no player has suit
        board = [(2, "spade"), (3, 'spade'), (5, 'spade'), (10, 'spade'), (12, 'spade')]
        hand_1 = [(13, "club"),(13, "club")]
        hand_2 = [(12, "heart"),(12, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.flush()
        hand_2_res = hand_2_checker.flush()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 3)  
        
    def test_flush_winner_with_flush_on_board(self):
        # flush on the board but hand 1 has a higher suited card
        board = [(2, "spade"), (3, 'spade'), (5, 'spade'), (10, 'spade'), (12, 'spade')]
        hand_1 = [(13, "club"),(13, "spade")]
        hand_2 = [(12, "heart"),(9, "spade")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.flush()
        hand_2_res = hand_2_checker.flush()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1)         
        
    def test_flush_winner(self):
        # hand 1 has the flush 
        board = [(2, "spade"), (3, 'spade'), (5, 'spade'), (10, 'club'), (12, 'club')]
        hand_1 = [(13, "spade"),(14, "spade")]
        hand_2 = [(12, "heart"),(12, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.flush()
        hand_2_res = hand_2_checker.flush()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1)   
        
        
    def test_straight_draw(self):
        # straight on the board
        # NOTE: hand_1 has a straight A->5 but it is still a tie since they share the max straight
        board = [(2, "spade"), (3, 'spade'), (4, 'spade'), (5, 'club'), (6, 'club')]
        hand_1 = [(13, "spade"),(14, "spade")]
        hand_2 = [(12, "heart"),(12, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.straight()
        hand_2_res = hand_2_checker.straight()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 3)      
    
    def test_straight_draw_not_on_board(self):
        board = [(2, "spade"), (3, 'spade'), (4, 'spade'), (5, 'club'), (6, 'club')]
        hand_1 = [(13, "spade"),(7, "spade")]
        hand_2 = [(12, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.straight()
        hand_2_res = hand_2_checker.straight()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 3) 
    
    def test_straight_winner_with_higher_straight(self):
        # both have a straight that extends what is on the board but hand 1 extends further
        board = [(2, "spade"), (3, 'spade'), (4, 'spade'), (5, 'club'), (6, 'club')]
        hand_1 = [(8, "spade"),(7, "spade")]
        hand_2 = [(12, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.straight()
        hand_2_res = hand_2_checker.straight()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1) 
        
    def test_straight_winner(self):
        # hand 1 has a straight and hand 2 does not
        board = [(8, "spade"), (9, 'spade'), (10, 'spade'), (5, 'club'), (6, 'club')]
        hand_1 = [(11, "spade"),(12, "club")]
        hand_2 = [(12, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.straight()
        hand_2_res = hand_2_checker.straight()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1) 
        
    def test_three_of_a_kind_draw(self):
        # three of a kind on the board along with the 2 highest kickers on the board
        board = [(8, "spade"), (8, 'spade'), (8, 'spade'), (14, 'club'), (13, 'club')]
        hand_1 = [(11, "spade"),(12, "club")]
        hand_2 = [(12, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.three_of_a_kind()
        hand_2_res = hand_2_checker.three_of_a_kind()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 3) 
        
    def test_three_of_a_kind_winner_from_kicker(self):
        # three of a kind on the board but hand 1 has the higher kicker
        board = [(8, "spade"), (8, 'spade'), (8, 'spade'), (10, 'club'), (13, 'club')]
        hand_1 = [(11, "spade"),(14, "club")]
        hand_2 = [(12, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.three_of_a_kind()
        hand_2_res = hand_2_checker.three_of_a_kind()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1) 
        
    def test_three_of_a_kind_winner_trips_over_trips(self):
        # both hands make trips, but hand 1 has the higher trips
        board = [(8, "spade"), (8, 'spade'), (9, 'spade'), (14, 'club'), (13, 'club')]
        hand_1 = [(9, "spade"),(9, "club")]
        hand_2 = [(12, "heart"),(8, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.three_of_a_kind()
        hand_2_res = hand_2_checker.three_of_a_kind()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1) 
        
    def test_three_of_a_kind_winner(self):
        # hand 1 a pocket pair making trips 
        board = [(8, "spade"), (8, 'spade'), (9, 'spade'), (14, 'club'), (13, 'club')]
        hand_1 = [(9, "spade"),(9, "club")]
        hand_2 = [(12, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.three_of_a_kind()
        hand_2_res = hand_2_checker.three_of_a_kind()
        res = sim.check_generic_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1) 
        
    
    def test_two_pair_draw_kicker_on_board(self):
        # two pair on board and the highest kicker is on the board
        board = [(8, "spade"), (8, 'spade'), (9, 'spade'), (9, 'club'), (14, 'club')]
        hand_1 = [(3, "spade"),(1, "club")]
        hand_2 = [(3, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.two_pair()
        hand_2_res = hand_2_checker.two_pair()
        res = sim.check_two_pair_winner(hand_1_res, hand_2_res, hand_1, hand_2, board)   
        self.assertEqual(res, 3) 
        
    def test_two_pair_draw_kicker_in_both_hands(self):
        # two pair on board and the highest kicker is present in both player hands
        board = [(8, "spade"), (8, 'spade'), (9, 'spade'), (9, 'club'), (4, 'club')]
        hand_1 = [(13, "spade"),(1, "club")]
        hand_2 = [(13, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.two_pair()
        hand_2_res = hand_2_checker.two_pair()
        res = sim.check_two_pair_winner(hand_1_res, hand_2_res, hand_1, hand_2, board)   
        self.assertEqual(res, 3) 
        
    def test_two_pair_winner_from_kicker(self):
        # two pair on board and the highest kicker is present in only hand 1
        board = [(8, "spade"), (8, 'spade'), (9, 'spade'), (9, 'club'), (4, 'club')]
        hand_1 = [(14, "spade"),(1, "club")]
        hand_2 = [(13, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.two_pair()
        hand_2_res = hand_2_checker.two_pair()
        res = sim.check_two_pair_winner(hand_1_res, hand_2_res, hand_1, hand_2, board)   
        self.assertEqual(res, 1)   
        
    def test_two_pair_winner_from_pairs_in_hand(self):
        # hand 1 has a pocket pair with a pair on the board
        board = [(8, "spade"), (8, 'spade'), (9, 'spade'), (7, 'club'), (4, 'club')]
        hand_1 = [(10, "spade"),(10, "club")]
        hand_2 = [(13, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.two_pair()
        hand_2_res = hand_2_checker.two_pair()
        res = sim.check_two_pair_winner(hand_1_res, hand_2_res, hand_1, hand_2, board)   
        self.assertEqual(res, 1) 
        
    def test_two_pair_winner_from_pairs(self):
        # hand 1 make pairs with two board cards
        board = [(8, "spade"), (7, 'spade'), (9, 'spade'), (2, 'club'), (4, 'club')]
        hand_1 = [(8, "spade"),(2, "club")]
        hand_2 = [(13, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.two_pair()
        hand_2_res = hand_2_checker.two_pair()
        res = sim.check_two_pair_winner(hand_1_res, hand_2_res, hand_1, hand_2, board)   
        self.assertEqual(res, 1) 
         
    def test_pair_draw(self):
        # pair on the board and all the highest kickers on the board
        board = [(8, "spade"), (8, 'spade'), (13, 'spade'), (12, 'club'), (14, 'club')]
        hand_1 = [(5, "spade"),(2, "club")]
        hand_2 = [(3, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.pair()
        hand_2_res = hand_2_checker.pair()
        res = sim.check_pair_winner(hand_1_res, hand_2_res, hand_1, hand_2, board)   
        self.assertEqual(res, 3) 
             
    def test_pair_draw_from_same_pair(self):
        # both make the same pair and have the same kicker
        board = [(3, "spade"), (5, 'spade'), (13, 'spade'), (12, 'club'), (14, 'club')]
        hand_1 = [(5, "spade"),(7, "club")]
        hand_2 = [(5, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.pair()
        hand_2_res = hand_2_checker.pair()
        res = sim.check_pair_winner(hand_1_res, hand_2_res, hand_1, hand_2, board)   
        self.assertEqual(res, 3)      
        
    def test_pair_draw_from_same_pair(self):
        # both make the same pair and have the same kickers on the board
        board = [(11, "spade"), (5, 'spade'), (13, 'spade'), (12, 'club'), (14, 'club')]
        hand_1 = [(5, "spade"),(7, "club")]
        hand_2 = [(5, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.pair()
        hand_2_res = hand_2_checker.pair()
        res = sim.check_pair_winner(hand_1_res, hand_2_res, hand_1, hand_2, board)   
        self.assertEqual(res, 3)      
        
    def test_pair_winner_from_higher_pair(self):
        # hand 1 has the higher pair
        board = [(11, "spade"), (5, 'spade'), (13, 'spade'), (12, 'club'), (14, 'club')]
        hand_1 = [(11, "spade"),(7, "club")]
        hand_2 = [(5, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.pair()
        hand_2_res = hand_2_checker.pair()
        res = sim.check_pair_winner(hand_1_res, hand_2_res, hand_1, hand_2, board)   
        self.assertEqual(res, 1)   
        
    def test_pair_winner_from_higher_kicker(self):
        # both hands have the same pair but hand 1 has the higher kicker to play
        board = [(11, "spade"), (5, 'spade'), (10, 'spade'), (12, 'club'), (14, 'club')]
        hand_1 = [(11, "spade"),(13, "club")]
        hand_2 = [(11, "heart"),(7, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.pair()
        hand_2_res = hand_2_checker.pair()
        res = sim.check_pair_winner(hand_1_res, hand_2_res, hand_1, hand_2, board)   
        self.assertEqual(res, 1)   
        
    def test_high_card_draw_from_full_board(self):
        # draw since the 5 highest cards are on the board
        board = [(11, "spade"), (10, 'spade'), (14, 'spade'), (8, 'club'), (7, 'club')]
        hand_1 = [(2, "spade"),(1, "club")]
        hand_2 = [(3, "heart"),(4, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.high_card()
        hand_2_res = hand_2_checker.high_card()
        res = sim.check_high_card_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 3)    
        
    def test_high_card_draw_from_same_high_card_in_hand(self):
        # draw since the 5 highest cards are on the board
        board = [(11, "spade"), (10, 'spade'), (13, 'spade'), (8, 'club'), (7, 'club')]
        hand_1 = [(14, "spade"),(1, "club")]
        hand_2 = [(14, "heart"),(4, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.high_card()
        hand_2_res = hand_2_checker.high_card()
        res = sim.check_high_card_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 3)  
        
    def test_high_card_draw_from_same_high_card_in_hand(self):
        # draw since the 5 highest cards are on the board
        board = [(11, "spade"), (10, 'spade'), (13, 'spade'), (8, 'club'), (7, 'club')]
        hand_1 = [(14, "spade"),(1, "club")]
        hand_2 = [(14, "heart"),(4, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.high_card()
        hand_2_res = hand_2_checker.high_card()
        res = sim.check_high_card_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 3)  
        
    def test_high_card_winner_from_hand_holding_high_card(self):
        # hand 1 wins since it is holding the highest card
        board = [(11, "spade"), (10, 'spade'), (13, 'spade'), (8, 'club'), (7, 'club')]
        hand_1 = [(14, "spade"),(1, "club")]
        hand_2 = [(13, "heart"),(4, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.high_card()
        hand_2_res = hand_2_checker.high_card()
        res = sim.check_high_card_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1)  
        
    def test_high_card_winner_from_hand_holding_second_high_card(self):
        # both are holding the same high card but hand 1 wins since it has the next highest card
        board = [(8, "spade"), (7, 'spade'), (13, 'spade'), (8, 'club'), (7, 'club')]
        hand_1 = [(14, "spade"),(10, "club")]
        hand_2 = [(14, "heart"),(9, "heart")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.high_card()
        hand_2_res = hand_2_checker.high_card()
        res = sim.check_high_card_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1)  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def test_high_card_draw(self):
        board = [(6, "spade"), (5, 'spade'), (7, 'spade'), (8, 'spade'), (9, 'spade'),]
        hand_1 = [(2, "spade"),(1, "heart")]
        hand_2 = [(2, "diamond"),(4, "diamond")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.high_card()
        hand_2_res = hand_2_checker.high_card()
        res = sim.check_high_card_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 3)           
        
    def test_high_card_winner(self):
        # hand 1 should win
        board = [(2, "spade"), (3, 'spade'), (4, 'spade'), (5, 'spade'), (6, 'spade'),]
        hand_1 = [(10, "spade"),(14, "heart")]
        hand_2 = [(11, "diamond"),(13, "diamond")]
        sim = Simulator(1, hand_1, hand_2, False)
        hand_1_checker = HandChecker(hand_1, board)        
        hand_2_checker = HandChecker(hand_2, board)        
        hand_1_res = hand_1_checker.high_card()
        hand_2_res = hand_2_checker.high_card()
        res = sim.check_high_card_winner(hand_1_res, hand_2_res)   
        self.assertEqual(res, 1)    
        
        
        
if __name__ == '__main__':
    unittest.main()
    
        
        

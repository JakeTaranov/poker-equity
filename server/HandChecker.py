class HandChecker():
    
    @staticmethod
    def generate_rank_counts(cards):
        rank_counts = {}
        for rank, _ in cards:
            rank_counts[rank] = rank_counts.get(rank, 0) + 1
        return rank_counts
    
    
    # returns a dict of each suit with a list of its correspoding ranks assoositaed
    # eg: "clubs": [1,4,6,16],
    #     "hearts": [5,15]
    #     etc....
    
    @staticmethod
    def generate_suit_counts(cards):
        suit_counts = {}
        for rank, suit in cards:
            if suit not in suit_counts:
                suit_counts[suit] = [rank]
            else:
                suit_counts[suit].append(rank)
            
            
        return suit_counts
        
        
    def __init__(self, player_cards, board):
        self.player_cards = player_cards
        self.board = board
        self.board_and_player_cards = player_cards + board
        self.all_ranks = [rank for rank, _ in self.board_and_player_cards]
        self.all_rank_counts = self.generate_rank_counts(self.board_and_player_cards)        
        self.player_cards_ranks = [rank for rank, _ in self.player_cards]
        self.all_suit_counts = self.generate_suit_counts(self.board_and_player_cards)
    
    def high_card(self):
        return sum(sorted(self.all_ranks, reverse=True)[:5])

    @staticmethod
    def pair_helper(player_cards, board, ranks):
        cur_max_pair = 0
        # NOTE: the reason we need to make a new board_and_player_cards here is since we are sometimes passing this function 
        #       an empty list so we can is to see if there exist two pair on the board alone
        for rank, count in ranks.items():
            if count == 2:
                cur_max_pair = max(cur_max_pair, rank)
                
        return cur_max_pair

    def pair(self):    
        board_pair = self.pair_helper([], self.board, self.all_rank_counts)
        board_hand_pair = self.pair_helper(self.player_cards, self.board, self.all_rank_counts)
        
        # logic is similar to two pair, read comments if confused
        if board_pair == board_hand_pair:
            return board_pair   
        else:
            return board_hand_pair
        
        
    @staticmethod
    def two_pair_helper(player_cards, board):
        cur_max_two_pairs = 0
        rank_counts = {}
        # NOTE: the reason we need to make a new board_and_player_cards here is since we are sometimes passing this function 
        #       an empty list so we can is to see if there exist two pair on the board alone
        board_and_player_cards = player_cards + board
        # try and use the rank counts from the list we already have generates, substract the lists???
        for rank, _ in board_and_player_cards:
            rank_counts[rank] = rank_counts.get(rank, 0) + 1
            
        pairs = [rank for rank, count in rank_counts.items() if count == 2]
        
        pairs = sorted(pairs, reverse=True)
        if len(pairs) >= 2:
            cur_max_two_pairs = [pairs[0], pairs[1]]
        
        return cur_max_two_pairs
    
    

    def two_pair(self):
        
        board_two_pair = self.two_pair_helper(player_cards=[], board=self.board)
        board_and_hand_two_pair = self.two_pair_helper(player_cards = self.player_cards, board = self.board)
        
        # if the pair top pair on the self.board is the same as the top pair with self.player_cardss then return the top pair (either)
        if board_two_pair == board_and_hand_two_pair:
            return board_two_pair
        else:
        # if the pair on the self.board is not the same as the pair with the players hand, then this means
        # the pair with the players hand must be higher since we return the max 
            return board_and_hand_two_pair
                

    # finds the reamining two cards from a board that has three of a kind on it 
    # eg: board = 4 4 4 2 1, function return 2, 1
    @staticmethod
    def find_unique_in_three_of_a_kind(board):
        count = {}
        for rank, _ in board:
            count[rank] = count.get(rank, 0) + 1
        
        unique = [rank for rank, count in count.items() if count == 1]
        return unique
      
      
      
    #NOTE: FIX THIS UGLY SHIT, ONLY USE THIS CODE ONCE. DRY BITCH
    @staticmethod
    def three_of_a_kind_helper(player_cards, board):
        board_and_player_cards = player_cards + board
        cur_max_trips = 0
        rank_counts = {}
        for rank, _ in board_and_player_cards:
            rank_counts[rank] = rank_counts.get(rank, 0) + 1
        
        for rank, count in rank_counts.items():
            if count == 3:
                cur_max_trips = max(cur_max_trips, rank)
        
        return cur_max_trips   
          
      
      
    # how will this wor    
    def three_of_a_kind(self):        
        board_three_of_a_kind = self.three_of_a_kind_helper(player_cards=[], board=self.board)
        board_and_player_cards_three_of_a_kind = self.three_of_a_kind_helper(player_cards=self.player_cards, board=self.board)
        
        if board_three_of_a_kind == 0 and board_and_player_cards_three_of_a_kind == 0:
            return 0
        # same logic as two pair and pair is comments there if confused
        if board_three_of_a_kind == board_and_player_cards_three_of_a_kind:
            # since the best three of a hand kind is on the board, then we must consider the kicker
            unique_in_board = self.find_unique_in_three_of_a_kind(self.board)
            possible_cards = sorted(self.player_cards_ranks + unique_in_board, reverse=True)
            return sum(possible_cards[:2])
        else:
            # if it is not the best, then the player must have the higher three of a kind
            return board_and_player_cards_three_of_a_kind

        
    def straight(self):
        rank_set = sorted(set(rank for rank, _ in self.board_and_player_cards))
        straight_score = 0
        
        for i in range(len(rank_set) - 4):
            #check to see if there is any straight
            if rank_set[i] == rank_set[i + 1] - 1 == rank_set[i + 2] - 2 == rank_set[i + 3] - 3 == rank_set[i + 4] - 4:
                straight_score = max(straight_score ,rank_set[i] + rank_set[i+1] + rank_set[i+2] + rank_set[i+3] + rank_set[i+4])
        
        #check to see if there is an ace -> 5 straight
        if rank_set[-1] == 14 and rank_set[0] == 2 and rank_set[1] == 3 and rank_set[2] == 4 and rank_set[3] == 5:
            straight_score = max(straight_score ,rank_set[i] + rank_set[i+1] + rank_set[i+2] + rank_set[i+3] + rank_set[i+4])
        
        return straight_score

    def flush(self):
        max_rank_flush = 0
                
        for _, ranks in self.all_suit_counts.items():
            # if a suit has 5 or more elemetns to its category, then there is a flush
            if len(ranks) >= 5:
                max_rank_flush = max(max_rank_flush, sum(sorted(ranks, reverse=True)[:5]))
                
        return max_rank_flush

    def full_house(self):                
        three_of_a_kind = False
        two_of_a_kind = False
        max_full_three = 0
        max_full_two = 0
            
        for rank, count in self.all_rank_counts.items():
            if count == 3:
                three_of_a_kind = True
                max_full_three = max(max_full_three, rank)
            elif count == 2:
                two_of_a_kind = True
                max_full_two = max(max_full_two, rank)
        
        if three_of_a_kind and two_of_a_kind:
            return max_full_three*3 + max_full_two*2
        return 0


    @staticmethod
    def find_unique_in_four_of_a_kind(board):
        count = {}
        
        for rank, _ in board:
            count[rank] = count.get(rank, 0) + 1
            
        unique = [rank for rank, count in count.items() if count == 1]
        return unique
    
    @staticmethod
    def four_of_a_kind_helper(player_cards, board):
        rank_counts = {}
        board_and_player_cards = player_cards + board
        cur_max_quads = 0
        for rank, _ in board_and_player_cards:
            rank_counts[rank] = rank_counts.get(rank, 0) + 1
            
        
        for rank, count in rank_counts.items():
            if count >= 4:
                cur_max_quads = max(cur_max_quads, rank)
        
        return cur_max_quads

    def four_of_a_kind(self):
        
        board_four_of_a_kind = self.four_of_a_kind_helper(player_cards=[], board=self.board)
        board_and_player_four_of_a_kind = self.four_of_a_kind_helper(player_cards=self.player_cards, board=self.board)
        
        
        if board_four_of_a_kind == 0 and board_and_player_four_of_a_kind == 0:
            return 0
        #same logic as three of a kind and two pair etc...
        if board_four_of_a_kind == board_and_player_four_of_a_kind:
            unique_in_board = self.find_unique_in_four_of_a_kind(self.board)
            possible_cards = self.player_cards_ranks + unique_in_board
            return max(possible_cards)
        else:
            return board_and_player_four_of_a_kind 
                

    def straight_flush(self):
        
        has_flush = self.flush()
        has_straight = self.straight()
        max_straight_flush = 0
        
        if has_flush and has_straight:
            #returns the max value of the straight
            max_straight_flush = has_straight
        
        return max_straight_flush
            

    def royal_flush(self):
        
        if self.straight() and self.flush():
            straight_flush_ranks = [rank for rank, _ in self.board_and_player_cards if rank in {10, 11, 12, 13, 14}]
            
            if set(straight_flush_ranks) == {10, 11, 12, 13, 14}:
                return 1
            
        return 0       
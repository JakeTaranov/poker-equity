from HandChecker import HandChecker
import random

h1c1 = { "suit": "heart", "value": "Q", "rank": 1, "isPlayable": True }
h1c2 = { "suit": "heart", "value": "Q", "rank": 1, "isPlayable": True }
h1 = [(h1c1["rank"], h1c2["suit"]), (h1c2["rank"], h1c2["suit"])]


h2c1 = { "suit": "heart", "value": "Q", "rank": 13, "isPlayable": True }
h2c2 = { "suit": "heart", "value": "Q", "rank": 14, "isPlayable": True }
h2 = [(h2c1["rank"], h2c2["suit"]), (h2c2["rank"], h2c2["suit"])]

board_raw = [
    { "suit": "spade", "value": "Q", "rank": 15, "isPlayable": True },
    { "suit": "club", "value": "Q", "rank": 20, "isPlayable": True },
    { "suit": "heart", "value": "Q", "rank": 10, "isPlayable": True },
    { "suit": "heart", "value": "Q", "rank": 11, "isPlayable": True },
    { "suit": "heart", "value": "Q", "rank": 12, "isPlayable": True },
]

board = [(board_raw[0]["rank"], board_raw[0]["suit"]), (board_raw[1]["rank"], board_raw[1]["suit"]), (board_raw[2]["rank"], board_raw[2]["suit"]), (board_raw[3]["rank"], board_raw[3]["suit"]), (board_raw[4]["rank"], board_raw[4]["suit"])]



hand_2_check = HandChecker(player_cards=h2, board=board)
hand_1_check = HandChecker(player_cards=h1, board=board)

pair_1 = hand_1_check.check_pair()
pair_2 = hand_2_check.check_pair()

two_pair_1 = hand_1_check.check_two_pair()
two_pair_2 = hand_2_check.check_two_pair()

three_1 = hand_1_check.check_three_of_a_kind()
three_2 = hand_2_check.check_three_of_a_kind()

straight_1 = hand_1_check.check_straight()
straight_2 = hand_2_check.check_straight()

flush_1 = hand_1_check.check_flush()
flush_2 = hand_2_check.check_flush()

fh_1 = hand_1_check.check_full_house()
fh_2 = hand_2_check.check_full_house()

four_1 = hand_1_check.check_four_of_a_kind()
four_2 = hand_2_check.check_four_of_a_kind()

sf_1 = hand_1_check.check_straight_flush()
sf_2 = hand_2_check.check_straight_flush()

rf_1 = hand_1_check.check_royal_flush()
rf_2 = hand_2_check.check_royal_flush()


print("PAIR", pair_1, pair_2)
print("TWO PAIR", two_pair_1, two_pair_2)
print("THREE", three_1, three_2)
print("STRAIGHT", straight_1, straight_2)
print("FLUSH", flush_1, flush_2)
print("FULL HOUSE", fh_1, fh_2)
print("FOUR", four_1, four_2)
print("STRAIGHT FLUSH", sf_1, sf_2)
print("ROYAL FLUSH", rf_1, rf_2)
from collections import Counter
import numpy as np
from resurses import possible_streets
from data_struct import CounterStorage


def create_dec():
    dec_nums = np.random.randn(52)
    dec = [0] * 52
    # S - пики, H - червы, D - бубны, С - крести
    for i, suit in enumerate(["S", "H", "D", "C"]):
        for j, num in enumerate(["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]):
            dec[i * 13 + j] = (dec_nums[i * 13 + j], num + suit)
    shuffled_dec = sorted(dec, key=lambda elem: elem[0])
    clear_dec = [card[1] for card in shuffled_dec]
    return clear_dec


def sort_cards(cards):
    card_num = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    card_values_dict = dict(zip(card_num, range(13)))
    sorted_cards = sorted(cards, key=lambda card: card_values_dict[card[0]])
    return sorted_cards


def remove_double_cards(nums_str):
    this_num_str = nums_str[::]
    for num in ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]:
        for _ in range(7):
            this_num_str = this_num_str.replace(num * 2, num, len(this_num_str))
    return this_num_str


class Player:
    def __init__(self, position: str, stake=100.0, name="hero"):
        self.stake = stake
        self.name = name
        if position not in ["SB", "BB", "UTG", "HJ", "CO", "BTN"]:
            raise f"There is no {position} position at the poker table"
        else:
            self.position = position

    def make_bet(self, size: float):
        self.stake -= min(self.stake, size)
        return min(self.stake, size)


class ComboChecker:
    def __init__(self, hand=None, board=None):
        if hand is None:
            raise IOError("Hand can`t be empty!")
        self.hand = hand
        if board is None:
            board = []
        self.board = board
        # собрание всех карт в доступе
        self.cards = sort_cards(hand + board)
        # выделение всех достоинств карт
        self.nums = [card[0] for card in self.cards]
        self.nums_count = dict(zip(Counter(self.nums).values(), Counter(self.nums).keys()))
        # выделение всех достоинств карт
        self.suits = [card[1] for card in self.cards]
        self.suits_count = dict(zip(Counter(self.suits).values(), Counter(self.suits).keys()))

    def update_cards(self, board=None, hand=None):
        if board is not None:
            self.board = board
        if hand is not None:
            self.hand = hand
        # собрание всех карт в доступе
        self.cards = sort_cards(hand + board)
        # выделение всех достоинств карт
        self.nums = [card[0] for card in self.cards]
        self.nums_count = CounterStorage(self.nums)
        # выделение всех мастей карт
        self.suits = [card[1] for card in self.cards]
        self.suits_count = CounterStorage(self.suits)

    def get_most_freq_suit(self):
        sorted_dict = dict(sorted(self.suits_count.items(), key=lambda x: x[0]))
        return list(sorted_dict.values())[-1], list(sorted_dict.keys())[-1]

    def get_most_freq_num(self):
        quan_most_freq_num = max(self.nums_count.keys())
        return self.nums_count[quan_most_freq_num], quan_most_freq_num

    def find_higher_combo(self):
        my_cards_set_str = remove_double_cards("".join(self.nums))
        quan_most_freq_suit = max(self.suits_count.keys())
        most_freq_suit = self.suits_count[quan_most_freq_suit]
        quan_most_freq_num = max(self.nums_count.keys())
        most_freq_num = self.nums_count[quan_most_freq_num]  # self.get_most_freq_num()
        if quan_most_freq_suit >= 5:
            street_nums = ""
            for card in self.cards:  # оставляются только карты самой частой масти
                street_nums += card[0] if most_freq_suit in card else ""
            if 'TJQKA' in street_nums: return "FR"
            for street in possible_streets:
                if street in street_nums: return "FST" + street[-1]
        if quan_most_freq_num == 4: return "FK" + most_freq_num
        if 3 in self.nums_count.keys() and 2 in self.nums_count.keys():
            return "FH" + self.nums_count[3] + self.nums_count[2]
        if quan_most_freq_suit >= 5: return "F" + street_nums[-1:-6:-1]
        for street in possible_streets:
            if street in my_cards_set_str: return "ST" + street[-1]
        if 3 in self.nums_count.keys():
            return "TK" + self.nums_count[3] + "".join(self.nums).replace(self.nums_count[3], "", 3)[-1:-3:-1]
        if "".join(map(str, self.nums_count.keys())).rfind("2") != "".join(map(str, self.nums_count.keys())).find(
            "2"): return "DP"

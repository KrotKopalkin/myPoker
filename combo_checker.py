from dec_generator import *

print({3:"3",3:"4"})
for _ in range(1):
    dec = create_dec()
    hand = ['4H', '6H']  # dec[:2]
    board = ['6C', '6S', '7H', '7S', '7D']  # dec[2:randint(2, 7)]
    combo_checker = ComboChecker(hand, board)
    combo = combo_checker.find_higher_combo()
    print(combo_checker.nums)
    print(f"Hand: {hand},Board: {board}, Sorted: {sort_cards(hand + board)}, Combo: {combo}")

from dec_generator import *
from time import time

start_time = time()

sorted_dec = sort_cards(create_dec())
boards = []
for c1 in range(len(sorted_dec)):
    for c2 in range(c1+1, len(sorted_dec)):
        for c3 in range(c2+2, len(sorted_dec)):
            boards += [[sorted_dec[c1], sorted_dec[c2], sorted_dec[c3]]]
boards = np.array(boards)
print(len(boards))
print(boards)
print(time() - start_time)

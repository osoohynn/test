import random as r
import time as t

u = r.sample(range(1,46),6)
u.sort()
print(u)


import random as r
card = ['A', '4', '1', 'K', 'Q']
print(card)
r.shuffle(card)
print(card)
print(r.choice(card))
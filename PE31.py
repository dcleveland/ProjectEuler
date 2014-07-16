"""Project Euler problem 31
https://projecteuler.net/problem=31

In England the currency is made up of pound and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 100p and 200p.
It is possible to make 2 lbs in the following way:

1x100p + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can 2 pounds be made using any number of coins?

"""
from itertools import permutations

COINS = [1, 2, 5, 10, 20, 50, 100, 200]

perms = {}

for i in range(0, 201):
    perms[i, 0] = 1

for i in range(0, 201):
    for j in range(1, len(COINS)):
        perms[i, j] = 0
        if i >= COINS[j]:
            perms[i, j] += perms[i, j-1]
            perms[i, j] += perms[i-COINS[j], j]
        else:
            perms[i, j] = perms[i, j-1]


print perms[200, 7]
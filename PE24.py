"""Project Euler problem 24
https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""
# Cheating?
from itertools import permutations

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

if __name__ == "__main__":
  perms = list(permutations(digits))
  perms.sort()
  print ("The millionth lexographic permutation of the digits 0, 1, 2, 3, 4, 5,"
         " 6, 7, 8 and 9 is %s." % ("".join(list(perms[999999]))))
  
  # The millionth lexographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7,
  # 8 and 9 is 2783915460.
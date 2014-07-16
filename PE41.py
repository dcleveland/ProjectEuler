"""Project Euler problem 41
https://projecteuler.net/problem=41

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""
from itertools import permutations
import math

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

max_pand = 0

def IsPrime(n):
  if n % 2 == 0 and n > 2: 
    return False
  return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

if __name__ == "__main__":
  for i in range(1, 10):
    numbers = range(1, i + 1)
    perms = permutations(numbers)
    candidates = []
    while True:
      try:
        c = int("".join([str(x) for x in perms.next()]))
        if IsPrime(c) and c > max_pand:
          max_pand = c
      except:
        break

  print "The max n-digit pandigital number that is prime is %s." % max_pand

  # The max n-digit pandigital number that is prime is 7652413

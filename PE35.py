"""Project Euler problem 35
https://projecteuler.net/problem=35

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""

import math


# Borrowing from PE7.py
def IsPrime(n):
  if n % 2 == 0 and n > 2: 
    return False
  return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def IsCircular(n):
  if not IsPrime(n):
    return False
  n_rotations = len(str(n))
  rotations = [n]
  for i in range(1, n_rotations):
    rotations.append(int(str(n)[i:] + str(n)[0:i]))
  return all(IsPrime(r) for r in rotations)


if __name__ == "__main__":
  circular = set()
  for i in range(2, 1000001):
    if IsCircular(i):
        circular.add(i)
  print "There are %s circular primes below one million." % len(circular)

  # There are 55 circular primes below one million.
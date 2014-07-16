"""Project Euler problem 37
https://projecteuler.net/problem=37

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import math


def IsPrime(n):
  if n % 2 == 0 and n > 2 or n == 1: 
    return False
  return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

trunctable_primes = set()
n = 10
while len(trunctable_primes) < 11:
  if IsPrime(n):
    if all(IsPrime(int(str(n)[i:])) for i in range(0, len(str(n)))) and \
        all(IsPrime(int(str(n)[0:j])) for j in range(1, len(str(n)))):
      trunctable_primes.add(n)
  n += 1
print ("The sum of the eleven primes that are both truncatble from left to "
       "right and right to left is %s." % (sum(trunctable_primes)))

# The sum of the eleven primes that are both truncatble from left to right and
# right to left is 748317.

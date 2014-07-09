# Project Euler problem 10
# https://projecteuler.net/problem=

# Find the sum of the primes below one million

import math
import sys

# Sieve of Eratosthenes (http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
# w/ some minor improvements

N = int(2e6)


def GetPrimes(n=2e6):
  primes = []
  numbers = range(2, n + 1)
  not_prime = set()
  x = 2
  while True:
    sys.stdout.write("\rX = %s" % x)
    sys.stdout.flush()
    if x*numbers[0] > n:
      return
    mults = [x*j for j in numbers if x*j in numbers]
    for y in mults:
      numbers.pop(numbers.index(y))
    try:
      x = numbers[numbers.index(x) + 1]
    except:
      break
  return numbers


# Much faster algorithm borrowing IsPrime() from PE7.py
def IsPrime(n):
  if n % 2 == 0 and n > 2: 
    return False
  return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def GetPrimes(n=2e6):
  primes = []
  for i in range(2, n+1):
    if IsPrime(i):
      primes.append(i)
  return primes

def GetSum(n=2e6):
  sum_n = sum(GetPrimes(int(n)))
  return sum_n

if __name__ == "__main__":
  print "Sum of primes below %s is %s" % (N, GetSum())
  # Sum of primes below 2000000.0 is 142913828922

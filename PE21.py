"""Project Euler problem 21
https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a != b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import math


def GetFactorSum(n):
  factors = set()
  factors.add(1)
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i:
      factors.add(i)
      factors.add(n/i)
  return sum(list(factors))


if __name__ == "__main__":
  numbers = range(10000)
  amicables = set()
  for i in numbers:
    fsum = GetFactorSum(i)
    if i == GetFactorSum(fsum) and i != fsum:
      amicables.add(i)
      amicables.add(fsum)
  print "The sum of amicable numbers below 10,000 is %s." % sum(list(amicables))

  # The sum of amicable numbers below 10,000 is 31626. 
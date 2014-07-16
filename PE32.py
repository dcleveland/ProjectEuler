"""Project Euler problem 32
https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""
import sys


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pandigitals = set()


def IsPandigital(identity_str):
  if len(str(identity_str)) != 9:
    return False
  for i in range(1, 10):
    if str(i) not in identity_str:
      return False
  return True

if __name__ == "__main__":
  for i in range(0, 5000):
    for j in range(0, 500):
      if len(str(i*j) + str(i) + str(j)) > 9:
        break
      if IsPandigital(str(i) + str(j) + str(i*j)):
        print "\rFound a pandigital! %s * %s = %s" % (str(i), str(j), str(i*j))
        pandigitals.add(i*j)

  print ("There are %s products whose multiplicand, multiplier, product "
         "identity can be written as a 1 through 9 pandigital. Their total "
         "sum is %s" % (len(pandigitals), sum(list(pandigitals))))
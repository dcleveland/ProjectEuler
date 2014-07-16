"""Project Euler problem 34
https://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


def GetFactorial(n):
  product = 1
  for i in range(1, n + 1):
    product *= i
  return product


curious = set()
# Curious how to prove that you don't need to go higher than 50000
for i in range(3, 50000):
  digits = [int(x) for x in str(i)]
  if sum([GetFactorial(j) for j in digits]) == i:
    curious.add(i)


print "The sum of curious numbers is %s." % (sum(curious))

# The sum of curious numbers is 40730.
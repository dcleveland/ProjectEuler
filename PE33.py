"""Project Euler problem 33
https://projecteuler.net/problem=33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.
"""
import math


# borrowing from PE23.py
def GetFactors(n):
  factors = set()
  factors.add(1)
  for i in range(2, int(math.sqrt(n)) + 1):
    if not n % i:
      factors.add(i)
      factors.add(n/i)
  factors.add(n)
  return list(factors)


fractions = set()

for a in range(10, 100):
  for b in range(10, 100):
    if a >= b:
      continue
    a_digits = [x for x in str(a)]
    b_digits = [y for y in str(b)]
    if a_digits[0] == b_digits[1] and b_digits[1]:
      if (int(a_digits[1]) + 0.) / int(b_digits[0]) == (a + 0.) / b:
        fractions.add((a, b))
    elif a_digits[1] == b_digits[0] and int(b_digits[1]):
      if (int(a_digits[0]) + 0.) / int(b_digits[1]) == (a + 0.) / b:
        fractions.add((a, b))
numerator = 1
denominator = 1
result = ""
for f in fractions:
  result += "%s / %s\n" % (f[0], f[1])
  numerator *= f[0]
  denominator *= f[1]


print result
print "Product of the fractions is %s / %s" % (numerator, denominator)

while True:
  n_factors = GetFactors(numerator)
  d_factors = GetFactors(denominator)
  overlap = set(n_factors).intersection(set(d_factors)) - set([1])
  if overlap:
    divisor = max(overlap)
    numerator = numerator / divisor
    denominator = denominator / divisor
  else:
    break

print "The reduced fraction is %s / %s." % (numerator, denominator)
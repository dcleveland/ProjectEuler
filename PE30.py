"""Project Euler problem 30
https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""
good = set()

FIFTH_POWERS = {
  1: 1**5,
  2: 2**5,
  3: 3**5,
  4: 4**5,
  5: 5**5,
  6: 6**5,
  7: 7**5,
  8: 8**5,
  9: 9**5,
  0: 0**5
}

# Brute force method: check all numbers in a huge range and assume that's all
# of them.
for i in range(4150, 9999999):
  digits = [int(x) for x in str(i)]
  if sum([x**5 for x in digits]) == i:
    good.add(i)
print ", ".join([str(g) for g in list(good)])

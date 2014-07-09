"""# Project Euler problem 16
# https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

if __name__ == "__main__":
  power_str = str(2**1000)
  power_sum = sum([int(x) for x in power_str])
  print "The sum of the digits of 2^1000 = %s" % power_sum

  # The sum of the digits of 2^1000 = 1366
"""Project Euler problem 43
https://projecteuler.net/problem=43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
valid_sum = 0


def CheckDivisors(number):
  if int(str(number)[3]) % 2:
    return False
  elif int(str(number)[2:5]) % 3:
    return False
  elif int(str(number)[5]) % 5:
    return False
  elif int(str(number)[4:7]) % 7:
    return False
  elif int(str(number)[5:8]) % 11:
    return False
  elif int(str(number)[6:9]) % 13:
    return False
  elif int(str(number)[7:]) % 17:
    return False
  else:
    return True


if __name__ == "__main__":
  perms = permutations(digits, 10)
  while True:
    try:
      n = int("".join(str(x) for x in perms.next()))
      if CheckDivisors(n):
        valid_sum += n
    except:
      break
  print ("The sum of 0 to 9 palandromes with the same divisibility properties"
         " of 1406357289 is %s." % valid_sum)

  # The sum of 0 to 9 palandromes with the same divisibility properties is
  # 16695334890.

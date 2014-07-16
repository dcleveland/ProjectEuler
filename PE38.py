"""Project Euler problem 38
https://projecteuler.net/problem=38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""


# Borrowing from PE36.py
def IsPandigital(identity_str):
  if len(str(identity_str)) != 9:
    return False
  for i in range(1, 10):
    if str(i) not in identity_str:
      return False
  return True

max_pandigital = 0

if __name__ == "__main__":
  for i in range(1, 50000):
    concat = ""
    for j in range(1, 1000):
      concat += "%s" % str(i*j)
      if len(concat) > 9:
        break
      elif IsPandigital(concat) and int(concat) > max_pandigital:
        max_pandigital = int(concat)
        integer = i
        series_n = j

  print ("The largest 1 to 9 pandigital 9-digit number that can be formed as "
         "the concatenated product of an integer with (1,2, ... , n) where n > "
         "1 is %s." % max_pandigital)
  print ("%s is the concatenated product of %s and the series (%s)." %
         (max_pandigital, integer,
          ", ".join(str(i) for i in range(1, series_n + 1))))

  # The largest 1 to 9 pandigital 9-digit number that can be formed as the
  # concatenated product of an integer with (1,2, ... , n) where n > 1 is
  # 932718654.
  # 932718654 is the concatenated product of 9327 and the series (1, 2).
"""Project Euler problem 17
# https://projecteuler.net/problem=17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""

NUMBERS_TO_WORDS = {
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  7: "seven",
  8: "eight",
  9: "nine",
  10: "ten",
  11: "eleven",
  12: "twelve",
  13: "thirteen",
  14: "fourteen",
  15: "fifteen",
  16: "sixteen",
  17: "seventeen",
  18: "eighteen",
  19: "nineteen",
  20: "twenty",
  30: "thirty",
  40: "forty",
  50: "fifty",
  60: "sixty",
  70: "seventy",
  80: "eighty",
  90: "ninety",
  100: "hundred",
  1000: "onethousand"
}

def GetLengthOfNumber(n):
  n_str = str(n)
  digits = len(n_str)
  if digits == 1:
    l = len(NUMBERS_TO_WORDS[n])
  elif digits == 2:
    if n in NUMBERS_TO_WORDS:
      l = len(NUMBERS_TO_WORDS[n])
    elif not int(n_str[1]):
      l = len(NUMBERS_TO_WORDS[n])
    else:
      l = len(NUMBERS_TO_WORDS[int(n_str[0] + "0")]) \
          + len(NUMBERS_TO_WORDS[int(n_str[1])])
  elif digits == 3:
    if int(n_str[1:]) in NUMBERS_TO_WORDS:
      l = len(NUMBERS_TO_WORDS[int(n_str[0])]) + len("hundredand") \
          + len(NUMBERS_TO_WORDS[int(n_str[1:])])
    elif not int(n_str[1]): # X0X
      if not int(n_str[2]): # X00
        l = len(NUMBERS_TO_WORDS[int(n_str[0])]) + len("hundred")
      else: # X0N
        l = len(NUMBERS_TO_WORDS[int(n_str[0])]) + len("hundredand") \
            + len(NUMBERS_TO_WORDS[int(n_str[2])])
    elif not int(n_str[2]):
      l = len(NUMBERS_TO_WORDS[int(n_str[0])]) + len("hundredand") \
          + len(NUMBERS_TO_WORDS[int(n_str[1:])])
    else:
      l = len(NUMBERS_TO_WORDS[int(n_str[0])]) + len("hundredand") \
          + len(NUMBERS_TO_WORDS[int(n_str[1] + "0")]) \
          + len(NUMBERS_TO_WORDS[int(n_str[2])])
  else:
    l = len(NUMBERS_TO_WORDS[1000])
  return l


if __name__ == "__main__":
  char_sum = 0
  for i in range(1, 1001):
    char_sum += GetLengthOfNumber(i)
  print "%s characters needed to spell the numbers 1...1000" % char_sum

  #21124 characters needed to spell the numbers 1...1000
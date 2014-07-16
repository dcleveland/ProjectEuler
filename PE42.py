"""Project Euler problem 33
https://projecteuler.net/problem=33

The nth term of the sequence of triangle numbers is given by,

t sub n = 1/2* n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For example,
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""

import codecs

LETTER_SCORES = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

def GetWordScore(word):
  return sum([LETTER_SCORES[i] for i in word])


if __name__ == "__main__":
  fh = codecs.open("words.txt", "r")
  data = fh.read().replace('"', "").split(",")
  scores = [GetWordScore(d) for d in data]
  max_score = max(scores)
  triangles = []
  t = 1
  while t <= max_score:
    triangles.append(t*(t + 1)/2)
    t += 1
  count = 0
  for s in scores:
    if s in triangles:
      count += 1
  print "There are %s triangle words in words.txt." % count

  # There are 162 triangle words in words.txt.

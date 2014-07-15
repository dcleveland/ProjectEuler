"""Project Euler problem 26
https://projecteuler.net/problem=26

Starting with the number 1 and moving to the right in a clockwise direction a 5
by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?

Solution:
We can see that each of the diagonals follows a pattern related to the square of
the "layer" they are on. In particular, if we call i the distance of the upper
right corner from the center then,

top right corner = (i + 2)^2
bottom right corner = (i + 1)^2 - i
bottom left corner = (i + 1)^2 + 1
top left corner = (i + 2)^2 - (i + 1)

"""
if __name__ == "__main__":
  total = 1
  for i in range(3, 1002, 2):
    # Start from i = 3 and make steps of 2 up to 1001.
    total += i**2 + i**2 - (i - 1) + (i-1)**2 - (i - 2) + (i - 1)**2 + 1
           # [___]  [______________]  [_________________]  [_____________]
           #  |         |                   |                  |
           #  |         |                   |                  ---- bottom left
           #  |         |                   ----bottom right
           #  |         -----top left
           #  |
           #  |
            # ----top right
  print "The sum of the diagonals for a 1001 x 1001 spiral is %s." % total

  # The sum of the diagonals for a 1001 x 1001 spiral is 669171001.
  
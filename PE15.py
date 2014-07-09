"""# Project Euler problem 15
# https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Ideas:
  Start at the bottom right node.
  Go up one node, count the number of paths from that node (1)
  Do the same going left from the bottom right node (1)
  Recursively count the number of paths from each node
  Notice that the number of paths = the sum of the number of paths from each possible next node
  Notice that this looks familiar:
1                            1
2                          1   1
3                        1   2   1
4                      1   3   3   1
5                    1   4   6   4   1 --> 6 paths for 2x2. nth element of the 2nth row (indexed at 0)
6                  1   5  10   10  5   1
7                1   6  15  20   15  6   1  --> 20 paths for 3x3. nth element of the 2nth row (indexed at 0)
                  .
                  .
                  .

So we want the nth element of the 2nth row, for n = 20.

So we want C(2n, n) = C(40, 20) = 137846528820.
"""

if __name__ == "__main__":
  print "There are %s paths for a 20x20 grid." % 137846528820  # :)
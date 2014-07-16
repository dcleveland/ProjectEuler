"""Project Euler problem 39
https://projecteuler.net/problem=39

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?

Solution/noteds:
* Dynamic programming?

"""
from collections import defaultdict
import math


# Brute force :(
if __name__ == "__main__":
  solutions = defaultdict(int)
  for a in range(1, 1000):
    for b in range(1, 1000):
      c = math.sqrt(a**2 + b**2)
      if c.is_integer() and a + b + c <= 1000:
        solutions[int(a + b + c)] += 1

  print ("A perimeter of %s has the most solutions with %s."
    % ([k for k in solutions if solutions[k] == max(solutions.values())][0],
       solutions[k]))

  # A perimeter of 840 has the most solutions with 4.

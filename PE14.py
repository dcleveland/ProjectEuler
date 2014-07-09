"""# Project Euler problem 14
# https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from collections import defaultdict
import sys

def GetNextInSequence(n):
  if n % 2:
    return 3*n + 1
  else:
    return n / 2

def ComputeSequenceLength(n):
  seq = [n]
  if n == 1:
    return
  while seq[-1] > 1:
    next_number = GetNextInSequence(seq[-1])
    seq.append(next_number)
    if computed[next_number]:
      length = len(seq) + computed[next_number]
      computed[n] = length
      break
  if n not in computed:
    computed[n] = len(seq)
    return

if __name__ == "__main__":
  computed = defaultdict(int)
  computed[1] = 1
  for x in range(1, int(1e6)):
    sys.stdout.write("\rx=%s" % x)
    sys.stdout.flush()
    ComputeSequenceLength(x)
  max_len = max(computed.values())
  max_start = [x for x in computed if computed[x] == max_len][0]
  print "\n%s generates the longest sequence (%s values)" % (max_start, max_len)
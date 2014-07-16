"""Project Euler problem 67
https://projecteuler.net/problem=67


By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt a 15K text file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to
try every route to solve this problem, as there are 299 altogether! If you could
check one trillion (1012) routes every second it would take over twenty billion
years to check them all. There is an efficient algorithm to solve it. ;o)"""

import codecs
from collections import defaultdict
import PE18 as pe_fcns

if __name__ == "__main__":
  fh = codecs.open("triangle.txt", "r")
  tree_data = [r.replace("\r\n", "") for r in fh.readlines()]
  dict_tree = dict([(a, [int(x) for x in 
                         tree_data[a - 1].replace("\r\n", "").split(" ")])
                    for a in range(1, len(tree_data) + 1)])
  tree = pe_fcns.BuildTree(dict_tree)
  max_sum = pe_fcns.GetMaxFromNode(tree, len(tree.tree) - 1)
  print "The maximum sum path of the tree in triangles.txt is %s" % max_sum

  # The maximum sum path of the tree in triangles.txt is 7273.
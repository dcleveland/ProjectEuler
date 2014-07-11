"""Project Euler problem 18
https://projecteuler.net/problem=18

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                         75
                        95 64
                      17 47 82
                     18 35 87 10
                    20 04 82 47 65
                  19 01 23 75 03 34
                88 02 77 73 07 63 67
               99 65 04 28 06 16 70 92
             41 41 26 56 83 40 80 70 33
           41 48 72 33 47 32 37 16 94 29
          53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
       91 71 52 38 17 14 91 43 58 50 27 29 48
      63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)"""

from collections import defaultdict
import sys


dict_tree = {
    1: [75],
    2: [95, 64],
    3: [17, 47, 82],
    4: [18, 35, 87, 10],
    5: [20, 04, 82, 47, 65],
    6: [19, 01, 23, 75, 03, 34],
    7: [88, 02, 77, 73, 07, 63, 67],
    8: [99, 65, 04, 28, 06, 16, 70, 92],
    9: [41, 41, 26, 56, 83, 40, 80, 70, 33],
    10: [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    11: [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    12: [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    13: [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    14: [63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    16: [04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]
}


class Tree(object):
  def __init__(self):
    self.root = Node(None)
    self.depth = 0
    self.nodes = []
    self.tree = defaultdict(list)


class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.depth = 0


def InsertNode(tree, node, key):
  if not tree.root.value:
    tree.root = node
    tree.nodes.append(node)
    tree.depth += 1
    tree.tree[tree.depth].append(node)
  elif key < len(tree.nodes):
    # ReplaceNode(tree, node, key)
    pass
  elif key == len(tree.nodes):
    if len(tree.tree[tree.depth]) == tree.depth:
      # new row
      tree.depth += 1
      tree.tree[tree.depth].append(node)
      r_parent = tree.tree[tree.depth - 1][0]
      r_parent.l_child = node
      tree.nodes.append(node)
    else:
      tree.nodes.append(node)
      tree.tree[tree.depth].append(node)
      # Check if last node at this depth
      if len(tree.tree[tree.depth]) == tree.depth:
        # only need left_parent
        l_parent = tree.tree[tree.depth - 1][tree.depth - 2]
        l_parent.r_child = node
      else:
        node_row_index = len(tree.tree[tree.depth]) - 1
        l_parent = tree.tree[tree.depth - 1][node_row_index - 1]
        l_parent.r_child = node
        r_parent = tree.tree[tree.depth - 1][node_row_index]
        r_parent.l_child = node


def BuildTree(nodes):
  tree = Tree()
  index = 0
  for i, n in enumerate(nodes):
    for j, k in enumerate(nodes[n]):
      node = Node(k)
      InsertNode(tree, node, index)
      index += 1
  return tree


def PrintTree(tree):
  """Handy for visualization."""
  output = []
  cols = (max([len(t) for t in tree.tree.values()]) + 1)*4
  offset = cols / 4
  for row in tree.tree:
    vals = [str(n.value) for n in tree.tree[row]]
    clean_vals = []
    for v in vals:
      if len(v) == 1:
        v = "0" + v
      clean_vals.append(v)
    if row % 2:
      output.append("  "*(offset) + "  ".join(clean_vals) + "\n")
    else:
      output.append("  "*(offset) + "  ".join(clean_vals) + "\n")
    offset = offset - 1
  return output

def GetMaxFromNode(tree, row_number):
  # For each value in this row, find it's biggest child node and add that value
  # to this node's value
  for i in range(len(tree.tree[row_number])):
    this_node = tree.tree[row_number][i]
    this_node.value += max(tree.tree[row_number][i].l_child.value,
                           tree.tree[row_number][i].r_child.value)
  if len(tree.tree[row_number]) == 1:
    # We've gotten to the root of the tree, return the updated root value
    return tree.tree[row_number][0].value
  else:
    # Recursively update the values in the row above
    return GetMaxFromNode(tree, row_number -1)

if __name__ == "__main__":
  tree = BuildTree(dict_tree)
  print "Max path sum of the tree \n\n%s" % ("".join(PrintTree(tree)))
  # Start from the second to last row and work our way up recursively
  max_sum = GetMaxFromNode(tree, len(tree.tree) - 1)
  print "\n is %s" % max_sum
  print "Updated tree is:\n\n%s" % "".join(PrintTree(tree))
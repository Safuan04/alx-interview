#!/usr/bin/python3
"""Defining a function pascal_triangle"""


def pascal_triangle(n):
  """This is a function that returns a list of lists of
  integers representing the Pascal's triangle of n"""
  if n <= 0:
    return []

  l = []

  for i in range(n):
    sec_l = []
    if i == 0:
      l.append([1])
    else:
      for j in range(i + 1):
        if j == 0 or j == i:
          sec_l.append(1)
        else:
          value = l[i - 1][j] + l[i - 1][j - 1]
          sec_l.append(value)
      l.append(sec_l)

  return l

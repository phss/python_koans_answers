#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
  if not is_a_triangle(a, b, c):
    raise TriangleError
  elif a == b == c:
    return "equilateral"
  elif a == b or b == c or a == c:
    return "isosceles"
  else:
    return "scalene"

def is_a_triangle(a, b, c):
  if a > b and a > c:
    biggest, smallest_1, smallest_2 = a, b, c
  elif b > c:
    biggest, smallest_1, smallest_2 = b, a, c
  else:
    biggest, smallest_1, smallest_2 = c, a, b

  return smallest_1 + smallest_2 > biggest

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass

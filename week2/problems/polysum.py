"""
A regular polygon has n number of sides. Each side has length s.

    The area of a regular polygon is: 0.25∗𝑛∗𝑠2𝑡𝑎𝑛(𝜋/𝑛)
    The perimeter of a polygon is: length of the boundary of the polygon

Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
"""

import math


def polysum(n: int, s: int) -> float:
  """
  Computes the sum of the area + perimeter squared
  of a regular polygon.

  The area of a regular polygon is : 0.25∗𝑛∗𝑠2𝑡𝑎𝑛(𝜋/𝑛)
  The perimeter of a polygon is    : length of the boundary
                                     of the polygon
  ---------------------------------------------------------
  Input:
  n : int    the number of sides of the polygon
  s : int    the length of each side of the polygon
  ---------------------------------------------------------
  Returns : float
  """

  area = (0.25 * n * s**2)/(math.tan(math.pi/n))
  perimeter = n * s

  return round(area + perimeter**2, 4)

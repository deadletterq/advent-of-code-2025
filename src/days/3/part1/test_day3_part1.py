from unittest import TestCase
from . import solution

class Test(TestCase):
  def test_example(self):
    input = [
      [9,8,7,6,5,4,3,2,1,1,1,1,1,1,1],
      [8,1,1,1,1,1,1,1,1,1,1,1,1,1,9],
      [2,3,4,2,3,4,2,3,4,2,3,4,2,7,8],
      [8,1,8,1,8,1,9,1,1,1,1,2,1,1,1],
    ]
    result = solution(input)
    self.assertEqual(357, result)

  def test_1(self):
    input = [
      [1, 2, 3, 4]
    ]
    result = solution(input)
    self.assertEqual(34, result)


from unittest import TestCase
from . import solution

class Test(TestCase):
  def test_example(self):
    input = [
      "L68",
      "L30",
      "R48",
      "L5",
      "R60",
      "L55",
      "L1",
      "L99",
      "R14",
      "L82",
    ]
    result = solution(input)
    self.assertEqual(result, 3)

  def test_l50(self):
    input = ["L50"]
    result = solution(input)
    self.assertEqual(result, 1)

  def test_r50(self):
    input = ["R50"]
    result = solution(input)
    self.assertEqual(result, 1)

  def test_r49(self):
    input = ["R49"]
    result = solution(input)
    self.assertEqual(result, 0)

  def test_l51(self):
    input = ["L51"]
    result = solution(input)
    self.assertEqual(result, 0)
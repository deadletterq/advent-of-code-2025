from unittest import TestCase
from . import solution

class Test(TestCase):
  def test_example(self):
    input = [
      "L68", # 82, 1
      "L30", # 52, 1
      "R48", # 0, 2
      "L5",  # 95, 2
      "R60",
      "L55",
      "L1",
      "L99",
      "R14",
      "L82",
    ]
    result = solution(input)
    self.assertEqual(6, result)

  def test_l50_drift(self):
    input = ["L1" for _ in range(50)]
    result = solution(input)
    self.assertEqual(1, result)

  def test_r50_drift(self):
    input = ["R1" for _ in range(50)]
    result = solution(input)
    self.assertEqual(1, result)

  def test_l50(self):
    input = ["L50"]
    result = solution(input)
    self.assertEqual(1, result)

  def test_r50(self):
    input = ["R50"]
    result = solution(input)
    self.assertEqual(1, result)

  def test_r51(self):
    input = ["R51"]
    result = solution(input)
    self.assertEqual(1, result)

  def test_r49(self):
    input = ["R49"]
    result = solution(input)
    self.assertEqual(0, result)

  def test_l51(self):
    input = ["L51"]
    result = solution(input)
    self.assertEqual(1, result)

  def test_l49(self):
    input = ["L49"]
    result = solution(input)
    self.assertEqual(0, result)

  def test_R1K(self):
    input = ["R1000"]
    result = solution(input)
    self.assertEqual(10, result)

  def test_L1K(self):
    input = ["L1000"]
    result = solution(input)
    self.assertEqual(10, result)


  def test_complex_l(self):
    input = ["L50", "L1", "R1", "L1", "R1", "R1"]
    result = solution(input)
    self.assertEqual(3, result)


  def test_complex_r(self):
    input = ["R50", "L1", "L99", "L1", "R1", "R1"]
    result = solution(input)
    self.assertEqual(3, result)


  def test_complex_r_2(self):
    input = ["R50", "L1", "L199", "L1", "R1", "R1"]
    result = solution(input)
    self.assertEqual(4, result)
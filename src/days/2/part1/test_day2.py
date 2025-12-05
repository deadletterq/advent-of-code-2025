from unittest import TestCase
from . import solution

class Test(TestCase):
  def test_example(self):
    input = [
      (11, 22),
      (95, 115),
      (998, 1012),
      (1188511880, 1188511890),
      (222220, 222224),
      (1698522, 1698528),
      (446443, 446449),
      (38593856, 38593862),
      (565653, 565659),
      (824824821, 824824827),
      (2121212118, 2121212124),
    ]
    result = solution(input)
    self.assertEqual(1227775554, result)

  def test_1(self):
    input = [
      (11, 12),
    ]
    result = solution(input)
    self.assertEqual(11, result)

  def test_2(self):
    input = [
      (1_000_000_000_1_000_000_000, 1_000_000_000_1_000_000_001),
    ]
    result = solution(input)
    self.assertEqual(1_000_000_000_1_000_000_000, result)

  def test_3(self):
    input = [
      (101, 102),
    ]
    result = solution(input)
    self.assertEqual(0, result)

  def test_4(self):
    input = [
      (123, 124),
    ]
    result = solution(input)
    self.assertEqual(0, result)
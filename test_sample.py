from unittest import TestCase
from sample import add


def test_tekitou():
  a = 1
  b = 1
  assert a == b

class TestAdd(TestCase):
  def test_add_1(self):
    self.assertEqual(1, 1)

  def test_add_2(self):
    self.assertEqual(3, add(1, 2))

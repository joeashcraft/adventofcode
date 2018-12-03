import unittest
from day1 import *

class MyFirstTests(unittest.TestCase):

    def test1(self):
        self.assertEqual(part1([1, 1, 1]), 3)
        self.assertEqual(part1([1, 1, -2]), 0)
        self.assertEqual(part1([-1, -2, -3]), -6)

    def test2(self):
        self.assertEqual(part2([+1, -1]), 0)
        self.assertEqual(part2([+3, +3, +4, -2, -4]), 10)
        self.assertEqual(part2([-6, +3, +8, +5, -6]), 5)
        self.assertEqual(part2([+7, +7, -2, -7, -4]), 14)

if __name__ == '__main__':
    unittest.main()


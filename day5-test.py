import unittest
from day5 import part1
from day5 import part2


class MyFirstTests(unittest.TestCase):
    test_input = 'dabAcCaCBAcCcaDA'

    def test_part1(self):
        self.assertEqual(len(part1(self.test_input)), 10)

    def test_part2(self):
        self.assertEqual(part2(self.test_input), 4)


if __name__ == '__main__':
    unittest.main()

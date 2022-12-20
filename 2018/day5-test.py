import unittest
from day5 import react, part1, part1_test_if_pair
from day5 import part2


class MyFirstTests(unittest.TestCase):
    test_input = 'dabAcCaCBAcCcaDA'

    def test_part1_helpers(self):
        self.assertEqual(part1_test_if_pair('A', 'A'), False)
        self.assertEqual(part1_test_if_pair('A', 'a'), True)
        self.assertEqual(part1_test_if_pair('a', 'A'), True)
        self.assertEqual(part1_test_if_pair('a', 'z'), False)

    def test_part1(self):
        self.assertEqual(len(react("aaaaa")), 5)
        self.assertEqual(len(react("aBcDe")), 5)
        self.assertEqual(len(react("aAbcd")), 3)
        self.assertEqual(len(react(self.test_input)), 10)

    # def test_part2(self):
    #     self.assertEqual(part2(self.test_input), 4)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

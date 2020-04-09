import unittest
from day6 import part1, part1_parse_input, part1_calc_taxi_dist


class MyFirstTests(unittest.TestCase):
    test_input = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""
    my_input = test_input.splitlines()

    def test_part1_helpers(self):
        self.assertEqual(
            part1_parse_input(self.my_input),
            [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)])
        self.assertEqual(
            part1_calc_taxi_dist((-3, 1), (2, 3)),
            7)
        self.assertEqual(
            part1_calc_taxi_dist((1, 1), (1, 4)),
            3)

    def test_part1(self):
        self.assertEqual(part1(self.my_input), 17)

    # def test_part2(self):
    #     self.assertEqual(part2(self.test_input), 4)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

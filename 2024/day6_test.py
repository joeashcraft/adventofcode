#!env python
import unittest
import day6

class MyFirstTests(unittest.TestCase):

    test_input_raw = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...'''
    test_input_parsed = [1000, 2000, 3000, 10000]
    test_input_solution_part1 = 41
    test_input_solution_part2 = 0
    real_solution_part1 = 0
    real_solution_part2 = 0

    test_input_split = test_input_raw.splitlines()

    def test_helpers(self):
        self.assertEqual(day6.parse_input(self.test_input_raw), self.test_input_parsed)


    def test_part1(self):
        self.assertEqual(day6.part1(self.test_input_raw), self.test_input_solution_part1)

    # def test_part1_solved(self):
    #     with open(f"inputs/6", "r") as fh:
    #         puzzle_input = fh.read()
    #     self.assertEqual(day6.part1(puzzle_input), self.real_solution_part1)

    # def test_part2(self):
    #     self.assertEqual(day6.part2(self.test_input_raw), self.test_input_solution_part2)

    # def test_part2_solved(self):
    #     with open(f"inputs/6", "r") as fh:
    #         puzzle_input = fh.read()
    #     self.assertEqual(day6.part2(puzzle_input), self.real_solution_part2)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=True)

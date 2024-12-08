#!env python
import unittest
import day7

class MyFirstTests(unittest.TestCase):

    test_input_raw = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20 '''
    test_input_parsed = [1000, 2000, 3000, 10000]
    test_input_solution_part1 = 3749
    test_input_solution_part2 = 0
    real_solution_part1 = 0
    real_solution_part2 = 0

    test_input_split = test_input_raw.splitlines()

    def test_helpers(self):
        self.assertEqual(day7.parse_input(self.test_input_raw), self.test_input_parsed)


    def test_part1(self):
        self.assertEqual(day7.part1(self.test_input_raw), self.test_input_solution_part1)

    # def test_part1_solved(self):
    #     with open(f"inputs/7", "r") as fh:
    #         puzzle_input = fh.read()
    #     self.assertEqual(day7.part1(puzzle_input), self.real_solution_part1)

    # def test_part2(self):
    #     self.assertEqual(day7.part2(self.test_input_raw), self.test_input_solution_part2)

    # def test_part2_solved(self):
    #     with open(f"inputs/7", "r") as fh:
    #         puzzle_input = fh.read()
    #     self.assertEqual(day7.part2(puzzle_input), self.real_solution_part2)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=True)

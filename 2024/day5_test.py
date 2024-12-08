#!env python
import unittest
import day5


class MyFirstTests(unittest.TestCase):

    test_input_raw = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
    test_input_parsed = [1000, 2000, 3000, 10000]
    test_input_solution_part1 = 143
    test_input_solution_part2 = 0
    real_solution_part1 = 0
    real_solution_part2 = 0

    test_input_split = test_input_raw.splitlines()

    def test_helpers(self):
        self.assertEqual(day5.parse_input(self.test_input_raw), self.test_input_parsed)

    def test_part1(self):
        self.assertEqual(
            day5.part1(self.test_input_raw), self.test_input_solution_part1
        )

    # def test_part1_solved(self):
    #     with open("inputs/05", "r") as fh:
    #         puzzle_input = fh.read()
    #     self.assertEqual(day5.part1(puzzle_input), self.real_solution_part1)

    # def test_part2(self):
    #     self.assertEqual(day5.part2(self.test_input_raw), self.test_input_solution_part2)

    # def test_part2_solved(self):
    #     with open("inputs/05", "r") as fh:
    #         puzzle_input = fh.read()
    #     self.assertEqual(day5.part2(puzzle_input), self.real_solution_part2)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=True)

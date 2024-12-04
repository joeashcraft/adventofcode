#!env python
import unittest
import day2


class MyFirstTests(unittest.TestCase):

    test_input_raw = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    test_input_parsed = (
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    )
    test_input_safe = (True, False, False, False, False, True)
    test_input_mostly_safe = (True, False, False, True, True, True)
    test_input_solution_part1 = 2
    test_input_solution_part2 = 4
    real_solution_part1 = 242
    real_solution_part2 = 311

    test_input_split = test_input_raw.splitlines()

    def test_helpers(self):
        self.assertEqual(
            day2.parse_input(self.test_input_split), self.test_input_parsed
        )
        self.assertEqual(
            day2.is_safe_report(self.test_input_parsed), self.test_input_safe
        )
        self.assertEqual(
            day2.mostly_safe_reports(self.test_input_parsed),
            self.test_input_mostly_safe,
        )
        for ii, report in enumerate(self.test_input_parsed):
            # compare test_input_parsed with test_input_mostly_safe
            self.assertEqual(
                day2.is_mostly_safe_report(report), self.test_input_mostly_safe[ii]
            )

    def test_part1(self):
        self.assertEqual(
            day2.part1(self.test_input_raw), self.test_input_solution_part1
        )

    def test_part1_solved(self):
        with open(f"inputs/02", "r") as fh:
            puzzle_input = fh.read()
        self.assertEqual(day2.part1(puzzle_input), self.real_solution_part1)

    def test_part2(self):
        self.assertEqual(
            day2.part2(self.test_input_raw), self.test_input_solution_part2
        )

    def test_part2_solved(self):
        with open(f"inputs/02", "r") as fh:
            puzzle_input = fh.read()
        self.assertEqual(day2.part2(puzzle_input), self.real_solution_part2)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=True)

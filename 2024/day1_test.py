#!env python
import unittest
import day1


class MyFirstTests(unittest.TestCase):

    test_input_raw = """1000
2000
3000

10000"""
    test_input_solution_part1 = 142
    test_input_solution_part2 = 199

    test_input_split = test_input_raw.splitlines()

    # def test_helpers(self):
    #     self.assertEqual(
    #         6000,
    #         day1.totals(self.test_input_split)[0],
    #     )
    #     self.assertEqual(len(day1.totals(self.test_input_split)), 5)

    def test_part1(self):
        self.assertEqual(
            day1.part1(self.test_input_raw), self.test_input_solution_part1
        )

    # def test_part1_solved(self):
    #     with open(f"day1-input.txt", "r") as fh:
    #         puzzle_input = fh.read()
    #     self.assertEqual(day1.part1(puzzle_input), 1743217)

    def test_part2(self):
        self.assertEqual(
            day1.part2(self.test_input_raw), self.test_input_solution_part2
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=True)

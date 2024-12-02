#!env python
import unittest
import day1


class MyFirstTests(unittest.TestCase):

    test_input_raw = """3   4
4   3
2   5
1   3
3   9
3   3"""
    test_input_parsed = ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
    test_input_sorted = ((1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 9))
    test_input_solution_part1 = 11
    test_input_solution_part2 = 199

    test_input_split = test_input_raw.splitlines()

    def test_helpers(self):
        self.assertEqual(
            day1.parse_input(self.test_input_split), self.test_input_parsed
        )
        self.assertEqual(
            day1.sort_pairs(self.test_input_parsed), self.test_input_sorted
        )
        # self.assertEqual(len(day1.calc_distances(self.test_input_split)), 5)

    def test_part1(self):
        self.assertEqual(
            day1.part1(self.test_input_raw), self.test_input_solution_part1
        )

    def test_part1_solved(self):
        with open(f"inputs/01", "r") as fh:
            puzzle_input = fh.read()
        self.assertEqual(day1.part1(puzzle_input), 2057374)

    # def test_part2(self):
    #     self.assertEqual(
    #         day1.part2(self.test_input_raw), self.test_input_solution_part2
    #     )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=True)

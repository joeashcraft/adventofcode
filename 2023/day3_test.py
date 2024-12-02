import unittest
import day3


class MyFirstTests(unittest.TestCase):
    test_input_raw = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    test_input_solution_part1 = 4361
    # test_input_solution_part2 = 199

    test_input_split = test_input_raw.splitlines()

    # def test_helpers(self):
    #     self.assertEqual(
    #         6000,
    #         day3.totals(self.test_input_split)[0],
    #     )
    #     self.assertEqual(len(day3.totals(self.test_input_split)), 5)

    def test_part1(self):
        self.assertEqual(
            day3.part1(self.test_input_raw), self.test_input_solution_part1
        )

    # def test_part1_solved(self):
    #     with open(f"day3-input.txt", "r") as fh:
    #         puzzle_input = fh.read()
    #     self.assertEqual(day3.part1(puzzle_input), 1743217)

    # def test_part2(self):
    #     self.assertEqual(
    #         day3.part2(self.test_input_raw), self.test_input_solution_part2
    #     )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)

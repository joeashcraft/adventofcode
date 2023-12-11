import unittest
import day9


class MyFirstTests(unittest.TestCase):

    test_input_raw = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
    test_input_split = test_input_raw.splitlines()

    # def test_helpers(self):
    #     self.assertEqual(
    #         6000,
    #         day9.totals(self.test_input_split)[0],
    #     )
    #     self.assertEqual(len(day9.totals(self.test_input_split)), 5)

    def test_part1(self):
        self.assertEqual(day9.part1(self.test_input_raw), 13)

    # def test_part1_solved(self):
    #     with open(f"day9-input.txt", "r") as fh:
    #         puzzle_input = fh.read()
    #     self.assertEqual(day9.part1(puzzle_input), 1743217)

    # def test_part2(self):
    #     self.assertEqual(day9.part2(self.test_input_raw), 45000)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)

#!env python
import unittest
import day3


class MyFirstTests(unittest.TestCase):

    test_input_raw = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+
        mul(32,64]then(mul(11,8)mul(8,5))"""
    test_input_parsed = ((2, 4), (5, 5), (11, 8), (8, 5))
    test_input_solution_part1 = 161
    test_input_solution_part2 = 48
    real_solution_part1 = 167090022
    real_solution_part2 = 0

    test_input_split = test_input_raw.splitlines()

    def test_helpers(self):
        self.assertEqual(day3.parse_input(self.test_input_raw), self.test_input_parsed)
        self.assertEqual(list(day3.flatten(([1, 2], [3, 4]))), [1, 2, 3, 4])
        self.assertEqual(day3.cast_ints(["1", "2"]), [1, 2])
        self.assertEqual(day3.cast_ints(("1", "2")), (1, 2))

    def test_part1(self):
        self.assertEqual(
            day3.part1(self.test_input_raw), self.test_input_solution_part1
        )

    def test_part1_solved(self):
        with open(f"inputs/03", "r") as fh:
            puzzle_input = fh.read()
        self.assertEqual(day3.part1(puzzle_input), self.real_solution_part1)

    def test_part2(self):
        self.assertEqual(
            day3.part2(self.test_input_raw), self.test_input_solution_part2
        )

    # def test_part2_solved(self):
    #     with open(f"inputs/03", "r") as fh:
    #         puzzle_input = fh.read()
    #     self.assertEqual(day3.part2(puzzle_input), self.real_solution_part2)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=True)

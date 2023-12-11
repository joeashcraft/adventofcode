#!/usr/bin/env python
import logging
import unittest
import day8


class MyFirstTests(unittest.TestCase):
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)

    test_input_raw = """30373
25512
65332
33549
35390"""
    test_input_visible_one_row = [1, 0, 0, 1, 0]
    test_input_visible_map = [
        # fmt: off
        [1,1,1,1,1],
        [1,1,1,0,1],
        [1,1,0,1,1],
        [1,0,1,0,1],
        [1,1,1,1,1]
    ]
    # fmt: on
    test_input_split = test_input_raw.splitlines()

    def test_helpers(self):
        # self.assertEqual(
        #     16,
        #     day8.count_perimeter_trees(self.test_input_split),
        # )
        self.assertEqual(
            self.test_input_visible_one_row,
            day8.map_visible_trees(self.test_input_split[0]),
        )

    def test_part1(self):
        self.assertEqual(day8.part1(self.test_input_raw), 21)

    def test_part1_solved(self):
        with open(f"day8-input.txt", "r") as fh:
            puzzle_input = fh.read()
        self.assertEqual(day8.part1(puzzle_input), 1789)

    def test_part1_np(self):
        self.assertEqual(day8.part1_np(self.test_input_raw), 21)
        with open(f"day8-input.txt", "r") as fh:
            puzzle_input = fh.read()
        self.assertEqual(day8.part1_np(puzzle_input), 1789)

    def test_part2(self):
        self.assertEqual(day8.part2(self.test_input_raw), 8)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)

import logging
import unittest
import day2

logger = logging.getLogger()
logger.level = logging.DEBUG


class MyFirstTests(unittest.TestCase):
    test_input_raw = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    test_part1_constraint = {"red": 12, "green": 13, "blue": 14}
    test_input_solution_part1 = 8
    test_input_solution_part2 = 199

    test_solution_part1_helper = {
        1: ({"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2})
    }
    test_part1_hand = {"blue": 3, "red": 4}

    test_input_split = test_input_raw.splitlines()
    # breakpoint()

    def test_helpers(self):
        self.assertDictEqual(
            day2.part1_line_to_game(self.test_input_split[0]),
            self.test_solution_part1_helper,
        )
        self.assertEqual(
            day2.hand_is_possible(self.test_part1_hand, self.test_part1_constraint),
            True,
        )
        self.assertEqual(
            day2.hand_is_possible(self.test_part1_hand, {"red": 12, "green": 13}),
            False,
        )

    def test_part1(self):
        self.assertEqual(
            day2.part1(self.test_input_raw), self.test_input_solution_part1
        )

    # def test_part1_solved(self):
    #     with open(f"day2-input.txt", "r") as fh:
    #         puzzle_input = fh.read()
    #     self.assertEqual(day2.part1(puzzle_input), 1743217)

    # def test_part2(self):
    #     self.assertEqual(
    #         day2.part2(self.test_input_raw), self.test_input_solution_part2
    #     )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)

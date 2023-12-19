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
    test_input_solution_part2 = 2286

    test_solution_part1_helper = {
        1: ({"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}),
        2: (
            {"blue": 1, "green": 2},
            {"green": 3, "blue": 4, "red": 1},
            {"green": 1, "blue": 1},
        ),
        3: (
            {"green": 8, "blue": 6, "red": 20},
            {"blue": 5, "red": 4, "green": 13},
            {"green": 5, "red": 1},
        ),
        4: (
            {"green": 1, "red": 3, "blue": 6},
            {"green": 3, "red": 6},
            {"green": 3, "blue": 15, "red": 14},
        ),
        5: ({"red": 6, "blue": 1, "green": 3}, {"blue": 2, "red": 1, "green": 2}),
    }
    test_part1_hand = {"blue": 3, "red": 4}

    test_part2_minimal_hands = {
        1: {"red": 4, "green": 2, "blue": 6},
        2: {"red": 1, "green": 3, "blue": 4},
        3: {"red": 20, "green": 13, "blue": 6},
        4: {"red": 14, "green": 3, "blue": 15},
        5: {"red": 6, "green": 3, "blue": 2},
    }
    test_part2_powers = {1: 48, 2: 12, 3: 1560, 4: 630, 5: 36}

    test_input_split = test_input_raw.splitlines()
    # breakpoint()

    def test_part1_helpers(self):
        self.assertDictEqual(
            day2.part1_line_to_game(self.test_input_split[0])[1][0],  # TODO for loop
            self.test_solution_part1_helper[1][0],
        )
        self.assertTrue(
            day2.hand_is_possible(self.test_part1_hand, self.test_part1_constraint)
        )
        self.assertFalse(
            day2.hand_is_possible(self.test_part1_hand, {"red": 12, "green": 13})
        )

    def test_part1(self):
        self.assertEqual(
            day2.part1(self.test_input_raw), self.test_input_solution_part1
        )

    def test_part2_helpers(self):
        for game_id, hands in self.test_solution_part1_helper.items():
            self.assertEqual(
                day2.minimal_hand(hands),
                self.test_part2_minimal_hands[game_id],
            )
        for game_id, min_hand in self.test_part2_minimal_hands.items():
            self.assertEqual(
                day2.cubes_powers(min_hand), self.test_part2_powers[game_id]
            )

    def test_part2(self):
        self.assertEqual(
            day2.part2(self.test_input_raw), self.test_input_solution_part2
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)

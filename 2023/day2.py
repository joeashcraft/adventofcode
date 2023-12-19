#!env python
"""Day 2: Cube Conundrum

https://adventofcode.com/2023/day/2
"""

import logging

DAY = 2


# def part1_helper(line: str) -> int:
#     _func = "part1_helper"
#     logging.debug(f"{_func}(got {len(_input)} lines)")
#     logging.info(f'{_func}() returns {result}')
#     pass


def game_is_possible(hands: tuple, constraints: dict) -> bool:
    """Return true if all hands are possible given constraints."""
    _func = "game_is_possible"
    logging.debug(f"{_func}(hands={hands}, constraints={constraints})")

    for hand in hands:
        # consider constraints.
        # if any hand breaks constraints, the whole game is IMPOSSIBLE
        # or, if no hands break constraint, then add the Game ID to total
        if not hand_is_possible(hand, constraints):
            return False
    return True


def hand_is_possible(hand: dict, constraints: dict):
    """Return true if the hand is possible given constraints."""

    _func = "hand_is_possible"
    logging.debug(f"{_func}(hand={hand}, constraints={constraints})")
    # e.g. hand_is_possible(hand={'red': 6, 'blue': 1, 'green': 3}, constraints={'red': 12, 'green': 13, 'blue': 14})

    for color, count in hand.items():
        # assert the different colors in hand are subset of colors in constraints
        try:
            constraints[color]
        except KeyError as e:
            return False

    # assert the number of each color in hand is <= colors in constraints
    for color, count in hand.items():
        if not constraints[color] >= count:
            return False
    return True


def part1_line_to_game(line: str) -> dict:
    """Parse a single line of PUZZLE INPUT, and
    return a dict like
        { 1: ({"blue": 3, "red": 4}, {"red": 1, "green": 2, "blue": 6}, {"green": 2}) }
    """
    _func = "part1_line_to_game"
    logging.debug(f"{_func}(got {len(line)} lines)")
    result = dict()

    left, right = line.split(":")
    logging.debug(f"  left: {left}; right: {right}")

    game_id = int(left.split()[1])
    result[game_id] = list()
    logging.debug(f"  game_id: {game_id}")
    logging.debug(f"  result: {result}")

    hands = right.split(";")
    # [' 3 blue, 4 red', ' 1 red, 2 green, 6 blue', ' 2 green']
    logging.debug(f"  hands: {hands}")  # list of strings
    # foreach hand
    for hand in hands:
        # ' 3 blue, 4 red'
        _hand = hand.strip().replace(", ", ",").split(",")
        # ['3 blue', '4 red']
        logging.debug(f"    {_hand}")
        __hand = {}
        for h in _hand:
            # '3 blue'
            count = int(h.split()[0])
            color = h.split()[1]
            __hand[color] = count
            # { 'blue': 3 }
        logging.debug(f"    {__hand}")
        result[game_id].append(__hand)

    # turn the list to a tuple
    result[game_id] = tuple(result[game_id])
    logging.info(f"{_func}() returns {result}")
    return result


def part1(puzzle_input):
    """Determine which games would have been possible if the bag had been loaded
    with only 12 red cubes, 13 green cubes, and 14 blue cubes.

    What is the sum of the IDs of those games?
    """
    _func = "part1"
    _input = puzzle_input.splitlines()
    logging.info(f"{_func}(got {len(_input)} lines)")

    my_sum = 0
    my_constraint = {"red": 12, "green": 13, "blue": 14}

    games = dict()
    for game in _input:
        _game = part1_line_to_game(game)
        for k, v in _game.items():
            games[k] = v
            logging.debug(f"  games: {games}")

    possible_games = []
    # foreach game
    for game_id, hands in games.items():
        if game_is_possible(hands, my_constraint):
            possible_games.append(game_id)
            logging.debug(f"possible_games={possible_games}")

    logging.info(f"possible_games={possible_games}")
    return sum(possible_games)


def minimal_hand(hands: iter) -> dict:
    _func = "minimal_hand"
    logging.debug(f"{_func}(hands({len(hands)})={hands})")

    smallest_hand = {"red": 0, "green": 0, "blue": 0}
    min_hand = smallest_hand.copy()

    # foreach game
    for hand in hands:
        # foreach hand
        logging.debug(f"    hand={hand}")
        for color, count in hand.items():
            if count > min_hand[color]:
                min_hand[color] = count
                logging.debug(f"      min_hand=={min_hand}")

    logging.info(f"{_func}() returns {min_hand}")
    return min_hand


def cubes_powers(hand: dict) -> int:
    _func = "cubes_powers"
    logging.debug(f"{_func}(hand={hand})")

    power = 1
    for count in hand.values():
        power = power * count
        # logging.debug(f"{_func} power=={power}")

    logging.info(f"{_func}() returns {power}")
    return power


def part2(puzzle_input):
    """For each game, find the minimum set of cubes that must have been present.

    What is the sum of the power of these sets?
    """
    _func = "part2"
    _input = puzzle_input.splitlines()
    logging.info(f"{_func}() got {len(_input)} lines")

    games = dict()
    for game in _input:
        _game = part1_line_to_game(game)
        for k, v in _game.items():
            games[k] = v
            # {1: ({'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}), ...}

    powers = []
    for game_id, hands in games.items():
        # foreach game, find the minimal set of cubes
        logging.debug(f"  game={game_id}, hands={hands}")
        min_hand = minimal_hand(hands)
        # calc the power of the minmal set, and keep track
        powers.append(cubes_powers(min_hand))
        logging.debug(f"  powers=={powers}")

    return sum(powers)


if __name__ == "__main__":
    from os import getenv

    if getenv("DEBUG"):
        logging.basicConfig(level=logging.DEBUG)
        from day2_test import MyFirstTests

        puzzle_input = MyFirstTests.test_input_raw
    else:
        logging.basicConfig(level=logging.INFO)
        with open(f"day{DAY}_input.txt", "r") as fh:
            puzzle_input = fh.read()

    logging.info(f"main() got {len(puzzle_input)} bytes")

    if getenv("PART") == "1":
        print(f"PART 1: {part1(puzzle_input)}")
    elif getenv("PART") == "2":
        print(f"PART 2: {part2(puzzle_input)}")
    else:
        print(f"PART 1: {part1(puzzle_input)}")
        print(f"PART 2: {part2(puzzle_input)}")

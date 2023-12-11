#!env python
"""Day 6: Tuning Trouble

https://adventofcode.com/2022/day/6
"""

import logging

DAY = 6


def part1(puzzle_input):
    """How many characters need to be processed before the first start-of-packet marker is detected?"""
    _func = "part1"
    _input = str(puzzle_input.splitlines()[0])
    logging.info(f"{_func}(got {len(_input)} characters)")

    for ii, character in enumerate(_input):
        # logging.debug(
        #     f"{_func}(): ii={ii}, character={character}, slice={_input[ii:ii+4]}"
        # )
        slice = _input[ii : ii + 4]
        my_set = set(slice)
        if len(my_set) == 4:
            return ii + 4


def part2(puzzle_input):
    """How many characters need to be processed before the first start-of-message marker is detected?"""
    _func = "part2"
    _input = str(puzzle_input.splitlines()[0])
    logging.info(f"{_func}(got {len(_input)} characters)")

    for ii, character in enumerate(_input):
        logging.debug(
            f"{_func}(): ii={ii}, character={character}, slice={_input[ii:ii+14]}"
        )
        slice = _input[ii : ii + 14]
        my_set = set(slice)
        if len(my_set) == 14:
            return ii + 14


if __name__ == "__main__":
    from os import getenv

    if getenv("DEBUG"):
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    with open(f"day{DAY}-input.txt", "r") as fh:
        puzzle_input = fh.read()

    logging.info(f"read in {len(puzzle_input)} characters")

    print(f"PART 1: {part1(puzzle_input)}")
    print(f"PART 2: {part2(puzzle_input)}")

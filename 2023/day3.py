#!env python
"""Day 3: Gear Ratios

https://adventofcode.com/2023/day/3
"""

import logging
import numpy as np
import re
from string import punctuation

DAY = 3


# def part1_helper(line: str) -> int:
#     _func = "part1_helper"
#     logging.debug(f"{_func}(got {len(_input)} lines)")
#
#     logging.info(f"{_func}() returns {result})")
#     pass


def part1(puzzle_input):
    """What is the sum of all of the part numbers in the engine schematic?"""
    _func = "part1"
    _input = puzzle_input.splitlines()
    logging.debug(f"{_func}(got {len(_input)} lines)")

    _puzzle = np.array(_input)
    # logging.debug(f"  _puzzle=={_puzzle[0][0:2]}")
    breakpoint()

    symbols = "".join([x for x in punctuation if x is not "."])
    logging.debug(f"  symbols=={symbols}")

    result = int()

    logging.info(f"{_func}() returns {result})")
    return result


# def part2_helper(line: str) -> int:
#     _func = "part2_helper"
#     logging.debug(f"{_func}(got {len(_input)} lines)")
#
#     logging.info(f"{_func}() returns {result})")
#     pass


def part2(puzzle_input):
    _func = "part2"
    _input = puzzle_input.splitlines()
    logging.debug(f"{_func}(got {len(_input)} lines)")

    logging.info(f"{_func}() returns {result})")
    pass


if __name__ == "__main__":
    from os import getenv

    if getenv("DEBUG"):
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    with open(f"day{DAY}_input.txt", "r") as fh:
        puzzle_input = fh.read()

    logging.info(f"main(): read in {len(puzzle_input)} chars")

    if getenv("PART") == "1":
        print(f"PART 1: {part1(puzzle_input)}")
    elif getenv("PART") == "2":
        print(f"PART 2: {part2(puzzle_input)}")
    else:
        print(f"PART 1: {part1(puzzle_input)}")
        print(f"PART 2: {part2(puzzle_input)}")

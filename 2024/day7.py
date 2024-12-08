#!env python
"""Day 7: Bridge Repair

https://adventofcode.com/2024/day/7
"""

import logzero
from logzero import logger as logging
from utils.api import get_input

DAY = 7


def parse_input(line: str) -> tuple:
    _func = "parse_input"
    _input = line
    logzero.loglevel(logzero.DEBUG)
    logging.info(f"{_func}(got {len(_input)} lines)")
    logging.debug(f"{_func}(line={_input[:5]}...)")

    result = []
    logging.info(f"{_func}() returns {result[:5]}...")
    return tuple(result)

# def part1_helper(line: str) -> int:
#     _func = "part1_helper"
#     _input = line
#     logzero.loglevel(logzero.DEBUG)
#     logging.info(f"{_func}(got {len(_input)} lines)")
#     logging.debug(f"{_func}(line={_input[:5]}...)")
#
#     result = ''
#     logging.info(f"{_func}() returns {result[:5]}...")
#     return result



def part1(puzzle_input) -> int:
    """Determine which equations could possibly be true.

    What is their total calibration result?
    """
    _func = "part1"
    _input = puzzle_input.splitlines()
    logzero.loglevel(logzero.INFO)
    logging.info(f"{_func}(got {len(_input)} lines)")

    result = 0
    logging.info(f"{_func}() returns {result[:5]}...")
    return result


# def part2_helper(line: str) -> int:
#     _func = "part2_helper"
#     _input = line
#     logzero.loglevel(logzero.DEBUG)
#     logging.info(f"{_func}(got {len(_input)} lines)")
#     logging.debug(f"{_func}(line={_input[:5]}...)")
#
#     result = ''
#     logging.info(f"{_func}() returns {result[:5]}...")
#     return result


def part2(puzzle_input) -> int:
    _func = "part2"
    _input = puzzle_input.splitlines()
    logzero.loglevel(logzero.INFO)
    logging.debug(f"{_func}(got {len(_input)} lines)")

    result = 0
    logging.info(f"{_func}() returns {result[:5]}...")
    return result


if __name__ == "__main__":
    from os import getenv

    if getenv("DEBUG"):
        logzero.loglevel(logzero.DEBUG)
    else:
        logzero.loglevel(logzero.INFO)

    puzzle_input = get_input(DAY)

    logging.info(f"read in {len(puzzle_input)} lines")

    if getenv("PART") == "1":
        print(f"PART 1: {part1(puzzle_input)}")
    elif getenv("PART") == "2":
        print(f"PART 2: {part2(puzzle_input)}")
    else:
        print(f"PART 1: {part1(puzzle_input)}")
        print(f"PART 2: {part2(puzzle_input)}")

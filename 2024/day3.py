#!env python
"""Day 3: Mull It Over

https://adventofcode.com/2024/day/3
"""

import logzero
from logzero import logger as logging
from utils.api import get_input
from typing import Iterable
from itertools import chain


DAY = 3


def parse_input(line: str) -> tuple:
    """Returns tuple of tuples, each with 2 integers."""
    _func = "parse_input"
    _input = line
    logzero.loglevel(logzero.INFO)
    logging.info(f"{_func}(got {len(_input)} characters)")
    logging.debug(f"{_func}(line={_input[:15]}...)")

    import re

    # p = re.compile("mul\((\d{1,3}),(\d{1,3})\)")
    p = re.compile("(?<=mul\()(\d{1,3}),(\d{1,3})(?=\))")
    # matches: list = p.findall(_input)
    # [m.groups() for m in p.finditer(test_input_raw)]
    # logging.debug(f"matches={list(matches)[:5]}, ...")

    # _int_matches = []
    # for x, y in matches:
    #     _int_matches.append((int(x), int(y)))
    #     logging.debug(f"  int_matches={list(_int_matches)[:5]}, ...")
    # _int_matches = [(int(x), int(y)) for (x, y) in matches]

    # matches = [
    #     (int(x), int(y)) for (x, y) in list(p.findall(_input))
    # ]  # DONE refactor without for-loop
    matches = map(cast_ints, p.findall(_input))
    logging.debug(f"  matches is {type(matches)}")
    result = tuple(matches)
    logging.info(f"{_func}() returns a {type(result)} with {result[:5]},...")
    return result


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
def cast_ints(_input: Iterable) -> Iterable:
    """Returns same Type of Iterable as arguement, and turns each item to Integer."""
    _func = "cast_ints"
    # _input = line
    logzero.loglevel(logzero.INFO)
    try:
        logging.info(f"{_func}(len(_input)=={len(_input)})")
        logging.debug(f"{_func}(_input={_input[:5]}...)")
    except TypeError:
        logging.info(f"{_func}(_input is {type(_input)})")

    result = type(_input)(map(int, _input))
    try:
        logging.info(f"{_func}() returns {type(result)} {result[:5]}, ...")
    except TypeError:
        logging.info(f"{_func}() returns a {type(result)}")
    return result


def flatten(_input: Iterable) -> list:
    _func = "flatten"
    # _input = line
    logzero.loglevel(logzero.INFO)
    try:
        logging.info(f"{_func}(got {len(_input)} items to flatten)")
    except TypeError:
        logging.info(f"{_func}(got {type(_input)})")

    # logging.debug(f"{_func}(line={_input[:5]}...)")

    # result = [y for x in _input for y in x]
    result = chain.from_iterable(_input)
    logging.info(f"{_func}() returns {type(result)}...")
    return result


def part1(puzzle_input) -> int:
    """Scan the corrupted memory for uncorrupted mul instructions.

    What do you get if you add up all of the results of the multiplications?"""
    _func = "part1"
    _input = puzzle_input.splitlines()
    logzero.loglevel(logzero.INFO)
    logging.info(f"{_func}(got {len(_input)} lines)")

    # parse input
    from os import getenv
    from functools import reduce

    parsed = map(
        parse_input, _input
    )  # returns Iterator of tuples (one per _input line) of tuples (one per pattern match) of ints
    flat_parsed = flatten(parsed)  # returns flattened Iterable

    # if getenv("DEBUG"):
    #     # parsed = list(parse_input(line) for line in _input)
    #     # parsed = []
    #     # for line in _input:
    #     #     logging.debug(f"  line={line}")
    #     #     for x in parse_input(line):
    #     #         parsed.append(x)
    #     parsed = list(pair for line in _input for pair in parse_input(line))
    #     logging.debug(f"  parsed {type(parsed)} ({len(parsed)}) = {parsed[:3]}, ...")
    # else:
    #     parsed = (pair for line in _input for pair in parse_input(line))
    #     logging.debug(f"  parsed is {type(parsed)}")

    # mutiply pairs
    import math

    if getenv("DEBUG"):
        # products = list(math.prod(pair) for pair in flat_parsed)
        products = list(map(math.prod, flat_parsed))
        logging.debug(
            f"  products {type(products)} ({len(products)}) = {products[:3]}, ..."
        )
    else:
        products = map(math.prod, flat_parsed)
        # products: tuple = (
        # math.prod(pair) for pair in flat_parsed
        # )  # DONE refactor without for-loop
        logging.debug(f"  products is {type(products)}")

    # return sum
    result = sum(products)
    logging.info(f"{_func}() returns {result}...")
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
    """Handle the new instructions; what do you get if you add up all of the
    results of just the enabled multiplications?"""
    _func = "part2"
    _input = puzzle_input.splitlines()
    logzero.loglevel(logzero.INFO)
    logging.debug(f"{_func}(got {len(_input)} lines)")

    result = 0
    logging.info(f"{_func}() returns {result}...")
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

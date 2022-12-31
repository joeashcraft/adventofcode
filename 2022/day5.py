#!env python
"""Day 5: Supply Stacks

https://adventofcode.com/2022/day/5
"""

import logging
import re
from pprint import pprint
import copy

DAY = 5

STARTING = [
    ["Z", "J", "N", "W", "P", "S"],
    ["G", "S", "T"],
    ["V", "Q", "R", "L", "H"],
    ["V", "S", "T", "D"],
    ["Q", "Z", "T", "D", "B", "M", "J"],  # 5
    ["M", "W", "T", "J", "D", "C", "Z", "L"],
    ["L", "P", "M", "W", "G", "T", "J"],
    ["N", "G", "M", "T", "B", "F", "Q", "H"],
    ["R", "D", "G", "C", "P", "B", "Q", "W"],  # 9
]


def split_puzzle_input(lines_input: list) -> list:
    """split the puzzle input STARTING and INSTRUCTIONS.

    RETURNS (list) a line of 2 lists
    """
    _func = "split_puzzle_input"
    logging.info(f"{_func}(lines_input[{len(lines_input)}])")
    # read lines until empty line, split at that point
    starting = list()
    _instructions = list()

    while lines_input:
        line = lines_input.pop(0)
        if line != "":
            starting.append(line)
            # logging.debug(f"{_func}(): found a starting position")
        else:
            logging.info(f"{_func}(): found {len(starting)} starting positions")
            _instructions = lines_input.copy()
            logging.info(f"{_func}(): found {len(_instructions)} instructions")
            break

    # parse starting positions

    # parse instructions
    instructions = list()
    for line in _instructions:
        step = {
            "count": int(re.split(r" ", line)[1]),
            "from": int(re.split(r" ", line)[3]),
            "to": int(re.split(r" ", line)[5]),
        }
        instructions.append(step)
        # logging.debug(step)

    starting = copy.deepcopy(STARTING)  # cheat!
    logging.info(
        f"{_func}(): returns {len(starting)} starting positions and {len(instructions)} instructions"
    )
    return [starting, instructions]


def part1(puzzle_input):
    """After the rearrangement procedure completes, what crate ends up on top of each stack?

    RETURN (str) the crates on top of stacks, in stack order
    """
    _func = "part1"
    _input = puzzle_input.splitlines()
    logging.info(f"{_func}()")

    # separate puzzle input to starting position and instructions
    starting, instructions = split_puzzle_input(_input)

    # do moves
    working = copy.deepcopy(starting)
    for step in instructions:
        logging.debug(step)
        try:
            for count in range(step["count"]):
                working[step["to"] - 1].append(working[step["from"] - 1].pop())
        except IndexError as e:
            print(e)
            pprint(working)
            breakpoint()

    return "".join([stack[-1] for stack in working])


def part2(puzzle_input):
    """After the rearrangement procedure completes, what crate ends up on top of each stack?"""
    _func = "part2"
    _input = puzzle_input.splitlines()
    logging.info(f"{_func}()")

    starting, instructions = split_puzzle_input(_input)

    # do moves
    working = copy.deepcopy(starting)
    for step in instructions:
        logging.debug(step)
        try:
            my_length = len(working[step["to"] - 1])
            for count in range(step["count"]):
                working[step["to"] - 1].insert(
                    my_length, working[step["from"] - 1].pop()
                )
        except IndexError as e:
            print(e)
            pprint(working)
            breakpoint()

    return "".join([stack[-1] for stack in working])


if __name__ == "__main__":
    from os import getenv

    if getenv("DEBUG"):
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    with open(f"day{DAY}-input.txt", "r") as fh:
        puzzle_input_raw = fh.read()

    logging.info(f"read in {len(puzzle_input_raw)} lines")

    print(f"PART 1: top of stacks are: {part1(puzzle_input_raw)}")
    print(f"PART 2: top of stacks are: {part2(puzzle_input_raw)}")

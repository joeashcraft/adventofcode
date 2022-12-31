#!env python
"""Day 3: Rucksack Reorganization

https://adventofcode.com/2022/day/3
"""

import logging
from string import ascii_letters

DAY = 3

PRIORITIES = dict()
for i, v in enumerate(ascii_letters):
    PRIORITIES[v] = i + 1


def find_the_duplicate(rucksack: str) -> str:
    FUNC = "find_the_duplicate"
    my_length = len(rucksack)
    logging.debug(f"{FUNC}(rucksack: {rucksack})")
    left = rucksack[: my_length // 2]
    right = rucksack[my_length // 2 :]
    logging.debug(f"{FUNC}(): {left} <--> {right}")

    for c in left:
        if c in right:
            logging.debug(f"{FUNC}(): found duplicate {c}")
            return c


def find_the_badge(a, b, c):
    FUNC = "find_the_badge"
    logging.log(9, f"{FUNC}(a={a}, b={b}, c={c}")
    for item in a:
        if item in b and item in c:
            logging.debug(f"{FUNC}(): returns {item}")
            return item


def part1(puzzle_input):
    """Find the item type that appears in both compartments of each rucksack.

    What is the sum of the priorities of those item types?"""
    FUNC = "part1"
    _input = puzzle_input.splitlines()
    my_sum = 0

    for rucksack in _input:
        dupe = find_the_duplicate(rucksack)
        my_sum += PRIORITIES[dupe]
        logging.debug(f"{FUNC}(): duplicate {dupe} has priority {PRIORITIES[dupe]}")

    return my_sum


def part2(puzzle_input):
    """Find the item type that corresponds to the badges of each three-Elf group.

    What is the sum of the priorities of those item types?"""
    FUNC = "part2"
    from collections import deque

    _input = deque(puzzle_input.splitlines())
    my_sum = 0

    while _input:
        a, b, c = _input.popleft(), _input.popleft(), _input.popleft()
        badge = find_the_badge(a, b, c)
        my_sum += PRIORITIES[badge]

    return my_sum


if __name__ == "__main__":
    from os import getenv

    if getenv("DEBUG"):
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    with open(f"day{DAY}-input.txt", "r") as fh:
        puzzle_input = fh.read()

    logging.info(f"read in {len(puzzle_input)} lines")

    print(f"PART 1: sum is {part1(puzzle_input)}")
    print(f"PART 2: sum is {part2(puzzle_input)}")

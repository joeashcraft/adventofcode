#!env python
"""Day 4: Camp Cleanup

https://adventofcode.com/2022/day/4
"""

import logging

DAY = 4


def part1(puzzle_input):
    """In how many assignment pairs does one range fully contain the other?"""
    FUNC = "part1"
    lines = puzzle_input.splitlines()
    result = 0
    pairs = [tuple(line.split(",")) for line in lines]
    coords = list()  # [ [(2, 4), (6,8)],
                     #   [(2, 3), (4, 5)], ... ]
    for a, b in pairs:
        z = list()
        z.append(tuple(map(int, a.split("-"))))
        z.append(tuple(map(int, b.split("-"))))
        coords.append(z)
    for a, b in coords:
        if a[0] >= b[0] and a[1] <= b[1]:
            logging.debug(f"{FUNC}(): {a} is within {b}")
            result += 1
        elif a[1] >= b[1] and a[0] <= b[0]:
            logging.debug(f"{FUNC}(): {b} is within {a}")
            result += 1
    return result


def part2(puzzle_input):
    """In how many assignment pairs do the ranges overlap?"""
    FUNC = "part2"
    lines = puzzle_input.splitlines()

    result = 0
    pairs = [tuple(line.split(",")) for line in lines]
    coords = list()  # [ [(2, 4), (6,8)],
                     #   [(2, 3), (4, 5)], ... ]
    for a, b in pairs:
        z = list()
        z.append(tuple(map(int, a.split("-"))))
        z.append(tuple(map(int, b.split("-"))))
        coords.append(z)
    for a, b in coords:
        if a[0] >= b[0] and a[0] <= b[1]:
            logging.debug(f"{FUNC}(): Sit. 1: {a[0]} is within {b}")
            result += 1
        elif a[1] >= b[0] and a[1] <= b[1]:
            logging.debug(f"{FUNC}(): Sit. 2: {a[1]} is within {b}")
            result += 1
        elif a[0] <= b[0] and a[1] >= b[1]:
            logging.debug(f"{FUNC}(): Sit. 3: {a[1]} is within {b}")
            result += 1
        elif a[0] >= b[0] and a[1] <= b[1]:
            logging.debug(f"{FUNC}(): Sit. 4: {a[1]} is within {b}")
            result += 1

    # answer is not 457
    return result


if __name__ == "__main__":
    from os import getenv

    if getenv("DEBUG"):
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    with open(f"day{DAY}-input.txt", "r") as fh:
        puzzle_input = fh.read()

    logging.info(f"read in {len(puzzle_input)} lines")

    print(f"PART 1: found {part1(puzzle_input)} pairs fully contained")
    print(f"PART 2: found {part2(puzzle_input)} pairs overlap some")

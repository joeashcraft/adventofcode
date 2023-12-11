#!env python
"""Consider your entire calibration document. What is the sum of all of the calibration values?

https://adventofcode.com/2023/day/1
"""

import logging

DAY = 1


def part1_helper(line):
    my_num = 0
    # foreach char (left to right)
    for char in line:
        # if char is digit, then x10 and append to list, and store 'last=$digit'
        if char.isdigit():
            my_num = int(char) * 10
            break
    for char in reversed(line):
        if char.isdigit():
            my_num += int(char)
            break

    return my_num


def part1(puzzle_input):
    _func = "part1"
    _input = puzzle_input.splitlines()
    logging.info(f"{_func}(got {len(_input)} lines)")

    sum = 0
    # readlines from the file
    # foreach line
    for line in _input:
        sum += part1_helper(line)

    return sum


def part2(puzzle_input):
    _func = "part2"
    _input = puzzle_input.splitlines()
    logging.info(f"{_func}(got {len(_input)} lines)")

    pass


if __name__ == "__main__":
    from os import getenv

    if getenv("DEBUG"):
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    with open(f"day{DAY}-input.txt", "r") as fh:
        puzzle_input = fh.read()

    logging.info(f"read in {len(puzzle_input)} lines")

    print(f"PART 1: {part1(puzzle_input)}")
    print(f"PART 2: {part2(puzzle_input)}")

#!env python
"""Consider your entire calibration document. What is the sum of all of the calibration values?

https://adventofcode.com/2023/day/1
"""

import logging

DAY = 1


def part1_helper(line: str) -> int:
    """return the two-digit number of the left-most and right-most numerals in a string."""
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


def part2_helper(line: str) -> int:
    """Return the two-digit number of the left-most and right-most numerals (digits or words)."""
    _func = "part2_helper"
    logging.debug(f"{_func}(line({len(line)})={line})")

    calibration_value = 0
    number_words = (
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    )
    potential_left = []  # [ (value=1, index=2) ]
    potential_right = []  # [ (value=1, index=9) ]

    for ii, char in enumerate(line):
        # find the left-most digit and its index
        if char.isdigit():
            potential_left = [(char, ii)]
            logging.debug(f"potential_left={potential_left}")
            break

    # find the right-most digit and its index
    for ii, char in reversed(list(enumerate(line))):
        if char.isdigit():
            potential_right = [(char, ii)]
            logging.debug(f"potential_right={potential_right}")
            break
    # find any word-numbers and their indexes
    # TODO
    # if any word-number has a lesser index than the left-most digit, then store the word-number instead
    # if any word-number has a greater index than the right-most digit, then store the word-number instead

    logging.info(f"{_func}() returns {calibration_value})")
    return calibration_value


def part2(puzzle_input):
    """What is the sum of all of the calibration values?"""
    _func = "part2"
    _input = puzzle_input.splitlines()
    logging.info(f"{_func}(got {len(_input)} lines)")

    result = 0
    # foreach line of puzzle input
    for line in _input:
        # add the calibration value to running sum
        result += part2_helper(line)
        logging.debug(f"  result=={result}")
    # return the sum
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

    print(f"PART 1: {part1(puzzle_input)}")
    print(f"PART 2: {part2(puzzle_input)}")

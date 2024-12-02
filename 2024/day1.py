#!env python
"""Day 1: Historian Hysteria

https://adventofcode.com/2024/day/1
"""

from logzero import logger as logging
import logzero
from utils.api import get_input

DAY = 1


# def part1_helper(line: str) -> int:
#     _func = "part1_helper"
#     logging.debug(f"{_func}(got {len(_input)} lines)")
#
#     logging.info(f"{_func}() returns {result})")
#     pass
def calc_distances(pairs: tuple) -> tuple:
    _func = "calc_distances"
    logzero.loglevel(logzero.INFO)
    logging.info(f"{_func}(got {len(pairs)} lines)")
    logging.debug(f"{_func}(pairs({len(pairs)})=({pairs[0][:3]},{pairs[1][:3]}, ...))")

    result = [abs(a - b) for a, b in pairs]
    # for a, b in pairs:
    #     result.append(abs(a - b))

    logging.info(f"{_func}() returns {result[:3]}, ...)")
    return tuple(result)


def sort_pairs(pairs: tuple) -> tuple:
    _func = "sort_pairs"
    logzero.loglevel(logzero.INFO)
    logging.info(f"{_func}(got {len(pairs)} pairs)")
    logging.debug(f"{_func}(pairs({len(pairs)})=({pairs[0][:3]},{pairs[1][:3]}, ...))")

    result = tuple(zip(sorted(pairs[0]), sorted(pairs[1])))

    logging.info(f"{_func}() returns {result[:3]}, ...)")
    return result


def parse_input(lines: list) -> tuple:
    _func = "parse_input"
    logzero.loglevel(logzero.INFO)
    logging.info(f"{_func}(got {len(lines)} items in list)")
    logging.debug(f"{_func}(lines={lines[:3]}...)")

    column_a = []
    column_b = []

    for line in lines:
        logging.debug(f"  line={line}")
        logging.debug(f"  line.split()={line.split()}")
        column_a.append(int(line.split()[0]))
        logging.debug(f"  column_a[{len(column_a)}]={column_a[-1]}")
        column_b.append(int(line.split()[1]))
        logging.debug(f"  column_b[{len(column_b)}]={column_b[-1]}")

    result = (column_a, column_b)
    logging.info(f"{_func}() returns ({result[0][:3]},{result[1][:3]})...)")
    return result


def part1(puzzle_input) -> int:
    _func = "part1"
    _input = puzzle_input.splitlines()
    logging.debug(f"{_func}(got {len(_input)} lines)")

    # parse input
    # column_a = []
    # column_b = []
    parsed: tuple = parse_input(_input)

    # for line in _input:
    #     column_a.append(line.split(" ")[0])
    #     column_b.append(line.split(" ")[1])

    # make new pairs, sorted
    # sorted_pairs = []
    # sorted_pairs = [zip(sorted(column_a), sorted(column_b))]
    sorted_pairs: tuple = sort_pairs(parsed)

    # calculate distance
    distances: tuple = calc_distances(sorted_pairs)

    # sum the distance

    result: int = sum(distances)
    logging.info(f"{_func}() returns {result}")
    return result


# def part2_helper(line: str) -> int:
#     _func = "part2_helper"
#     logging.debug(f"{_func}(got {len(_input)} lines)")
#
#     logging.info(f"{_func}() returns {result})")
#     pass


def calc_similarity(lists_of_columns: tuple) -> tuple:
    """Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list."""
    _func = "calc_similarity"
    logzero.loglevel(logzero.DEBUG)
    logging.debug(f"{_func}(got {len(lists_of_columns)} lists_of_columns)")

    result = []
    for aa in lists_of_columns[0]:
        # similarity score is "Item A" times occurences in Column B
        result.append(int(aa) * int(lists_of_columns[1].count(aa)))
    logging.info(f"{_func}() returns {result[:9]}, ...)")
    return tuple(result)


def part2(puzzle_input) -> int:
    """Once again consider your left and right lists. What is their similarity score?"""
    _func = "part2"
    _input = puzzle_input.splitlines()
    logging.debug(f"{_func}(got {len(_input)} lines)")

    # parse input
    parsed: tuple = parse_input(_input)

    # create list of similarity scores
    similarities: tuple = calc_similarity(parsed)

    # sum similarity scores

    result: int = sum(similarities)
    logging.info(f"{_func}() returns {result}")
    return result


if __name__ == "__main__":
    from os import getenv

    # if getenv("DEBUG"):
    #     logging.basicConfig(level=logging.DEBUG)
    # else:
    #     logging.basicConfig(level=logging.INFO)

    puzzle_input = get_input(DAY)

    logging.info(f"read in {len(puzzle_input)} lines")

    if getenv("PART") == "1":
        print(f"PART 1: {part1(puzzle_input)}")
    elif getenv("PART") == "2":
        print(f"PART 2: {part2(puzzle_input)}")
    else:
        print(f"PART 1: {part1(puzzle_input)}")
        print(f"PART 2: {part2(puzzle_input)}")

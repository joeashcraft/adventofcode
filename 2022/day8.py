#!/usr/bin/env python
"""Day 8: Treetop Tree House

https://adventofcode.com/2022/day/8
"""

import logging

# from pprint import pprint

DAY = 8


# def count_perimeter_trees(map: list) -> int:
#     # count of perimeter trees == 2x nubmer of rows, and 2x num of columns, minus 4 corners
#     return (2 * len(map) + 2 * len(map[0])) - 4


def map_visible_trees(row: list) -> list:
    """Return a list which indicates whether a tree is visible.

    This simulates standing in front of a line of trees, and
    only counts trees visible from 1 point of view. So, run this again with the same
    list in reverse order to change the POV.

    INPUT: a single list of tree heights
    RETURNS a single list of 1s and 0s where 1 means a tree at the same position is visible.
    """
    _func = "map_visible_trees"
    row = list(row)
    logging.debug(f"{_func}(row({type(row)})={row})")
    logging.info(f"{_func}(got {len(row)} trees)")

    result = [False] * len(row)
    result[0] = True
    for ii, tree in enumerate(row):
        if ii == 0:
            continue
        if tree > max(row[0:ii]):
            result[ii] = True
    logging.debug(f"{_func} returns {result}")
    return result


def flatten(l):
    return [item for sublist in l for item in sublist]


def part1_np(puzzle_input):
    """Consider your map; how many trees are visible from outside the grid?

    Use numpy this time. #TODO"""
    _func = "part1_np"
    _input = puzzle_input.splitlines()
    logging.info(f"{_func}(got {len(_input)} lines)")

    import numpy as np

    my_arr = np.array(_input)

    pass


def part1(puzzle_input):
    """Consider your map; how many trees are visible from outside the grid?"""
    _func = "part1"
    _input = puzzle_input.splitlines()
    logging.info(f"{_func}(got {len(_input)} lines)")

    # a tree is visibile if tallest tree in front of it is shorter than it
    # all trees on perimeter are visible

    # a tree only counts as visible up to 1 time

    # STRATEGY: create a simpler map which just shows whether a tree is visible with 1 or 0
    trees_visible = [[False] * len(_input)] * len(_input[0])
    logging.debug("➡️Left to Right")
    # left to right
    for ii, row in enumerate(_input):
        trees_visible[ii] = map_visible_trees(row)
        # breakpoint()
        logging.debug(f"  trees_visible:{trees_visible}")

    # right to left
    logging.debug("⬅️Right to Left")
    for ii, row in enumerate(_input):
        trees_visible[ii] = list(
            map(any, zip(trees_visible[ii], reversed(map_visible_trees(reversed(row)))))
        )
    logging.debug(f"  trees_visible after RTL:{trees_visible}")
    logging.info(f"  trees_visible after RTL:{flatten(trees_visible).count(True)}")

    # top to bottom
    logging.debug("⬇️Top to Bottom")
    ttb_trees_visible = list()
    for col_num, column in enumerate(zip(*_input)):
        ttb_trees_visible.append(
            list(
                # fmt: off
            map(
                any,
                zip(
                    list(zip(*trees_visible))[col_num],
                    map_visible_trees(column))
            )
                # fmt: on
            )
        )

    # comparison is done; re-arrange back to rows/columns from columns/rows
    for col_num, column in enumerate(ttb_trees_visible):
        for row_num, tree in enumerate(column):
            trees_visible[row_num][col_num] = tree

    logging.debug(f"  trees_visible after TTB:{trees_visible}")
    logging.info(f"  trees_visible after TTB:{flatten(trees_visible).count(True)}")

    # bottom to top
    logging.debug("🆙Bottom to Top")
    btt_trees_visible = list()
    for col_num, column in enumerate(zip(*_input)):
        btt_trees_visible.append(
            list(
                # fmt: off
            map( #TODO
                any,
                zip(
                    list(zip(*trees_visible))[col_num][::-1],
                    map_visible_trees(column[::-1]))
            )
                # fmt: on
            )
        )
    for col_num, column in enumerate(btt_trees_visible):
        for row_num, tree in enumerate(column):
            trees_visible[row_num + 1 - len(btt_trees_visible)][col_num] = tree
    logging.debug(f"  trees_visible after BTT:{trees_visible}")
    logging.info(f"  trees_visible after BTT:{flatten(trees_visible).count(True)}")

    logging.debug(f"trees_visible={trees_visible}")
    logging.info(f"trees_visible={flatten(trees_visible).count(True)}")
    return flatten(trees_visible).count(True)


def part2(puzzle_input):
    """Consider each tree on your map. What is the highest scenic score possible for any tree?"""
    _func = "part2"
    _input = puzzle_input.splitlines()
    logging.info(f"{_func}(got {len(_input)} lines)")

    # TODO

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

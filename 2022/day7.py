#!env python
"""Day 7: No Space Left On Device

https://adventofcode.com/2022/day/7
"""

from logzero import logger as logging
import logzero
from pathlib import PurePath as P

DAY = 7
TOTAL_FS_SIZE = 70000000
FREE_SPACE_REQ = 30000000


def fs_filter(fs: dict, filter_size: int) -> dict:
    """returns a dict, a new FS filtered based on size.

    if filter_size is positive, return directories under filter_size.
    if filter_size is negative, return directories over filter_size.
    """
    new_fs = {}
    for name, size in fs.items():
        if filter_size > 0 and size <= filter_size:
            new_fs[name] = size
        if filter_size < 0 and size >= -filter_size:
            new_fs[name] = size
    return new_fs


def parse_fs(puzzle_input) -> dict:
    """return a dictionary representing the filesystem given by puzzle input."""
    _func = "parse_fs"
    _input = puzzle_input.splitlines()
    logging.info(f"{_func}(got {len(_input)} lines)")

    fs = {"/": 0}  # filesystem
    cwd = "/"
    # for each line
    for line in _input[1:]:  # skip first initialization line
        # if cd, then update CWD
        if line[:4] == "$ cd":
            if line[5:] == "..":
                cwd = str(P(cwd).parent)
            else:
                cwd = str(P(cwd, line[5:]))
                fs[cwd] = 0
        # if dir, irgnore?
        # if integer, save filename and ize
        elif line[0] in "123456789":
            _size = int(line.split(" ")[0])
            fs[cwd] += _size
            for d in P(cwd).parents:
                fs[str(d)] += _size
        # if ls, continue
        else:
            continue
    logging.info(f"{_func}() returns a dict with {len(fs)} items.")
    return fs


def part1(puzzle_input):
    """Find all of the directories with a total size of at most 100000.

    What is the sum of the total sizes of those directories?
    """
    _func = "part1"
    _input = puzzle_input.splitlines()
    logging.info(f"{_func}(got {len(_input)} lines)")

    fs = parse_fs(puzzle_input)

    logging.debug(f"{_func}(): fs before filtering={fs}")
    fs = fs_filter(fs, 100000)
    logging.debug(f"{_func}(): fs after filtering={fs}")

    # wrong answers:  1623729 (low)
    return sum(fs.values())


def part2(puzzle_input):
    """Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update.

    What is the total size of that directory?"""

    _func = "part2"
    _input = puzzle_input.splitlines()
    logging.info(f"{_func}(got {len(_input)} lines)")

    fs = parse_fs(puzzle_input)
    free_space = TOTAL_FS_SIZE - fs["/"]
    min_to_delete = FREE_SPACE_REQ - free_space
    logging.info(f"free space={free_space}")
    logging.info(f"min_to_delete={min_to_delete}")

    logging.debug(f"{_func}(): fs before filtering has {len(fs)}")
    fs = fs_filter(fs, -min_to_delete)
    logging.debug(f"{_func}(): fs after filtering has {len(fs)}")

    logging.info(sorted(fs.items(), key=lambda item: item[1]))
    print("PART 2: recommend delete: " + (min(fs, key=fs.get)))

    return min(fs.values())


if __name__ == "__main__":
    from os import getenv

    if getenv("DEBUG"):
        logzero.loglevel(logzero.DEBUG)
    else:
        logzero.loglevel(logzero.INFO)

    with open(f"day{DAY}-input.txt", "r") as fh:
        puzzle_input = fh.read()

    logging.info(f"read in {len(puzzle_input)} lines")

    print(f"PART 1: {part1(puzzle_input)}")
    print(f"PART 2: {part2(puzzle_input)}")

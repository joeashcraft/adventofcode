#!/usr/bin/env python3
# USAGE
# ./$0 [--dry-run] day
#
# --dry-run  do not submit answer to adventofcode.com
# day (int)  day number to run

import argparse
from logzero import logger
from utils.api import submit_result

DEBUG = False
YEAR = 2024


def init_argparse():
    parser = argparse.ArgumentParser(
        usage="%(prog)s [--dry-run] day",
        description="Run the tests; if tests succeed, submit answer to adventofcode.com.",
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        help="do not submit answer to adventofcode.com",
        action="store_true",
    )
    parser.add_argument("day", type=int)

    return parser


def split_parts_of_solution(solution: list) -> list:
    _func = "split_parts_of_solution"
    logger.info(f"{_func}(solution({type(solution)}, len={len(solution)})")
    logger.debug(f"  solution given = {bytes(solution, 'utf-8')}")

    result = [None, None]
    _solution = solution.splitlines()
    try:
        result[0] = _solution[0].split(":")[1].strip()
        result[1] = _solution[1].split(":")[1].strip()
    except:
        logger.error("  failed to parse a part of solution")
    if result[0] == "None":
        logger.error("  Part 1 not implemented")
        result[0] = None
    if result[1] == "None":
        logger.error("  Part 2 not implemented")
        result[1] = None
    logger.info(f"  return {result}")
    return result


if __name__ == "__main__":
    parser = init_argparse()
    if DEBUG:
        args = parser.parse_args(["--dry-run", "1"])
    else:
        args = parser.parse_args()
    logger.debug(args)

    ## ONE: run tests
    from os import system, popen
    from sys import exit

    tests_result = system(f"python3 day{args.day}_test.py")
    if tests_result:
        logger.debug(f"tests_result: {tests_result}")
        logger.fatal("tests failed, not proceeding to Step Two")
        if not DEBUG:
            exit(tests_result)
    # exec(open(f"day{args.day}_test.py").read())

    ## TWO: run the real thing
    logger.info(f"start Step Two")
    solutions_result = popen(f"python3 day{args.day}.py").read()

    part1_solution, part2_solution = split_parts_of_solution(solutions_result)
    logger.debug(f"part1_solution is {part1_solution}")
    logger.debug(f"part2_solution is {part2_solution}")

    ## THREE: check the answer
    if part1_solution:
        logger.debug("submit part1")
        if args.dry_run:
            logger.debug(
                f"[DRY RUN] submit_result(year={YEAR}, day={args.day}, part=1, answer={part1_solution})"
            )
        # submit_result(YEAR, args.day, 1, part1_solution)
    if part2_solution:
        logger.debug("submit part2")
        if args.dry_run:
            logger.debug(
                f"[DRY RUN] submit_result(year={YEAR}, day={args.day}, part=2, answer={part2_solution})"
            )
        # submit_result(YEAR, args.day, 2, part2_solution)

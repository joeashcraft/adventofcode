#!env python
"""Day 2: Red-Nosed Reports

https://adventofcode.com/2024/day/2
"""

import logzero
from logzero import logger as logging
from utils.api import get_input

DAY = 2


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
def is_safe_report(reports: list) -> tuple:
    """a report only counts as safe if all of the following are true:

    * The levels are either all increasing or all decreasing; and
    * Any two adjacent levels differ by at least one and at most three."""
    _func = "is_safe_report"
    _input = reports
    logzero.loglevel(logzero.INFO)
    logging.info(f"{_func}(got {len(_input)} lines)")
    logging.debug(f"{_func}(line={_input[:5]}...)")

    result = []
    for report in _input:
        logging.debug(f"  report={report}")
        _result = True
        if not any(
            [sorted(report) == report, list(reversed(sorted(report))) == report]
        ):
            logging.debug(f"    report unsafe: levels switch direction")
            _result = False
            result.append(_result)
            continue
        for ii, reading in enumerate(report):
            logging.debug(f"    [{ii}] reading={reading}")
            if ii == 0:
                # skip first reading
                continue
            if reading == report[ii - 1]:
                logging.debug(f"    report unsafe: adjacent levels are the same")
                _result = False
                result.append(_result)
                break
            if abs(reading - report[ii - 1]) > 3:
                logging.debug(f"    report unsafe: adjacent levels vary too much")
                _result = False
                result.append(_result)
                break
        if _result:
            logging.debug(f"  report must be safe")
            result.append(_result)
    assert len(reports) == len(result)
    logging.info(f"{_func}() returns {result[:5]},...")
    return tuple(result)


def parse_input(lists_of_reports: list) -> tuple:
    _func = "parse_input"
    _input = lists_of_reports
    logzero.loglevel(logzero.INFO)
    logging.info(f"{_func}(got {len(_input)} lines)")
    logging.debug(f"{_func}(line={_input[:5]}...)")

    result = []
    for report in _input:
        _report = []
        logging.debug(f"  report={report} {type(report)}")
        for reading in report.split():
            logging.debug(f"    reading={reading} {type(reading)}")
            _report.append(int(reading))

        logging.debug(f"  _report={_report} {type(_report)}")
        logging.debug(f"  _report[-1]={_report[-1]} {type(_report[-1])}")
        result.append(_report)

    logging.info(f"{_func}() returns {result[:5]}...")
    return tuple(result)


def part1(puzzle_input) -> int:
    """Analyze the unusual data from the engineers. How many reports are safe?"""
    _func = "part1"
    _input = puzzle_input.splitlines()
    logzero.loglevel(logzero.INFO)
    logging.info(f"{_func}(got {len(_input)} lines)")

    # parse input
    parsed: tuple = parse_input(_input)

    # determine whether reports are safe
    reports_result: tuple = is_safe_report(parsed)

    # return count of safe reports
    result = sum(reports_result)
    logging.info(f"{_func}() returns {result}")
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


def is_mostly_safe_report(report: list) -> bool:
    """Returns true if a report could be made safe by removing just 1 reading."""
    _func = "is_mostly_safe_report"
    _input = report
    logzero.loglevel(logzero.DEBUG)
    logging.info(f"{_func}(got {len(_input)} readings)")
    logging.debug(f"{_func}(line={_input[:5]}...)")

    # create several editions of report, one report per reading; each edition of the report is the original report minus 1 reading
    modified_reports = []
    for ii, reading in enumerate(_input):
        # maybe copy, then pop?
        _report = _input.copy()
        _report.pop(ii)
        logging.debug(f"  modified_report={_report}")
        modified_reports.append(_report)

        # test all editions of 1 report
        # if any edition is safe, then PASS
        # if no edition is safe, then FAIL
        logging.debug(
            f"  modified_reports({len(modified_reports)})={modified_reports[:2]},..."
        )

    result = bool(any(is_safe_report(modified_reports)))
    logging.info(f"{_func}() returns {result}...")
    return result


def mostly_safe_reports(reports: list, readings_to_ignore: int = 1) -> tuple:
    """Now, the same rules apply as before, except if removing a single level
    from an unsafe report would make it safe, the report instead counts as safe.
    """
    _func = "mostly_safe_reports"
    _input = reports
    logzero.loglevel(logzero.DEBUG)
    logging.info(f"{_func}(got {len(_input)} lines)")
    logging.debug(f"{_func}(line={_input[:5]}...)")

    # if a report is already safe, skip further testing

    # create several editions of a report, one report per reading; each edition of the report is the original report minus 1 reading
    modified_reports = []
    result = []
    for report in _input:
        logzero.loglevel(logzero.DEBUG)
        logging.debug(f"  report={report}")
        result.append(is_mostly_safe_report(report))
    assert len(_input) == len(result)
    logging.info(f"{_func}() returns ({len(result)}) {result[:5]},...")
    return tuple(result)


def part2(puzzle_input) -> int:
    """Update your analysis by handling situations where the Problem Dampener
    can remove a single level from unsafe reports.

    How many reports are now safe?
    """
    _func = "part2"
    _input = puzzle_input.splitlines()
    logzero.loglevel(logzero.INFO)
    logging.debug(f"{_func}(got {len(_input)} lines)")

    # parse input
    parsed: tuple = parse_input(_input)

    # determine whether reports are safe
    reports_result: tuple = mostly_safe_reports(parsed)

    # return count of safe reports
    result = sum(reports_result)
    logging.info(f"{_func}() returns {result}")
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

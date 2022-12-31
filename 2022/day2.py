#!env python
"""Day 2: Rock Paper Scissors.

https://adventofcode.com/2022/day/2
"""

import logging

DAY=2

STRATEGY1_SCORES={
    "A X": 4,  # ROCK rock
    "A Y": 8,  # ...  paper
    "A Z": 3,  # ...  scissor
    "B X": 1,  # PAPER rock
    "B Y": 5,
    "B Z": 9,
    "C X": 7,  # SCISSOR rock
    "C Y": 2,
    "C Z": 6
}

STRATEGY2_SCORES={
    "A X": 3,  # ROCK lose
    "A Y": 4,  # ...  draw
    "A Z": 8,  # ...  win
    "B X": 1,  # PAPER lose
    "B Y": 5,
    "B Z": 9,
    "C X": 2,  # SCISSOR lose
    "C Y": 6,
    "C Z": 7
}

def part1(puzzle_input):
    """What would your total score be if everything goes exactly according to your strategy guide?"""
    _input=puzzle_input.splitlines()
    my_sum = 0
    for ii in _input:
        my_sum += STRATEGY1_SCORES[ii]
    return my_sum

def part2(my_input):
    """Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
    """
    _input=puzzle_input.splitlines()
    my_sum = 0
    for ii in _input:
        my_sum += STRATEGY2_SCORES[ii]
    return my_sum



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    with open(f'day{DAY}-input.txt', 'r') as fh:
        puzzle_input = fh.read()

    logging.info(f'read in {len(puzzle_input)} lines')
    logging.debug(f'  for example: {puzzle_input[:10]}')

    print(f'PART 1: score using Strategy 1: {part1(puzzle_input)}')
    print(f'PART 2: score using Strategy 2: {part2(puzzle_input)}')

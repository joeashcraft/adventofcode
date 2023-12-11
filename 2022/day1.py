#!env python
"""Day 1: Calorie Counting

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

https://adventofcode.com/2022/day/1
"""

import logging

DAY=1

def totals(my_input: list) -> list:
    ret = list()
    ret_i = 0
    for i,calorie in enumerate(my_input):
        logging.debug(f'    FOR elf[{ret_i}]')
        logging.debug(f'    FOR: i={i}, calorie={calorie}')
        try:
            calorie=int(calorie)
            logging.debug(f'add {calorie} to ret[{ret_i}]')
            try:
                ret[ret_i] += calorie
            except IndexError:
                ret.append(calorie)
        except ValueError:
            if calorie=='':
                logging.debug(f'next elf')
                ret_i += 1
    logging.info(f'summed calorie counts for {len(ret)} elfs')
    return ret


def part1(my_input):
    """Find the Elf carrying the most Calories.
    
    How many total Calories is that Elf carrying?
    """
    _input=my_input.splitlines()

    return max(totals(_input))

def part2(puzzle_input):
    """Find the top three Elves carrying the most Calories.
    
    How many Calories are those Elves carrying in total?
    """
    _input=puzzle_input.splitlines()
    part2=sorted(totals(_input))
    logging.debug(part2[-3:])
    return sum(part2[-3:])



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    with open(f'day{DAY}-input.txt', 'r') as fh:
        puzzle_input = fh.read()

    logging.info(f'read in {len(puzzle_input)} lines')

    print("PART 1: Elf with most calories has " + str(part1(puzzle_input)) + " calories.")
    print("PART 2: Top 3 Elves are carrying " + str(part2(puzzle_input)) + " calories.")


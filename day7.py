#!env python
from logzero import logger


class OrderedSet(list):
    def append_dedup(self, *args):
        for x in args:
            if x not in self:
                self.append(x)
        return

class Step(str):
    pass


class Instruction(tuple):
    def __init__(self):
        assert len(self) == 2


class Instructions(list):
    def remove_all(self, Step):
        for Instruction in self:
            if Instruction[0] == Step:
                self.remove(Instruction)
        return


def parse_instructions(raw_instructions: list) -> list:
    """Parse raw_instructions in to tuples

    INPUT: list of strings
    RETURN: list of tuples"""
    # re("Step ([A-Z]) must be finished before step ([A-Z]) can begin\.")
    return [tuple([instruction[5], instruction[36]]) for instruction in raw_instructions]


def part1(raw_instructions: list) -> str:
    final_order = OrderedSet()
    valid_steps = set()
    parsed_instructions = list()

    # reformat raw ins for easier processing
    parsed_instructions = parse_instructions(raw_instructions)
    logger.debug(f"parsed_instructions ({len(parsed_instructions)}): {parsed_instructions}")

    # create a non-dupe list of valid steps
    for instruction in parsed_instructions:
        valid_steps.add(instruction[0])
        valid_steps.add(instruction[1])
    valid_steps: list = sorted(valid_steps)
    valid_steps = {x:0 for x in valid_steps}
    logger.debug(f"valid_steps ({len(valid_steps)}): {valid_steps}")


    # starting at VALID[0], check for any other INS where CURR is second
    # might as well start at the beginning
    step = sorted(valid_steps.keys())[0]
    logger.debug(f"step: {step}")

    wcount = 0
    logger.debug(f"WHILE: {wcount}")
    while len(valid_steps):
        wcount += 1
        logger.debug(f"WHILE: {wcount}")

        # count dependant valid_steps
        for k, v in valid_steps.items():
            count = int(0)
            for x, y in parsed_instructions:
                if k == y:
                    count += 1
            valid_steps[k] = count
        logger.debug(f"valid_steps ({len(valid_steps)}): {valid_steps}")

        # what's ready to exec?
        least = min([v for k, v in valid_steps.items()])
        # sort and exec first
        ready = sorted([k for k, v in valid_steps.items() if v == least])[0]
        logger.debug(f"step: {ready}")
        final_order.append(ready)
        logger.debug(f"final_order ({len(final_order)}): {final_order}")
        valid_steps.pop(ready)
        logger.debug(f"valid_steps ({len(valid_steps)}): {valid_steps}")
        for ii in parsed_instructions.copy():
            # breakpoint()
            if ii[0] == ready:
                parsed_instructions.remove(ii)
                logger.debug(f"parsed_instructions ({len(parsed_instructions)}): {parsed_instructions}")



    # at end of parsed, run remaining VALID in alpha order
    return ''.join(final_order)

if __name__ == '__main__':
    logger.info("Executing as script")
    file = open('day7-input.txt', 'r')
    raw_instructions: list = file.readlines()
    file.close()
    print(part1(raw_instructions))

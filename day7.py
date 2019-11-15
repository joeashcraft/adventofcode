#!env python


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
    final_order = []
    valid_steps = set()
    parsed_instructions = list()

    # reformat raw ins for easier processing
    parsed_instructions = parse_instructions(raw_instructions)

    # create a non-dupe list of valid steps
    for instruction in parsed_instructions:
        valid_steps.add(instruction[0])
        valid_steps.add(instruction[1])
    valid_steps: list = sorted(valid_steps)

    # starting at VALID[0], check for any other INS where CURR is second
    step = valid_steps[0]
    while len(valid_steps):
        before_steps = []
        # e.g. for c, find all instructions which must finish before C
        before_steps = [x for x, y in parsed_instructions if step == y]
        # if found, then go to first ins in alpha order, repeat
        if len(before_steps):
            step = sorted(before_steps)[0]
            continue
        else:
            # if not found, do it, and go to next INS in VALID
            final_order.append(step)
            try:
                valid_steps.remove(step)
            except ValueError:
                True
            for instruction in parsed_instructions:
                if instruction[0] == step:
                    parsed_instructions.remove(instruction)
            try:
                step = valid_steps[0]
            except IndexError:
                True
            continue


    # at end of parsed, run remaining VALID in alpha order
    return final_order

if __name__ == '__main__':
    file = open('day7-input.txt', 'r')
    raw_instructions: list = file.readlines()
    file.close()
    print(part1(raw_instructions))

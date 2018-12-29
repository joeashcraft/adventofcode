#!env python

from collections import defaultdict
import re


def part1_parse(sorted_input):
    # data structure might look like:
    # { GuardId: [0 * 60], ... }
    guards_sleeps = defaultdict(lambda: list(
        map(lambda zz: int(zz), '0' * 60)))

    for line in sorted_input:
        parsing = re.split(r'[ \[\]:#]', line)
        if parsing[5] == 'Guard':
            guard = parsing[7]
            # print("guard: {}".format(parsing[7]))
        elif parsing[5] == 'falls':
            start = int(parsing[3])
            # print("start: {}".format(parsing[3]))
        elif parsing[5] == 'wakes':
            end = int(parsing[3])
            # print("end: {}".format(parsing[3]))
            for ii in range(start, end):
                guards_sleeps[guard][ii] += 1

    return guards_sleeps


def part1_sleep_tots(dd):
    return list(map(lambda guard: (guard, sum(dd[guard])), dd))


def part1_sleepiest_guard(dd):
    return str(max(part1_sleep_tots(dd), key=lambda x: x[1])[0])


def part1_sleepiest_minute(dd):
    return int(dd[part1_sleepiest_guard(dd)].index(max(dd[part1_sleepiest_guard(dd)])))


def part1(input):
    """Strategy 1: Find the guard that has the most minutes asleep.
    What minute does that guard spend asleep the most?

    What is the ID of the guard you chose multiplied by the minute you chose?
    """
    guards_sleeps = part1_parse(input)

    print("Guard {} slept for {} minutes".format(
        part1_sleepiest_guard(guards_sleeps),
        sum(guards_sleeps[part1_sleepiest_guard(guards_sleeps)])
    ))
    return int(int(part1_sleepiest_guard(guards_sleeps)) * part1_sleepiest_minute(guards_sleeps))


def part2(input):
    """Strategy 2: Of all guards, which guard is most frequently asleep on the same minute?

    What is the ID of the guard you chose multiplied by the minute you chose?
    """

    pass


if __name__ == '__main__':
    file = open('day4-input.txt', 'r')
    linesin = file.read()
    file.close()

    input = sorted([ii for ii in linesin.splitlines()])

    print("{} is ID of the guard I chose multiplied by the minute.".format(
        part1(input)))
    # print("{} is the claim with no disputes.".format(part2(input)))

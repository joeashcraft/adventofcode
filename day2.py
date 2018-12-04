#!env python
"""----- Part 1 -----
To make sure you didn't miss any, you scan the likely candidate boxes again,
counting the number that have an ID containing exactly two of any letter and
then separately counting those with exactly three of any letter.
You can multiply those two counts together to get a rudimentary checksum and
compare it to what your device predicts.

For example, if you see the following box IDs:

* abcdef contains no letters that appear exactly two or three times.
* bababc contains two a and three b, so it counts for both.
* abbcde contains two b, but no letter appears exactly three times.
* abcccd contains three c, but no letter appears exactly two times.
* aabcdd contains two a and two d, but it only counts once.
* abcdee contains two e.
* ababab contains three a and three b, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly twice,
and three of them contain a letter which appears exactly three times.

Multiplying these together produces a checksum of 4 * 3 = 12.


What is the checksum for your list of box IDs?

----- Part 2 -----
The boxes will have IDs which differ by exactly one character at the same
position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by
two characters (the second and fourth). However, the IDs fghij and fguij differ
by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above,
this is found by removing the differing character from either ID,
producing fgij.)
"""


def letterCount(word):
    counts = dict()
    # count each letter in id
    for letter in word:
        if letter in counts.keys():
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts


def checksum(box_list):  # part1
    checksum, twos, threes = 0, 0, 0

    # for each box in list:
    for boxId in box_list:
        counts = letterCount(boxId)
        has_twos, has_threes = False, False

        # if any letter is found twice, increment TWOS
        # if any letter is found thrice, increment THREES
        for k, v in counts.items():
            if has_twos and has_threes:
                break
            if v == 2:
                has_twos = True
            if v == 3:
                has_threes = True
        if has_twos:
            twos += 1
        if has_threes:
            threes += 1
    checksum = twos * threes
    return int(checksum)


def part2(box_list):  # part2
    pass


if __name__ == '__main__':
    file = open('day2-input.txt', 'r')
    linesin = file.read()
    file.close()

    box_list = [ii for ii in linesin.splitlines()]

    print("letterCount('aabbccdddeeef'): " + str(letterCount('aabbccdddeeef')))
    print("checksum: " + str(checksum(box_list)))

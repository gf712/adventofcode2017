#! /usr/bin/env python3

# PROBLEM:
# The captcha requires you to review a sequence of digits (your puzzle input)
# and find the sum of all digits that match the next digit in the list.
# The list is circular, so the digit after the last digit is the first digit in the list.
#
# For example:
#
#     1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and
#     the third digit (2) matches the fourth digit.
#     1111 produces 4 because each digit (all 1) matches the next.
#     1234 produces 0 because no digit matches the next.
#     91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(usage="""{} """.
                                     format(sys.argv[0]),
                                     epilog="Solves Day 1 problem of advent of code 2017")

    parser.add_argument("-i", "--input", type=str,
                        help="""Input file""")
    parser.add_argument("-v", "--verbose", type=int, default=1,
                        help="""Verbose""")

    return parser.parse_args()


def main(input, verbose):

    result = 0

    prev_value = input[0]

    for i in range(1, len(input)+1):

        if i == len(input):
            value = input[-1]
        else:
            value = input[i]

        if prev_value == value:
            result += value

        prev_value = value

    if verbose:
        print("Result: {}".format(result))


if __name__ == '__main__':
    args = parse_args()

    with open(args.input, 'r') as f:
        input = [int(x) for x in f.readlines()[0] if x.isdigit()]

    main(input, args.verbose)

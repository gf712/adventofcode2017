#! /usr/bin/env python3

# The spreadsheet consists of rows of apparently-random numbers.
# To make sure the recovery process is on the right track,
# they need you to calculate the spreadsheet's checksum.
# For each row, determine the difference between the largest value and the smallest value;
# the checksum is the sum of all of these differences.
#
# For example, given the following spreadsheet:
#
# 5 1 9 5
# 7 5 3
# 2 4 6 8
#
#     The first row's largest and smallest values are 9 and 1, and their difference is 8.
#     The second row's largest and smallest values are 7 and 3, and their difference is 4.
#     The third row's difference is 6.
#
# In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(usage="""{} """.
                                     format(sys.argv[0]),
                                     epilog="Solves Day 2 problem of advent of code 2017")

    parser.add_argument("-i", "--input", type=str,
                        help="""Input file""")
    parser.add_argument("-v", "--verbose", type=int, default=1,
                        help="""Verbose""")

    return parser.parse_args()


def main(data, verbose):

    result = 0

    for row in data:
        min_i = min(row)
        max_i = max(row)

        result += max_i - min_i

    if verbose:
        print("Result: {}".format(result))


if __name__ == '__main__':

    args = parse_args()

    with open(args.input, 'r') as f:
        data = [[int(x) for x in row.split() if x.isdigit()] for row in f.readlines()]

    main(data, args.verbose)

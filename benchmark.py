#! /usr/bin/env python3

import timeit
from format_time import format_time


# BENCHMARKING

##############################################
#                   DAY 1
##############################################

print("""
##############################################
                   DAY 1
##############################################
""")

setup = """from Day1 import inverse_captcha
with open('Day1/day1_data.txt', 'r') as f:
    input = [int(x) for x in f.readlines()[0] if x.isdigit()]
"""

naive_python = timeit.timeit('inverse_captcha.main(input, 0)',
                             setup=setup,
                             number=10000) / 10000

print('Naive python 3 solution: {:>10.6f} {}/it'.format(*format_time(naive_python)))

##############################################
#                   DAY 2
##############################################

print("""
##############################################
                   DAY 2
##############################################
""")

setup = """from Day2 import corruption_checksum
with open('Day2/day2_data.txt', 'r') as f:
    input = [[int(x) for x in row.split() if x.isdigit()] for row in f.readlines()]"""

naive_python = timeit.timeit('corruption_checksum.main(input, 0)',
                             setup=setup,
                             number=10000) / 10000

print('Naive python 3 solution: {:>10.6f} {}/it'.format(*format_time(naive_python)))


##############################################
#                   END
##############################################
print("""
##############################################
              MERRY CHRISTMAS
##############################################
""")

n = 21
print(' '*int(n) + '*' + ' '*int(n/2))

for i in range(n):
    print(' ' * (n - (i + 1)), '+' * (2 * i + 1))

print(' '*int(n) + '||' + ' '*int(n/2))

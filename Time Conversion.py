# Sample Input 0
# 07:05:45PM

# Sample Output 0
# 19:05:45

import math
import os
import random
import re
import sys


def timeConversion(s):
    period = s[-2:]
    hh, mm, ss = map(int, s[:-2].split(':'))

    if period == 'AM':
        if hh == 12:
            hh = 0
    else:  # PM
        if hh != 12:
            hh += 12

    return f"{hh:02}:{mm:02}:{ss:02}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

# Sample Input 0
# 4
# 3 2 1 3

# Sample Output 0
# 2

# Explanation 0
# Candle heights are [3 2 1 3] . The tallest candles are  units, and there are 2 of them.

import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):
    # res = 0;
    # for num in candles:
    #     if num == max(candles):
    #         res+=1
    # return res
    num = max(candles)
    return candles.count(num)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

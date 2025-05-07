# Sample Input
# 1 2 3 4 5

# Sample Output
# 10 14

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    total = sum(arr)
    minimum = total - max(arr)
    maximum = total - min(arr)
    print(minimum,maximum)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
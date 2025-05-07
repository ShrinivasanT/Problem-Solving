# Sample Input
# STDIN      Function
# -----      --------
# 3           arr[][] sizes n = 3, m = 3
# 11 2 4     arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
# 4 5 6
# 10 8 -12

# Sample Output
# 15

# Explanation
# The primary diagonal is:
# 11
#    5
#      -12
# Sum across the primary diagonal: 11+5-12=4.

# The secondary diagonal is:
#      4
#    5
# 10

# Sum across the secondary diagonal:4+5+10=19 
# Difference: |4-19| = 15

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    n = len(arr)
    right = 0
    left = 0
    for i in range(n):
        right += arr[i][i]
        left += arr[i][n-i-1]
    return abs(right-left)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

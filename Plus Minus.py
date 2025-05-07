# Sample Input
# STDIN           Function
# -----           --------
# 6               arr[] size n = 6
# -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

# Sample Output
# 0.500000
# 0.333333
# 0.166667

import math
import os
import random
import re
import sys

def plusMinus(arr):

    zer = []
    pos = []
    neg = []
    for num in arr:
        if num < 0:
            neg.append(num)
        elif num > 0:
            pos.append(num)
        else :
            zer.append(num)
    pr = len(pos)/len(arr)
    nr = len(neg)/len(arr)
    zr = len(zer)/len(arr)
    print(f"{pr:.6f}")
    print(f"{nr:.6f}")
    print(f"{zr:.6f}")
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

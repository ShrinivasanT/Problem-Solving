# Sample Input
# STDIN                       Function
# -----                       --------
# 9                           n = 9
# 10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

# Sample Output
# 3

import math
import os
import random
import re
import sys
from collections import Counter

def sockMerchant(n, ar):
    pairs = 0
    counts = Counter(ar)
    for sock_color, count in counts.items():
        pairs += count // 2
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

# Sample Input 1
# 11
# 1 2 3 4 5 4 3 2 1 3 4

# Sample Output 1
# 3

import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    count = {}
    for bird in arr:
        if bird not in count:
            count[bird] = 0
        count[bird] += 1
        
    maxval = max(count.values())
    
    best = []
    for key, val in count.items():
        if val == maxval:
            best.append(key)             

    return min(best)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

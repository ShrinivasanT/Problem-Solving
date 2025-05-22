# Sample Input 1
# 10
# 3 4 21 36 10 28 35 5 24 42

# Sample Output 1
# 4 0

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    res = []
    minimum = maximum = scores[0]
    minimum_count = 0
    maximum_count = 0
    for num in scores:
        if num > maximum:
            maximum = num
            maximum_count+=1
        elif num < minimum:
            minimum = num
            minimum_count+=1
    res.append(maximum_count)
    res.append(minimum_count)
    return res
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

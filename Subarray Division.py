# Sample Input 2
# 1
# 4
# 4 1

# Sample Output 2
# 1

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    count = 0
    segment = []
    for num in s:
        segment.append(num)
        while(len(segment)==m):
            if sum(segment) == d:
                count+=1
            segment.remove(segment[0])
    return count        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()

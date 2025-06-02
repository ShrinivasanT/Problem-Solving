# Sample Input
# STDIN           Function
# -----           --------
# 6 3             n = 6, k = 3
# 1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]

# Sample Output
#  5

import math
import os
import random
import re
import sys

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i]+ar[j])%k==0:
                count+=1
            else:
                pass
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

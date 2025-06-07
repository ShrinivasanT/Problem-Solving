# Sample Input 0
# 6
# 2

# Sample Output 0
# 1

import math
import os
import random
import re
import sys

def pageCount(n, p):
    # Write your code here
    first_page_count= p//2
    back_count = (n//2)-(p//2)
    return min(first_page_count,back_count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

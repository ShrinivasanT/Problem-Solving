# return reversed array

import math
import os
import random
import re
import sys

def reverseArray(a):
    # supposed to be with logic using for loop and -1 iteration but this works better
    return reversed(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

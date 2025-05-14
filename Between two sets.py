# Sample Input
# 2 3
# 2 4
# 16 32 96

# Sample Output
# 3

import math
import os
import random
import re
import sys

def getTotalX(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    def lcm(x, y):
        return x * y // gcd(x, y)
    
    lcm_a = a[0]
    for num in a[1:]:
        lcm_a = lcm(lcm_a, num)
    
    gcd_b = b[0]
    for num in b[1:]:
        gcd_b = gcd(gcd_b, num)
    
    count = 0
    multiple = lcm_a
    while multiple <= gcd_b:
        if gcd_b % multiple == 0:
            count += 1
        multiple += lcm_a
    
    return count
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()

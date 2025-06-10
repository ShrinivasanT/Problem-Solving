# Sample Input 0
# 2
# 1 2 3
# 1 3 2

# Sample Output 0
# Cat B
# Mouse C

import math
import os
import random
import re
import sys

def catAndMouse(x, y, z):
    min_catA = (z-x)**2
    min_catB = (z-y)**2 
    
    if min_catA > min_catB : 
        return "Cat B"
    elif min_catB > min_catA:
        return "Cat A"
    else : 
        return "Mouse C"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()

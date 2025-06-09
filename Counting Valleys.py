# Sample Input
# 8
# UDDDUDUU

# Sample Output
# 1

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    level=0
    valley=0
    
    for step in path:
        if step =='U':
            level+=1
            if level==0:
                valley+=1
        elif step == 'D':
            level-=1
    return valley        
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

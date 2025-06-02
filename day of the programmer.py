# Sample Input 1
# 2016

# Sample Output 1
# 12.09.2016

import math
import os
import random
import re
import sys

def dayOfProgrammer(year):
    if year == 1918:
        return f"26.09.{year}"
    
    if year < 1918 and year % 4 == 0:
        return f"12.09.{year}"
        
    # Is Gregorian is factor of both 4 and 400 and
    # is not a factor of 100
    if year > 1918 and year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return f"12.09.{year}"
    
    # All other is 9/13
    return f"13.09.{year}" 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

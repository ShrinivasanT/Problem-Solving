# Sample Input 0
# 7 11
# 5 15
# 3 2
# -2 2 1
# 5 -6

# Sample Output 0
# 1
# 1

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0
    
    # Count apples falling within the range [s, t]
    for apple in apples:
        if a + apple >= s and a + apple <= t:
            apple_count += 1
    
    # Count oranges falling within the range [s, t]
    for orange in oranges:
        if b + orange >= s and b + orange <= t:
            orange_count += 1
    
    # Print the results
    print(apple_count)
    print(orange_count)
    # Write your code here

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

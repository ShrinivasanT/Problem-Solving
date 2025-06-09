# Sample Input 0
# 10 2 3
# 3 1
# 5 2 8

# Sample Output 0
# 9

import os
import sys

def getMoneySpent(keyboards, drives, b):
    spent_amt = -1
    for i  in keyboards:
        for j in drives:
            if ((i+j)<=b and (i+j)>spent_amt):
                spent_amt = i+j
    return spent_amt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()

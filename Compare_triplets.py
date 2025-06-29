#Sample Input 1
#17 28 30
#99 16 8

#Sample Output 1
#2 1

#Explanation 1

#Comparing the  elements,  so Bob receives a point.
#Comparing the  and  elements,  and  so Alice receives two points.
#The return array is 



import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    # Write your code here
    res = []
    alice = 0
    bob = 0
    for i in range(len(a)):
        if a[i] < b[i]:
            bob+=1
        elif a[i] > b[i]:
            alice+=1
                 
        
        
        
    res.append(alice)
    res.append(bob)
    return res
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

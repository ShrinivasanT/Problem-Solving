# Sample Input 1
# 4 1
# 3 10 2 9
# 7

# Sample Output 1
# Bon Appetit

import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    anna_bill = []
    bill.pop(k)
    anna_bill = bill
    actual_charge = 0
    
    for i in anna_bill:
        actual_charge+=i
           
    actual_charge = actual_charge//2 

    if actual_charge == b:
        print('Bon Appetit')
    elif actual_charge <b:
        print(b-actual_charge)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

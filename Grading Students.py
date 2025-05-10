# Sample Input 
# 73
# 67
# 38
# 33

# Sample Output
# 75
# 67
# 40
# 33

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    final_grade=[]
    for i in grades:
        if i>35 :
            if (i%5)>=3:
                res = i+(5-(i%5))
            else:
                res = i
        else :
            res = i
        final_grade.append(res)  
    return final_grade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

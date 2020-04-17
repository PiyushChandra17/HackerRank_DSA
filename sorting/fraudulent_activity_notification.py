#!/bin/python3

import math
import os
import random
import re
import sys


from bisect import insort, bisect_left

def activityNotifications(expenditure, d):
    # Check in
    if len(expenditure) < d : return 0

    # Usefull var
    res = 0
    half = int(d / 2)
    is_impair = d % 2 == 0 

    # Prepare, sort
    l_sorted = sorted(expenditure[:d])

    for i, current in enumerate(expenditure[d:]):
        # Add point
        if is_impair: med2 = l_sorted[half] + l_sorted[half-1]
        else: med2 = l_sorted[half] * 2
        if current >= med2:  res += 1

        # Remove last
        last = expenditure[i]
        index = bisect_left(l_sorted, last)
        del l_sorted[index]
                
        # Add new
        insort(l_sorted, current)

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

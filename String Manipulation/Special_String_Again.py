#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    count = n
    streak = [1] * n

    for i in range(1,n):
        if s[i] == s[i-1]:
            count += streak[i-1]
            streak[i] = streak[i-1] + 1

        temp = i - streak[i] - 1
        if temp >= 0:
            if s[i]==s[temp] and streak[i]<=streak[temp]:
                count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

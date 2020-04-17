#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the countTriplets function below.
def countTriplets(arr, r):
    r1 = Counter()
    r2 = Counter()

    count = 0
    for v in arr:
        if v/r in r2:
            count += r2[v/r]
        if v/r in r1:
            r2[v] += r1[v/r]
        r1[v] += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    while arr != [n for n in range(1,n+1)]:
        for i in range(len(arr)):
            if arr[i] != (i+1):
                ni = arr[i] - 1
                arr[i],arr[ni] = arr[ni],arr[i]
                swaps += 1
    return swaps
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    sz = len(s)
    count = 0

    for i in range(1,sz):
        for j in range(sz-i):
            for k in range(1,sz-i-j+1):
                if sorted(s[j:i+j]) == sorted(s[j+k:i+j+k]):
                    count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

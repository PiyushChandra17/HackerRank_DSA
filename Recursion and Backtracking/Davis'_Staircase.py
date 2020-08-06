#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    s0,s1,s2 = 1,2,4
    for i in range(n-1):
        s0,s1,s2 = s1,s2,s0+s1+s2
    return s0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()

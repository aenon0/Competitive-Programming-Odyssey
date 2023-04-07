#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    misplaced = arr[-1]
    indx = n - 1
    while misplaced < arr[indx - 1] and indx > 0:
        arr[indx] = arr[indx - 1] 
        indx -= 1
        print(*arr)
    arr[indx] = misplaced
    print(*arr)
         

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

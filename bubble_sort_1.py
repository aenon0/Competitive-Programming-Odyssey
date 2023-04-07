#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(arr):
    swaps = 0
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                # print(arr[j - 1], arr[j])
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    print("Array is sorted in", swaps, "swaps.")
    print("First Element:", arr[0])
    print("Last Element:", arr[-1])


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)

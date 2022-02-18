import math
import os
import random
import re
import sys

def reverseArray(arr):
    reverse_arr = []
    for i in range(0, len(arr)):
        reverse_arr.append(arr[len(arr)-1-i])
    return reverse_arr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    res = reverseArray(arr)
    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')
    fptr.close()

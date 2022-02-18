#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    output_list = list()
    print(a)
    array_list = a.split()
    while len(array_list) > 0:
        output_list.append(int(array_list[-1]))
        array_list.remove(array_list[-1])
    return output_list


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # arr_count = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))
    arr = input("give list: ")

    # res = reverseArray(arr)
    print(reverseArray(arr))
    # fptr.write(' '.join(map(str, res)))
    # fptr.write('\n')
    #
    # fptr.close()

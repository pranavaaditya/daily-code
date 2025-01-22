#We have already solved this using Python's capabilities.
#Now solving this with for loop - 

#!/bin/python3

import math
import os
import random
import re
import sys


def reverseArray(a): 
    
    reversed_array = []
    for i in range(len(a)):
        reversed_array.insert(0, a[i])
    return reversed_array
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

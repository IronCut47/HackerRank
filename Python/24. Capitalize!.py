#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    final = []
    temp = s.split(' ')
    for i in range(0, len(temp)):
        var = temp[i].capitalize()
        final.append(var)
    name = ' '.join(final)
    return name
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
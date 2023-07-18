import math
import os
import random
import re
import sys

# Another sorting method, the counting sort,
# does not require comparison. Instead, you create
# an integer array whose index range covers the entire
# range of values in your array to sort. Each time a
# value occurs in the original array, you increment
# the counter at that index. At the end, run through
# your counting array, printing the value of each non-zero
# valued index that number of times.
#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    # initialize int array
    result = [0 for i in range(100)]
    for i in arr:
        result[i] += 1
    return result


print(countingSort([1, 1, 3, 2, 1, 5, 5, 6,
                    7, 7, 3, 2, 1, 8, 9, 11]))

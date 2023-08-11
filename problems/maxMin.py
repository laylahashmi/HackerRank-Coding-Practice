#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    arr.sort()
    i = 0
    res = arr[-1]
    # largest number

    while True:
        try:
            tmp = arr[i+k-1] - arr[i]
            if res > tmp:
                res = tmp
        except:
            break
        i += 1

    return res

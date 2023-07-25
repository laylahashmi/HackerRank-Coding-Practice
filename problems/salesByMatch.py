#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    pairs = sum(i//2 for i in [ar.count(i) for i in (set(ar))])
    return pairs


print(sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]))

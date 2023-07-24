#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"


k = 5
A = [2, 1, 3]
B = [7, 8, 9]

# A = [1, 2, 2, 1]
# B = [3, 3, 3, 4]

print(twoArrays(k, A, B))

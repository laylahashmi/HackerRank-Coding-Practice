#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    l = len(arr[0])
    left_d = ([arr[i][i] for i in range(l)])
    right_d = ([arr[l-1-i][i] for i in range(l-1, -1, -1)])
    return abs((sum(left_d))-(sum(right_d)))


print(diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]))

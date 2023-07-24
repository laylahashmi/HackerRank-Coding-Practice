#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    s = set(a)
    for i in s:
        if a.count(i) == 1:
            return i


print(lonelyinteger([1, 2, 3, 4, 3, 2, 1]))

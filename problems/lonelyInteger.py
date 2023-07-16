#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    result = {}
    for number in a:
        if number not in result:
            result[number] = 0
        result[number] += 1
    for value in result:
        if result[value] == 1:
            return value


print(lonelyinteger([1, 2, 3, 4, 3, 2, 1]))

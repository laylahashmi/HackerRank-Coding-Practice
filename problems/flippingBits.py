#  You will be given a list of 32 bit unsigned integers.
#  Flip all the bits
# ( and ) and return the result as an unsigned integer.
#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    return ((2**32)-1-n)

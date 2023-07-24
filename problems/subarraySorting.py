# Two children, Lily and Ron, want to share a chocolate bar.
# Each of the squares has an integer on it.

# Lily decides to share a contiguous segment of the bar selected such that:

# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# Determine how many ways she can divide the chocolate.
#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    count = 0
    i = 0
    j = m
    while j <= len(s):
        if sum(s[i:j]) == d:
            count += 1
        i += 1
        j += 1
    return count


s = [2, 2, 1, 3, 2, 2]
d = 4
m = 2
print(birthday(s, d, m))

# Given five positive integers, find the minimum and maximum values that can
# be calculated by summing exactly four of the five integers. Then print the
# respective minimum and maximum values as a single line of two space-separated long integers.

# Function Description
# -miniMaxSum has the following parameter(s):
# --arr: an array of  integers

# Print
# -Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

# Input Format
# -A single line of five space-separated integers.

# Output Format
# -Print two space-separated long integers denoting the respective minimum and maximum values that can be
# calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)


def miniMaxSum(arr):
    # sort list
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if arr[i] > arr[j]:
    #             arr[i], arr[j] = arr[j], arr[i]
    arr.sort()

    min_value = arr[0]
    max_value = arr[4]
    print((sum(arr)-max_value), (sum(arr)-min_value))


miniMaxSum([3, 9, 1, 7, 4])

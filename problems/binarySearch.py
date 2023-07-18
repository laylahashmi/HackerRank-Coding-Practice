# Function Needs:
# - Accept a sorted list and a value as arguments
# - Check the middle value
# - Return an index if the value is what you're searching for
# - Return -1 if the value isn't in the list
# - Search a small index range if the value hasn't been found and the index
# range still contains values

def binary_search(lst, value, left=None, right=None):
    """
    Return index of value in sorted list.
    If value is not present, return -1

    Keyword arguments:
    lst -- a sorted list
    value -- value to be located in the list
    left (optional, default None) -- left bound of index range
    right (optional, default None) -- right bound of index range
    """

    # First: Set initial index range, return -1 if the list is empty
    if left is None and right is None:
        right = len(lst)

        # Return -1 for empty list
        if right == 0:
            return -1

        left = 0

    # Second: Check the middle value in this index range
    # --Get middle index of the index range
    mid = (left + right) // 2

    # Base case: last item in index range is not the value, return -1
    if right - left <= 1 and lst[mid] != value:
        return -1

    # Base case: found the value at middle index, return index
    if list[mid] == value:
        return mid

    # Recursive case: check value for new, smaller index range
    # -- value checked was greater than arg value
    elif lst[mid] > value:
        return binary_search(lst, value, left=left, right=(mid-1))

    # -- value checked was less than arg value
    elif lst[mid] < value:
        return binary_search(lst, value, left=(mid+1), right=right)


print(binary_search([1, 2, 3, 4, 6, 8, 9, 14,
      17, 23, 35, 36, 37, 48, 49, 50, 52], 17))

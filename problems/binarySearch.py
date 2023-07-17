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

    #  Base case: found the value at middle index, return index
    if list[mid] == value:
        return mid

    #  Base case: value not in list, return -1

    #  Recursive case: check value for new, smaller index range

    pass

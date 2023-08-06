def pageCount(n, p):
    # number of turns from the front of the book to reach p
    front = p//2  # double slash will give us an integer while single slash can give float/decimal
    # dividing by 2 because each turn of the page goes over 2 pages

    # number of turns from the back of the book to reach p
    n = n + 1 if n % 2 == 0 else n  # if n is even, add 1 to n else do nothing
    # total number of pages - page to reach = distance from last page to p
    back = (n - p)//2

    # min number of turns
    return min(front, back)

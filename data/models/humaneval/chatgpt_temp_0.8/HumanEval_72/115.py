def will_it_fly(q,w):
    # check if q is palindromic
    if q == q[::-1]:
        # check if sum of elements in q is less than or equal to w
        if sum(q) <= w:
            return True
    return False

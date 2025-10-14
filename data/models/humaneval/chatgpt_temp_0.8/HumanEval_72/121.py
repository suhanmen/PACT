def will_it_fly(q,w):
    # check if q is a palindromic list:
    if q == q[::-1]:
        # check if the sum of elements in q is less than or equal to w:
        if sum(q) <= w:
            return True
    return False

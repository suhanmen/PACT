def will_it_fly(q,w):
    # Check if q is a palindromic list
    if q == q[::-1]:
        # Check if sum of elements in q is less than or equal to maximum possible weight w
        if sum(q) <= w:
            return True
    return False

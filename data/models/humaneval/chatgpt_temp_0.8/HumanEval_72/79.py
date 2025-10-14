def will_it_fly(q,w):
    # Check if q is a palindromic list
    if q == q[::-1]:
        # Check if the sum of elements in q is less than or equal to w
        if sum(q) <= w:
            return True
        else:
            return False
    else:
        return False

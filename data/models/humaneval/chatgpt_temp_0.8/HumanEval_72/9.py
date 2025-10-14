def will_it_fly(q,w):
    # Check if the object is balanced
    if q == q[::-1]:
        # Check if the sum of elements is less than or equal to w
        if sum(q) <= w:
            return True
        else:
            return False
    else:
        return False

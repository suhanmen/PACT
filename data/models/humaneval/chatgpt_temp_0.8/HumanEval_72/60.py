def will_it_fly(q,w):
    # Check if the object is balanced (palindromic):
    if q == q[::-1]:
        # Check if the sum of the elements is less than or equal to the maximum weight:
        if sum(q) <= w:
            return True
    return False

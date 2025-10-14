def will_it_fly(q,w):
    if q != q[::-1]: # Check if the list is not palindromic
        return False
    if sum(q) > w: # Check if the sum of elements is greater than the maximum weight
        return False
    return True

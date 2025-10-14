def will_it_fly(q,w):
    if q != q[::-1]: # if the input list is not balanced (not a palindrome)
        return False
    elif sum(q) > w: # if the sum of the input list is greater than the maximum possible weight
        return False
    else:
        return True

def will_it_fly(q,w):
    # check if the list is palindromic
    if q == q[::-1]:
        # calculate the sum of elements in the list
        total_weight = sum(q)
        # check if the sum of elements is less than or equal to the maximum possible weight
        if total_weight <= w:
            return True
    return False

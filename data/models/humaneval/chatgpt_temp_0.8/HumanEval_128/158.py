python
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr:
        # return None for empty arr
        return None
    # initialize the product of all signs to 1
    prod = 1
    # initialize the sum of magnitudes to 0
    mag_sum = 0
    # loop through the array
    for i in arr:
        # update the product of all signs
        if i > 0:
            prod *= 1
        elif i < 0:
            prod *= -1
        else:
            prod *= 0
        # update the sum of magnitudes
        mag_sum += abs(i)
    # return the product of all signs multiplied by the sum of magnitudes
    return prod * mag_sum

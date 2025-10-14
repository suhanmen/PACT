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
    if len(arr) == 0:
        return None

    magnitude_sum = 0
    sign_product = 1

    for num in arr:
        magnitude_sum += abs(num)

        if num == 0:
            sign = 0
        elif num > 0:
            sign = 1
        else:
            sign = -1

        sign_product *= sign

    return magnitude_sum * sign_product

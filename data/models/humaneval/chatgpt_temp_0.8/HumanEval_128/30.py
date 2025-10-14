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

    product_of_signs = 1
    sum_of_magnitudes = 0

    for num in arr:
        if num > 0:
            sum_of_magnitudes += num
            product_of_signs *= 1
        elif num < 0:
            sum_of_magnitudes += abs(num)
            product_of_signs *= -1
        else:
            product_of_signs *= 0

    return sum_of_magnitudes * product_of_signs

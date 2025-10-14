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
        return None
    
    sign_prod = 1
    mag_sum = 0
    
    for num in arr:
        # Determine the sign of the number
        if num > 0:
            sign = 1
        elif num < 0:
            sign = -1
        else:
            sign = 0
        
        # Multiply the sign into the running product
        sign_prod *= sign
        
        # Add the magnitude of the number into the running sum
        mag_sum += abs(num)
    
    return sign_prod * mag_sum

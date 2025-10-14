def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1): # start with n-1 and decrement the value till 1
        if n % i == 0: # check if i divides n evenly
            return i # return i as the largest divisor
    return 1 # if no other divisor is found, return 1 as the largest divisor

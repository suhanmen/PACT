def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1): # loop backwards from n-1 to 1
        if n % i == 0: # if i divides n evenly
            return i # return i as the largest divisor
    return 1 # if no divisor is found except 1, return 1

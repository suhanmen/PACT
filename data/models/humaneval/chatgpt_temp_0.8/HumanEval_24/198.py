def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1): # start from n-1 and go downwards
        if n % i == 0: # i divides n evenly
            return i
    return 1 # if no divisor found, return 1 as every number is divisible by 1

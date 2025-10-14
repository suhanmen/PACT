def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1):  # start from n-1 and go backwards to 1
        if n % i == 0:  # check if i divides n evenly
            return i  # return the first divisor found
    return 1  # if no divisor found other than 1, return 1

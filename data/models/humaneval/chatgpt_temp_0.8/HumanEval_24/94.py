def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 1, -1):  # loop through all possible divisors, starting from n-1 and going down to 2
        if n % i == 0:  # if i evenly divides n, return it
            return i
    return 1  # if no divisor other than 1 is found, return 1

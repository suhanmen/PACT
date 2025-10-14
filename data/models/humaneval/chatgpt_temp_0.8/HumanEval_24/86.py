def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1):  # start from n-1 and iterate down to 1
        if n % i == 0:  # check if i is a divisor of n
            return i
    return 1  # if no divisor is found, return 1

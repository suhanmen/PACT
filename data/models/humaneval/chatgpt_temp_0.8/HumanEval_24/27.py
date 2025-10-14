def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1):  # iterate backwards from n-1 to 1
        if n % i == 0:  # if i divides n evenly, return it
            return i
    return 1  # if no divisor is found, return 1 (the smallest divisor)

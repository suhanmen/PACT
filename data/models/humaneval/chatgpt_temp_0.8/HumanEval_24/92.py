def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest_div = n-1
    while largest_div >= 1:
        if n % largest_div == 0:
            return largest_div
        largest_div -= 1
    return None

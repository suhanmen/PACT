def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest_div = 1
    for i in range(2, n//2 + 1):
        if n % i == 0:
            largest_div = i
    return largest_div

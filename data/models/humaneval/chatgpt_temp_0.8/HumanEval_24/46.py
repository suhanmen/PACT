def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    max_divisor = 1
    for i in range(2, n):
        if n % i == 0:
            max_divisor = i
    return max_divisor

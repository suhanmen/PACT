def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Check for edge case when n is 1
    if n == 1:
        return None
    
    # Find the largest divisor
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Initialize the largest divisor to be the floor division of n by 2
    largest = n // 2
    
    # Loop through all numbers from largest to 1
    for i in range(largest, 0, -1):
        # If i divides n evenly, return i
        if n % i == 0:
            return i
    
    # If no divisor is found, return 1 as the largest divisor
    return 1

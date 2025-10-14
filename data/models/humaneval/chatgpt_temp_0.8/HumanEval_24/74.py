def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1): # looping through all numbers smaller than n in descending order
        if n % i == 0: # checking if i divides n evenly
            return i # returning the largest such i

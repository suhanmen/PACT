def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest = 1 # initialize the largest divisor to 1
    for i in range(2, n): # loop through all the numbers between 2 and n-1
        if n % i == 0: # if i is a divisor of n
            largest = i # update the largest divisor
    return largest # return the largest divisor

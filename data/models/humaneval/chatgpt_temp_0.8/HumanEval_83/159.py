def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:  # If n is 1, only one-digit numbers can be counted
        count = 2
    elif n > 1:  # If n is more than 1, all n-digit numbers that start or end with 1 can be counted
        count = 2 * 9**(n-1) - 8**(n-1)
    return count

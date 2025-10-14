def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2  # There are only two 1-digit numbers that start or end with 1
    
    # Count the number of n-digit numbers that start or end with 1
    count = 9 * (10 ** (n - 2)) + 2 * starts_one_ends(n - 1)
    
    return count

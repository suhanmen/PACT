def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        # If n is 1, only 1 satisfies the condition
        count = 1
    else:
        # If n is greater than 1, count the numbers that start and end with 1
        count = 9 * (2**(n-2))
    return count

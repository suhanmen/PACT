def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        count = 1
    elif n == 2:
        count = 10
    else:
        count = 9 * (10 ** (n-2)) * 2
    return count

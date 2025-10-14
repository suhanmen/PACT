def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        count = 1
    elif n > 1:
        count = 2 * 9 * (10 ** (n-2))
        # 2 comes from 1 at start or end, 9 choices for the other digits, and (n-2) digits remaining
    return count

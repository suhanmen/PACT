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
        # 2 choices for the first digit (1 or 9)
        # 9 choices for each of the remaining digits
        # Multiply by 10 raised to the power of (n-2) to account for remaining digits
    return count

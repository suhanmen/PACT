def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2  # There are two 1-digit numbers that start or end with 1: 1 and 10.
    else:
        count += 9 * 2  # The first digit can be any of the non-zero digits (9) and the last digit can be 1 or 0 (2).
        count += 9 * (10 ** (n - 2)) * 2  # The first digit can be any of the non-zero digits (9) and the last digit can be 1 or 0 (2). The remaining n-2 digits can be any digit (10**(n-2)).
        return count

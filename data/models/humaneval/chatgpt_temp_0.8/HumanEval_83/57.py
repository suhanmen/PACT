def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 1
    # count of numbers starting with 1
    count += 9 * (10 ** (n - 2))
    # count of numbers ending with 1
    count += 9 * (10 ** (n - 2))
    # count of numbers starting and ending with 1
    count += 10 ** (n - 2)
    return count

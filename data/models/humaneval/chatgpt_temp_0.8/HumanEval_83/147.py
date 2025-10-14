def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.

    Args:
    n -- a positive integer

    Returns:
    count -- the count of n-digit positive integers that start or end with 1
    """

    count = 0

    # There are 2 possibilities for the first digit:
    # either it is 1, or it is any other digit (there are 9 possibilities).
    # There are also 2 possibilities for the last digit.
    # Therefore, there are 2 * 9 * 10^(n-2) n-digit integers that start or end with 1.
    count = 2 * 9 * 10**(n-2)

    return count

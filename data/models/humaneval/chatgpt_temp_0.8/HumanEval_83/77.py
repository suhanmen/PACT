def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        count = 2
    elif n > 1:
        count = 2 * 9 * (10 ** (n - 2))
        # First digit can be either 1 or not 1, hence 2 options
        # Last digit can only be 1, hence 1 option
        # The remaining n-2 digits can be any of the digits 0-9 except 1, hence 9 options for each of them
    return count

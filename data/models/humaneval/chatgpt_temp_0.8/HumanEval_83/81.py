def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    start_count, end_count = 0, 0
    if n == 1:
        return 1
    else:
        start_count = 9 * 10 ** (n-2)
        end_count = 10 ** (n-1) - 10 ** (n-2)
        return start_count + end_count

def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    else:
        # Count the numbers that start with 1
        count_start = 9 * pow(10, n-2)
        # Count the numbers that end with 1
        count_end = pow(10, n-1) - pow(10, n-2)
        # Subtract the overlap (i.e., the numbers that start and end with 1)
        count_overlap = 1 * pow(10, n-2)
        return count_start + count_end - count_overlap

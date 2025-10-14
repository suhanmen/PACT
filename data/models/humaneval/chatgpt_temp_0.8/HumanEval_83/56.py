def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    total_count = 0
    if n == 1:
        return 2
    else:
        # Count the number of n-digit integers that start with 1
        count_start_1 = 9 * (10**(n-2))
        # Count the number of n-digit integers that end with 1
        count_end_1 = 9 * (10**(n-2))
        # Count the number of n-digit integers that start and end with 1
        count_start_end_1 = 9 * (10**(n-3))

        # Add up the counts
        total_count = count_start_1 + count_end_1 - count_start_end_1

    return total_count

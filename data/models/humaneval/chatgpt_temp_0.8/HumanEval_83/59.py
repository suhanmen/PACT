def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        # There is only one 1-digit positive integer that starts or ends with 1
        count = 1
    else:
        # There are 9 choices for the first digit (excluding 0 and 1)
        # and 2 choices for the last digit (either 1 or something else)
        count = 9 * 2**(n-2)
        # If n is even, we need to double the count since we're counting both
        # the numbers that start with 1 and the numbers that end with 1
        if n % 2 == 0:
            count *= 2
    return count

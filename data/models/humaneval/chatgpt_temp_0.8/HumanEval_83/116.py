def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1  # Only one 1-digit number starts or ends with 1
    else:
        count = 9  # There are 9 possible digits for the other n-1 positions
        for i in range(2, n):
            count *= 10  # There are 10 possible digits for each of the remaining positions
        return 2 * count + starts_one_ends(n - 1)
